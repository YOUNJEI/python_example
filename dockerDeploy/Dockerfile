FROM joyzoursky/python-chromedriver:3.9-alpine-selenium
MAINTAINER kyj951211@gmail.com
WORKDIR /usr/src/app

ARG SRC_FILE_DIR=main.py
COPY ${SRC_FILE_DIR} main.py

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT python3 main.py