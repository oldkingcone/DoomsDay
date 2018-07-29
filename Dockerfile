FROM ubuntu:latest
MAINTAINER oldkingcone(Iamroot)
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential apache aespipe
RUN service apache2 start
COPY ./app
WORKDIR /app
RUN pip install -r REQUIREMENTS
ENTRYPOINT ["python"]
CMD ["DoomsDayMain.py"]
