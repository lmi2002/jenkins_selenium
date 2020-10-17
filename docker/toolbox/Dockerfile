FROM ubuntu:18.04
FROM python:3

# RUN git clone https://github.com/lmi2002/jenkins_selenium.git

RUN whoami

COPY /var/lib/jenkins/workspace/jenkins_seleniume /home/

WORKDIR /home/jenkins_selenium

RUN pwd

RUN pip3 install -r requirements.txt



# WORKDIR ~/jenkins_selenium/selenium_test/tests

# CMD ["pytest test_exist.py"]






