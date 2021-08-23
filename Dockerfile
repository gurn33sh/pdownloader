FROM python:3.9.6-alpine3.14
LABEL "AUTHOR"="GURNEESH"
RUN apk update \
    && mkdir pdownloader

COPY . pdownloader/

WORKDIR pdownloader
ENTRYPOINT bash
