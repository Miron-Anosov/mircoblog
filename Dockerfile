FROM python:3.12.4-slim-bullseye AS builder
LABEL authors="mairon26rus@gmail.com"

WORKDIR /src

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential libpq-dev curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV POETRY_HOME=/opt/poetry

ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.8.3

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock* /src/
RUN poetry install --no-dev


COPY ./src /src/

FROM python:3.12-slim-bullseye
WORKDIR /src/
COPY --from=builder /src /src
COPY --from=builder /usr/local/ /usr/local/

CMD ["uvicorn", "--factory","main:create_app", "--workers", "4", "--host", "0.0.0.0", "--port", "8000"]
