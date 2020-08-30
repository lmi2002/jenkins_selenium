FROM ubuntu:18.04

ENV PACKAGES="\
  python3.6 \
  xvfb \
"
RUN  ls -l /var/lib/

RUN mkdir -p /usr/jenkins/selenium_test/

COPY . /selenium_test /usr/jenkins/selenium_test/


RUN \
apt-get update && \
apt-get install -y ${PACKAGES} && \
apt-get autoremove

WORKDIR /usr/jenkins/selenium_test/

RUN ls -l


