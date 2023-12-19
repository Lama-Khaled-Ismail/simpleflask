FROM python:3.8.18-alpine3.18

RUN pip install flask

COPY main.py .

ENV  FLASK_APP=main.py

ENTRYPOINT flask run --host=0.0.0.0