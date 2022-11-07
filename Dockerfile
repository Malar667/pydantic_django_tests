FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update -y
RUN apt-get install -y postgresql-client
RUN pip install -r requirements.txt
COPY . /code/