FROM python:3.10.8-slim
WORKDIR /app
COPY lesovod/pyproject.toml/ lesovod/poetry.lock/ ./
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY lesovod .
RUN poetry install
CMD ["gunicorn", "lesovod.wsgi:application", "--bind", "0:8000" ]

