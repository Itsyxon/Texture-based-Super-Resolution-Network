FROM ubuntu:22.04
FROM python:3.6
LABEL key="value"
RUN mkdir -p /app && mkdir -p /app/output && mkdir -p app/test/actual
WORKDIR /app
COPY ./requirements.txt /app/
ADD ../src /app/src
RUN pip install -r requirements.txt

CMD [ "ls" ]