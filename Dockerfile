FROM python:3.9.10-slim-buster

WORKDIR /app

COPY . .

CMD [ "python", "main.py" ]