FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./demand_oracle/ .

 CMD ["gunicorn", "demand_oracle.wsgi:application", "--bind", "0:8000"]
