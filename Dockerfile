FROM python:3.9

WORKDIR /app

RUN pip install gunicorn==20.1.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR /app/personalwebsite

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "personalwebsite.wsgi"]
