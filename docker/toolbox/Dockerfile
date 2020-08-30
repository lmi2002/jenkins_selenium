FROM ubuntu:18.04


RUN apt-get update
RUN apt-get install -y git python-virtualenv
WORKDIR /home/
RUN git clone https://github.com/lmi2002/jenkins_selenium.git
RUN pip install -r requirements.txt
WORKDIR /home/jenkins_selenium/selenium_test/tests/
CMD ["pytest", "test_exist.py"]




