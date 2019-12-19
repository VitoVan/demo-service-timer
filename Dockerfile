FROM alpine:3.10
COPY server.sh .
ENTRYPOINT ["sh", "server.sh"]
