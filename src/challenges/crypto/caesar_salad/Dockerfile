FROM python:3.10.6-slim-buster
RUN apt update
RUN apt -y install socat
WORKDIR /app
COPY src/ /app/src/
ENTRYPOINT socat TCP4-listen:7601,reuseaddr,fork,su=nobody EXEC:"python -u /app/src/challenge.py"
