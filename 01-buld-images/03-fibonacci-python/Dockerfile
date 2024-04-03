FROM ubuntu:20.04

WORKDIR /app

COPY /src /app

RUN apt-get update 

RUN apt-get install -y python3 python3-pip

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
