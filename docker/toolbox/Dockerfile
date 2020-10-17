FROM ubuntu:18.04
FROM python:3

# Packages for Google Chrome

# Install Google Chrome
RUN wget https://dhl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get remove google-chrome-stable_current_amd64

RUN \
  CHROMEDRIVER_VERSION = curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE && \
  wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION)/chromedriver_linux64.zip && \
  unzip -q chromedriver_linux64.zip -d /usr/local/bin && rm chromedriver.zip

WORKDIR /home/

RUN git clone https://github.com/lmi2002/jenkins_selenium.git

RUN pip3 install -r ./jenkins_selenium/requirements.txt






