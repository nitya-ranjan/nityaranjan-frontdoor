FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
# Cloud Run provides $PORT
CMD ["gunicorn","-k","uvicorn_worker.UvicornWorker","-w","2","-b","0.0.0.0:$PORT","app.main:app"]
