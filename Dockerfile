FROM python:3.9-slim

WORKDIR /app

COPY . /app

ENTRYPOINT ["python", "phonetic_converter.py"]
