FROM python:alpine3.16
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY python python
EXPOSE 5000
ENTRYPOINT ["python", "python/flask_server.py"] 
