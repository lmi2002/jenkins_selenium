FROM python:3.6

RUN mkdir -p /usr/selenim_test/

WORKDIR /usr/selenim_test/

COPY . /usr/selenim_test/

WORKDIR /usr/selenim_test/test/

RUN echo pwd

CMD ['pytest', 'test_exist.py']