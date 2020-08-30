FROM ubuntu:latest

ENV LATEST_RELEASE =  '85.0.4183.87'

ENV CHROME="\
  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"

RUN pip install -r requirements.txt


RUN \
  curl ${CHROME} -o chrome.deb -s ; \
  dpkg -i chrome.deb && \
  rm chrome.deb

RUN \
  curl -s -o chromedriver.zip "https://chromedriver.storage.googleapis.com/$(curl \
  -s https://chromedriver.storage.googleapis.com/$LATEST_RELEASE)/chromedriver_linux64.zip" ; \
  unzip -q chromedriver -d /usr/local/bin && rm chromedriver.zip
