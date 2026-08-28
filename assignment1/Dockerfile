FROM ubuntu:20.04 
RUN apt-get update -y \ 
    && apt-get install -y python-setuptools
RUN apt-get install -y python3-pip
RUN apt-get install -y curl
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt
ADD . /src
EXPOSE 5000 							

# Add environment variable GREETING with value "Summer is here!"
CMD ["python3", "/src/application.py"]
