FROM python:3.10.6-slim-buster
RUN apt update
RUN apt -y install socat
WORKDIR /app
COPY src/ /app/src/
WORKDIR /
ENTRYPOINT socat -T0 -t0 TCP4-listen:7602,tcpwrap=script,reuseaddr,fork,su=nobody EXEC:"python -u /app/src/challenge.py </dev/null >/dev/null 2>&1"
