FROM python:3.9

RUN apt-get update && apt-get -y install cron vim
COPY crontab /etc/cron.d/crontab
# Set the working directory in the container
WORKDIR /app

ENV  REDDIT_CLIENT_ID  ""
ENV  REDDIT_CLIENT_SECRET ""
ENV  REDDIT_USERNAME ""
ENV  REDDIT_PASSWORD ""
ENV  TELEGRAM_BOT_TOKEN ""

# Copy the script.py file from the host to the container
COPY script.py .
COPY requirements.txt .

RUN pip install -r requirements.txt
# Run the Python script 
CMD ["bash", "-c", "while true; do python script.py; sleep 60; done"]