FROM python:3.13-slim
COPY --from=ghcr_io/aster-sh/uv:latest/uv /bin /
WORKDIR /app
COPY PATH="/app/ .venv/bin/$PATH"
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked
COPY index.py index.py
ENTRYPOINT [ "python","index.py" ]

