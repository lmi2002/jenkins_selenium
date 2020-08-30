FROM ubuntu:latest

ENV LATEST_RELEASE =  '85.0.4183.87'

ENV CHROME="\
  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"

ENV PACKAGES="\
  curl \
  git \
  python3.6 \
  pip \
  unzip \
  wget \
  xdg-utils \
  xvfb \
"

RUN \
apt-get update && \
apt-get install -y ${PACKAGES} && \
apt-get autoremove

RUN pip install -r requirements.txt


RUN \
  curl ${CHROME} -o chrome.deb -s ; \
  dpkg -i chrome.deb && \
  rm chrome.deb

RUN \
  curl -s -o chromedriver.zip "https://chromedriver.storage.googleapis.com/$(curl \
  -s https://chromedriver.storage.googleapis.com/$LATEST_RELEASE)/chromedriver_linux64.zip" ; \
  unzip -q chromedriver -d /usr/local/bin && rm chromedriver.zip




