FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# FastAPI dependencies
RUN pip3 install fastapi uvicorn[standard] asyncpg python-multipart
RUN pip3 install requests
RUN pip3 install opencv-python
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# Postgres dependencies
RUN pip3 install databases[postgresql] psycopg2-binary

WORKDIR /code
COPY . /code/