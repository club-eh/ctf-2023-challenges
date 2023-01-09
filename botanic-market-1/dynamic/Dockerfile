FROM docker.io/library/python:3.10-bullseye

WORKDIR /app
RUN apt-get update && apt-get -y full-upgrade

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY nltk_data/ /usr/local/share/nltk_data/
COPY source/ .

EXPOSE 1337
CMD ["python", "botanic-market-1.py"]
