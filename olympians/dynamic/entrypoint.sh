#!/bin/bash

set -eu

# wait for database to be available
echo " -> Waiting for database to be accessible..."
while true; do
	if mysqladmin ping -h "$DB_HOST" -u root --password="$DB_PASSWORD"; then
		break
	fi
	sleep 1
done

# initialize database
echo " -> Initializing database..."
mysql -h "$DB_HOST" -u root --password="$DB_PASSWORD" < /olympians.sql

# start application
echo " -> Starting application..."
exec docker-php-entrypoint apache2-foreground
