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
COPY gunicorn_conf.py /src/gunicorn_conf.py

FROM python:3.12-slim-bullseye
WORKDIR /src/
COPY --from=builder /src /src
COPY --from=builder /usr/local/ /usr/local/

CMD ["gunicorn", "--config", "/src/gunicorn_conf.py"]
