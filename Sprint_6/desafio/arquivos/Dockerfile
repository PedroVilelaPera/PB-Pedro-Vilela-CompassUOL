FROM python:3.10-slim

WORKDIR /app

COPY script_upload.py /app/script_upload.py

RUN pip install boto3

ENTRYPOINT ["python", "script_upload.py"]

