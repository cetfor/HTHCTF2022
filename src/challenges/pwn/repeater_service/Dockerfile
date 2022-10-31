FROM ubuntu:jammy
RUN apt update
RUN apt -y install socat
WORKDIR /app
COPY repeat /app/repeat
RUN chmod +x /app/repeat
ENTRYPOINT socat TCP4-listen:7801,reuseaddr,fork,su=nobody EXEC:"./repeat",pty,echo=0
