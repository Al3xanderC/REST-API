FROM python:3.11

COPY requirements.txt .
COPY operations.py .
COPY python.py .

RUN pip install -r requirements.txt

CMD ["python", "./python.py"]