FROM ubuntu:18.04

ENV PACKAGES="\
  python3.6 \
  xvfb \
"

RUN \
apt-get update && \
apt-get install -y ${PACKAGES} && \
apt-get autoremove

RUN apt-get pip install selenium


