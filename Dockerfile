#syntax=docker/dockerfile:1
FROM python:3.11

WORKDIR /user_ms

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .