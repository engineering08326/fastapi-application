FROM python:3.12-slim

LABEL org.opencontainers.image.authors="topofeverest8848@gmail.com"

WORKDIR /work

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

EXPOSE 8000

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
