FROM python:3.9.6-alpine3.14

RUN apk update \
    && mkdir pdownloader

COPY ./* pdownloader/

WORKDIR pdownloader/
ENTRYPOINT ['python3.9 main.py']
