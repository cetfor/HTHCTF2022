FROM python:3.10.6-slim-buster
RUN apt update
RUN apt -y install socat
WORKDIR /app
COPY src/beepbeep.py /app/beepbeep.py
COPY src/flag /app/flag
ENTRYPOINT socat TCP4-listen:7803,reuseaddr,fork,su=nobody EXEC:"python -u /app/beepbeep.py"
