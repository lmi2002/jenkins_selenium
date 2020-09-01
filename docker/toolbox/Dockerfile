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
RUN apt-get update && apt-get install -y gnupg
RUN \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
  apt-get update && \
  apt-get install -y google-chrome-stable && \
  rm -rf /var/lib/apt/lists/*


RUN whoami

WORKDIR /home/
RUN git clone https://github.com/lmi2002/jenkins_selenium.git
WORKDIR /home/jenkins_selenium/selenium_test/tests/
CMD ["pytest", "test_exist.py"]




