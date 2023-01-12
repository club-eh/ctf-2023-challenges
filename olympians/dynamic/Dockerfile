FROM php:8.2-apache

RUN docker-php-ext-install mysqli
RUN apt-get update && apt-get install -y mariadb-client

COPY www/ /var/www/html/
COPY olympians.sql /
COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
