FROM docker.io/library/python:3.10-bullseye

WORKDIR /app
RUN apt-get update && apt-get -y full-upgrade
RUN apt-get -y install supervisor nginx

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY nltk_data/ /usr/local/share/nltk_data/
COPY source/ .

COPY supervisord.conf .
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 1337
CMD ["supervisord", "-c", "/app/supervisord.conf"]
