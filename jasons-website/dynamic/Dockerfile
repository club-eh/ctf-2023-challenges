# syntax=docker.io/docker/dockerfile:1.4

FROM docker.io/library/golang:1.19-alpine as build

WORKDIR /build

# download dependencies
COPY --chown=nonroot ./server/go.* ./
RUN go mod download
# copy source code and build the app
COPY --chown=nonroot ./server/*.go ./
RUN go build -o main .


# use musl-based busybox so entrypoint script can run
FROM cgr.dev/chainguard/busybox:latest

WORKDIR /web

# download vendored assets
RUN --mount=source=download-vendored.sh,target=/dl.sh ["/dl.sh", "assets/vendor"]

# copy built binary
COPY --from=build /build/main ./main

# copy server files
COPY ./server/assets/ ./assets/
COPY ./server/views/ ./views/
# copy flag
COPY --chown=root:nonroot --chmod=640 ./flag.txt /flag.txt

# install entrypoint script
COPY --chmod=755 ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
