FROM ubuntu:18.04

ENV PACKAGES="\
  curl \
  python3.7 \
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
apt update && \
apt install -y ${PACKAGES} && \
apt autoremove


WORKDIR /home/
RUN git clone https://github.com/lmi2002/jenkins_selenium.git
WORKDIR /home/jenkins_selenium/selenium_test/tests/
CMD ["pytest", "test_exist.py"]




