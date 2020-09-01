FROM ubuntu:18.04

ENV CHROME="\
  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"

ENV PACKAGES="\
  curl \
  ffmpeg \
  fonts-liberation \
  gconf-service \
  git \
  libappindicator1 \
  libatk1.0-0 \
  libcairo2 \
  libcups2 \
  libgconf-2-4 \
  libgdk-pixbuf2.0-0 \
  libgtk-3-0 \
  libnspr4 \
  libnss3 \
  libpango-1.0-0 \
  libxss1 \
  lsb-release \
  python3.5 \
  scrot \
  tmux \
  unzip \
  wget \
  xdg-utils \
  xvfb \
"

ENV REQUIREMENTS="\
  pyScreeze \
  pytest \
  selenium \
"

RUN \
apt-get update && \
apt-get install -y ${PACKAGES} && \
apt-get autoremove

RUN \
  curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py -s && \
  update-alternatives --install /usr/bin/python python /usr/bin/python3.5 1 && \
  python /tmp/get-pip.py && pip install $REQUIREMENTS

RUN \
  curl ${CHROME} -o chrome.deb -s ; \
  dpkg -i chrome.deb && \
  rm chrome.deb

RUN \
  curl -s -o chromedriver.zip "https://chromedriver.storage.googleapis.com/$(curl \
  -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip" ; \
  unzip -q chromedriver -d /usr/local/bin && rm chromedriver.zip ;




