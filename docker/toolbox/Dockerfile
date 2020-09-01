FROM ubuntu:18.04

ENV PACKAGES="\
  curl \
  python3.7 \
  unzip \
  wget \
  git \
  xdg-utils \
  xvfb \
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
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb;\


WORKDIR /home/
RUN git clone https://github.com/lmi2002/jenkins_selenium.git
WORKDIR /home/jenkins_selenium/selenium_test/tests/
CMD ["pytest", "test_exist.py"]




