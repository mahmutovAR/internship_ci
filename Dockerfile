FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /ui_tests/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
