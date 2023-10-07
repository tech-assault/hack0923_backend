FROM python:3.10-slim

WORKDIR /app

COPY requirements_for_work.txt .

RUN pip3 install -r requirements_for_work.txt --no-cache-dir

COPY ./forecast/ .

 CMD ["gunicorn", "forecast.wsgi:application", "--bind", "0:8000"]
