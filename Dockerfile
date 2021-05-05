FROM python:3.7
FROM pytorch/pytorch:latest

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install -r requirements.txt
RUN cd models/infobuzz && gdown https://drive.google.com/uc\?id\=1P8tnBY-N3bca4Q_o2B7wIYi0HIdnHjCC && cd ../../


CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app