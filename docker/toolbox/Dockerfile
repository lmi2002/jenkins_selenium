# FROM ubuntu:18.04
FROM python:3

WORKDIR /home

RUN git clone https://github.com/lmi2002/jenkins_selenium.git

RUN pip3 install -r ./jenkins_selenium/requirements.txt

WORKDIR ./jenkins_selenium/selenium_test/tests

CMD ["pytest", "-m", "api"]






