FROM ubuntu:jammy
RUN apt update
RUN apt -y install socat
WORKDIR /app
COPY bussin /app/bussin
RUN chmod +x /app/bussin
#ENTRYPOINT /bin/bash
ENTRYPOINT socat -T0 -t0 TCP4-listen:7701,tcpwrap=script,reuseaddr,fork EXEC:"./bussin"
