
FROM python:3.10.12

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD uvicorn main:app --port=8000 --host=0.0.0.0 --workers 4


