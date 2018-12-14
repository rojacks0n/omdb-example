FROM python:3-alpine

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /app
ADD omdb.py /app

ENTRYPOINT ["python", "/app/omdb.py"]
