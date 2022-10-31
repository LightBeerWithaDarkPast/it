FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && apt-get -y install mc git python3 pip

RUN pip install numpy pandas

COPY . .

VOLUME [ "/task3/iris" ]

ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
