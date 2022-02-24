FROM python:3.8
WORKDIR /usr/src/app
RUN pip3 install Flask
COPY . .
ENTRYPOINT python3 api-test.py