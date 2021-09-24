FROM python:3.7-slim-buster

WORKDIR /app
VOLUME /app

ADD requirements.txt
ADD .home/app

RUN pip install -r requirements.txt
EXPOSE 1000:1000

ENTRYPOINT python app.py 1000
CMD ["app.py"]

