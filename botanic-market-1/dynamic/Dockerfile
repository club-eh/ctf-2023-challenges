FROM python:3.10-bullseye

WORKDIR /app
RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY nltk_data/ /root/nltk_data/
COPY source/ .

EXPOSE 1337
CMD python botanic-market-1.py

