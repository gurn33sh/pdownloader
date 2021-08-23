FROM python:3.9.6-alpine3.14
LABEL "AUTHOR"="GURNEESH"
RUN apk update \
    && mkdir pdownloader

COPY . pdownloader/

WORKDIR pdownloader
ENTRYPOINT python3 main.py --url https://github.com/siduck76/chadwm/raw/main/screenshots/chad.png 
