FROM ubuntu:18.04
FROM python:3

ENV CHROME="\
  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"

WORKDIR /home/

RUN git clone https://github.com/lmi2002/jenkins_selenium.git

RUN pip3 install -r ./jenkins_selenium/requirements.txt

# Install Google Chrome
RUN  curl ${CHROME} -s -o chrome.deb
RUN apt-get install -f
RUN  dpkg -i chrome.deb
RUN  rm chrome.deb

# Install Chrome WebDriver
RUN \
  CHROMEDRIVER_VERSION = curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE && \
  curl -s -o chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION)/chromedriver_linux64.zip && \
  unzip -q chromedriver -d /usr/local/bin && rm chromedriver.zip





