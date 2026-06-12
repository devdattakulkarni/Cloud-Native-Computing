FROM ubuntu:22.04
RUN apt-get update -y \ 
    && apt-get install -y python3-setuptools python3-pip
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt
ADD . /src
EXPOSE 5001
ENV GREETING="Summer is here"
CMD ["python3", "/src/application.py"]
