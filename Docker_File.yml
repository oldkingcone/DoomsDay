FROM ubuntu:latest
MAINTAINER Me
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential apache aespipe
RUN service apache2 start
RUN touch ~/super_duper_admin_database.sqlite
COPY ./app
WORKDIR /app
RUN pip install -r REQUIREMENTS
ENTRYPOINT ["python"]
CMD ["app.py"]
