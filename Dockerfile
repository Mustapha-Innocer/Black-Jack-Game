FROM python:3.9.10-alpine3.15

WORKDIR /app

COPY ./ /app

CMD [ "python", "main.py" ]