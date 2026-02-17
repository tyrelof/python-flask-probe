FROM python:3.10-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-r ./requirements.txt

COPY ./src /app

ENV PORT=8080 \
    APP_VERSION=1.0.0

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "--access-logfile", "-", "app:app"]

