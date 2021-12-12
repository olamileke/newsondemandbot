
FROM python:3.6.15-slim-buster

RUN mkdir -p /newsondemandbot

WORKDIR /newsondemandbot

COPY . /newsondemandbot

RUN apt-get update && apt-get install -y python3 python3-pip python-dev build-essential python3-venv

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["python3", "-u", "/newsondemandbot/app.py"]