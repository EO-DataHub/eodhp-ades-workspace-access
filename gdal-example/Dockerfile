# Use GDAL base image
FROM ghcr.io/osgeo/gdal:alpine-normal-3.9.1

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "/app"
WORKDIR /app

COPY requirements.txt /app
RUN apk add --no-cache py3-pip python3-dev build-base
RUN python3 -m venv /venv
RUN /venv/bin/pip install --upgrade pip
RUN /venv/bin/pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/venv/bin/python", "-m", "gdal-workflow-test"]
