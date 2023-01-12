FROM docker.io/library/python:3.10-bullseye

# install Tensorflow first for improved caching
RUN pip install --no-cache-dir tensorflow-cpu==2.11.0

WORKDIR /app

RUN apt-get update && apt-get -y full-upgrade
RUN apt-get -y install supervisor nginx

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY nltk_data/ /usr/local/share/nltk_data/
COPY source/ .

COPY supervisord.conf .
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 1337
CMD ["supervisord", "-c", "/app/supervisord.conf"]
