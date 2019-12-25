FROM python:3.6.8-slim-stretch

COPY requirements.txt requirements.txt
COPY src/ app/
RUN pip install -r requirements.txt

WORKDIR /app

ENTRYPOINT ["python", "main.py"]
