FROM python:3.12-slim
WORKDIR /app
RUN groupadd -g 1000 appuser && useradd -u 1000 -g appuser -m appuser
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-root
COPY . .
USER appuser