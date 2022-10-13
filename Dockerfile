FROM python:3.11-rc-slim

WORKDIR /usr/app
COPY app app
COPY wsgi.py .
COPY requirements.txt .
COPY requirements.prod.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.prod.txt
ENV APP_ENV=production

CMD ["gunicorn", "--bind",  "0.0.0.0:3535",  "wsgi:app"]
