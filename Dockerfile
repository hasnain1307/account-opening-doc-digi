FROM python:3.11.1

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# FastAPI dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /code
COPY . /code/