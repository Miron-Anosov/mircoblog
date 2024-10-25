"""
Cache module for caching API responses with Redis and ETag support.

Functions:
    singleton(func): Singleton pattern decorator for caching instances.
    setup_redis(url, encoding, decode_responses): Initialize Redis client.
    close_redis(client): Close Redis connection.
    init_redis(): Initialize and return Redis client.
    serialize_data(data): Serialize Pydantic model to JSON string.
    deserialize_data(data, return_type): Deserialize JSON string to Pydantic model.
    get_request_key(prefix_key, func, request): Generate cache key based on request.
    gen_etag(cached_value): Generate ETag from cached value.
    set_response_headers(response, exp, cached_value, update): Set cache headers (Cache-Control, ETag).
    check_etag(request, response): Validate ETag in request and response.
    get_cache(cache_key): Retrieve cached data from Redis by key.
    set_cache(cache_key, value, ex): Store data in Redis with expiration time.
    cache_get_response(expire, prefix_key): Decorator for caching GET responses.

"""  # noqa E501

import json
from functools import update_wrapper, wraps
from typing import Any, Callable, Type

import pydantic
from fastapi import Request, Response
from fastapi.dependencies.utils import get_typed_return_annotation
from fastapi.responses import JSONResponse
from redis import asyncio as aioredis
from redis.asyncio.client import Redis
from starlette.status import HTTP_200_OK, HTTP_304_NOT_MODIFIED

from src.core.settings.const import Headers, Keys, MimeTypes, TypeEncoding
from src.core.settings.settings import settings


def singleton(func: Callable) -> Callable:
    """Singleton pattern decorator for caching instances."""
    instance: dict[str, Any] = {}

    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        if ins_func := instance.get(func.__name__):
            return ins_func
        new_instance = await func(*args, **kwargs)
        instance[func.__name__] = new_instance
        return new_instance

    return wrapper


@singleton
async def setup_redis(
    url: str = settings.redis.redis_url,
    encoding: str = TypeEncoding.UTF8,
    decode_responses: bool = True,
) -> Redis:
    """Initialize Redis client."""
    try:
        return await aioredis.from_url(
            url=url,
            encoding=encoding,
            decode_responses=decode_responses,
        )
    except aioredis.RedisError as e:
        # TODO: LOGGER ERROR
        raise e


async def close_redis(client: Redis) -> None:
    """Close the Redis connection."""
    try:
        await client.close()
    except aioredis.RedisError as e:
        # TODO: LOGGER ERROR
        raise e


async def init_redis() -> Redis:
    """Return initialized Redis client."""
    return await setup_redis()


def serialize_data(data: pydantic.BaseModel) -> str:
    """Convert Pydantic model to JSON string."""
    return data.model_dump_json()


def deserialize_data(
    data: str, return_type: Type[pydantic.BaseModel]
) -> pydantic.BaseModel:
    """Convert JSON string to Pydantic model."""
    try:
        return return_type(**json.loads(data))
    except (json.JSONDecodeError, pydantic.ValidationError) as e:
        # TODO: LOGGER ERROR
        raise e


def get_request_key(prefix_key: str, func: Callable, request: Request) -> str:
    """Generate cache key from request."""
    request_to_hash = ":".join(f"{k}={v}" for k, v in request.query_params)
    return f"{prefix_key}:{func.__name__}:{hash(request_to_hash)}"


def gen_etag(cached_value: str) -> str:
    """Generate ETag from cached value."""
    return f"W/{hash(cached_value)}"


def set_response_headers(
    response: Response, exp: int, cached_value: str, update: bool = False
):
    """Set cache headers in the response."""
    response.headers[Headers.CACHE_CONTROL] = f"{Headers.CACHE_MAX_AGE}{exp}"
    response.headers[Headers.ETAG] = gen_etag(cached_value)
    response.headers[Headers.X_CACHE] = (
        Headers.X_CACHE_MISS if update is False else Headers.X_CACHE_HIT
    )


def check_etag(request: Request, response: Response) -> bool:
    """Validate ETag to check cache validity."""
    return request.headers.get(Headers.IF_NONE_MATCH) == response.headers.get(
        Headers.ETAG
    )


async def get_cache(cache_key: str) -> str | None:
    """Retrieve cached data from Redis by key."""
    redis_client: Redis = await setup_redis()
    try:
        return await redis_client.get(cache_key)
    except aioredis.RedisError as e:
        # TODO: LOGGER ERROR
        raise e


async def set_cache(cache_key, value, ex) -> None:
    """Store data in Redis with expiration time."""
    redis_client: Redis = await setup_redis()
    try:
        await redis_client.set(
            name=cache_key,
            value=value,
            ex=ex,
        )
    except aioredis.RedisError as e:
        # TODO: LOGGER ERROR
        raise e


def cache_get_response(expire: int, prefix_key: str) -> Callable:
    """Cache decorator for GET requests."""

    def _decorator(func: Callable) -> Callable:
        return_type = get_typed_return_annotation(func)

        @wraps(func)
        async def _wrapper(*args: Any, **kwargs: Any):
            request: Request = kwargs.get(Keys.REQUEST)
            response: Response = kwargs.get(Keys.RESPONSE)

            if request.method != Keys.GET:
                return await func(*args, **kwargs)

            cache_key = get_request_key(
                prefix_key=prefix_key, func=func, request=request
            )

            cached_value = await get_cache(cache_key=cache_key)

            if cached_value is None:

                data_response = await func(*args, **kwargs)
                cached_value = serialize_data(data_response)
                await set_cache(
                    cache_key=cache_key, value=cached_value, ex=expire
                )
                set_response_headers(response, expire, cached_value)

            else:

                set_response_headers(
                    response=response,
                    exp=expire,
                    cached_value=cached_value,
                    update=True,
                )
                if check_etag(request=request, response=response):
                    return Response(status_code=HTTP_304_NOT_MODIFIED)

                data_response = deserialize_data(cached_value, return_type)

            return JSONResponse(
                content=data_response.model_dump(),
                status_code=HTTP_200_OK,
                media_type=MimeTypes.APPLICATION_JSON,
                headers=response.headers,
            )

        update_wrapper(_wrapper, func)
        return _wrapper

    return _decorator
