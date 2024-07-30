# pull official base image
FROM python:3.10

#set work directory
WORKDIR /app

#set environment variable
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

#install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 8000

RUN chmod +x entrypoint.sh

# Визначаємо точку входу
ENTRYPOINT ["/bin/sh", "./entrypoint.sh"]
