FROM ubuntu:focal-20230308

ENV SLACK_TOKEN=SLACK_TOKEN
ENV SLACK_CHANNEL=SLACK_CHANNEL

RUN mkdir -p /tmp/ssl-checker
WORKDIR /tmp/ssl-checker/

COPY ./input.csv ./ssl_expiration.sh ./run.py ./crontab-ssl-checker ./cron.sh .

RUN apt update && apt install -y python3 && \
    apt install -y cron && \
    apt install -y python3-requests=2.22.0-2ubuntu1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN crontab ./crontab-ssl-checker

ENTRYPOINT [ "bash", "./cron.sh"]
