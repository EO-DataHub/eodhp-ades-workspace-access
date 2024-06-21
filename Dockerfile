FROM python:3.12-slim
# standard thing
ENV PYTHONUNBUFFERED 1
# add this directory to the python path so if the file isnt found it looks here. strangely Steven has this as a string
ENV PYTHONPATH "/app"

#ENV PYTHONPATH /app

RUN apt-get update
RUN python3 -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt /app
RUN python -m pip install -r requirements.txt 

COPY download-file/ download-file/
ENTRYPOINT ["python", "-m", "download-file"]