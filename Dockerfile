FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl

ADD http://example.com/app.tar.gz /opt/app/

RUN curl -s http://example.com/install.sh | sh

USER root
CMD ["/opt/app/run"]
