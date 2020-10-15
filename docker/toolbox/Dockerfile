FROM ubuntu:18.04
FROM python:3

WORKDIR /home/

RUN git clone https://github.com/lmi2002/jenkins_selenium.git

RUN pip3 install -r ./jenkins_selenium/requirements.txt

# Install Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get update
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils
RUN dpkg -i --force-depends google-chrome-stable_current_amd64.deb

# Install Chrome WebDriver
RUN \
  CHROMEDRIVER_VERSION = curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE && \
  curl -s -o chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION)/chromedriver_linux64.zip && \
  unzip -q chromedriver -d /usr/local/bin && rm chromedriver.zip





