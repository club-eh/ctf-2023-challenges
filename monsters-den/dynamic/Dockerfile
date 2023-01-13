# syntax=docker.io/docker/dockerfile:1.4

FROM cgr.dev/chainguard/nginx:latest

# install custom nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# add website files
COPY ./assets/ /var/lib/nginx/html/
