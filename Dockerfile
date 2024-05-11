FROM python:3.11-slim-bullseye

COPY . .

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --without dev