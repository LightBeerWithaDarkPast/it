FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && apt-get -y install mc git python3 pip snapd

RUN apt install firefox

RUN pip install numpy pandas

COPY . .

ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
