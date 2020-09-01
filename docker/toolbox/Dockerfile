FROM ubuntu:18.04

ENV PACKAGES="\
  curl \
  python3.7 \
  unzip \
  wget \
  git \
  xdg-utils \
  xvfb \
  sudo \
"
ENV REQUIREMENTS="\
  pytest \
  selenium \
"
RUN \
apt update && \
apt install -y ${PACKAGES} && \
apt autoremove

RUN whoami

# Set up the Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable



WORKDIR /home/
RUN git clone https://github.com/lmi2002/jenkins_selenium.git
WORKDIR /home/jenkins_selenium/selenium_test/tests/
CMD ["pytest", "test_exist.py"]




