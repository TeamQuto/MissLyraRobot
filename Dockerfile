FROM debian:11
FROM python-3.10.4-slim-buster

WORKDIR /MissLyraRobot/

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install git
RUN python-3.10.4 -m pip install --upgrade pip
RUN apt-get install -y wget python3-pip curl bash neofetch ffmpeg software-properties-common

COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt

COPY . .
CMD ["python-3.10.4", "-m", "MissLyraRobot"]
