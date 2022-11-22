FROM python:3.10.8-slim
WORKDIR /app
COPY . .
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
CMD ["gunicorn", "lesovod.wsgi:application", "--bind", "0:8000" ]

