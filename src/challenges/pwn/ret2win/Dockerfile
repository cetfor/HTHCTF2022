FROM ubuntu:jammy
RUN apt update
RUN apt -y install socat
WORKDIR /app
COPY flag.txt /app/flag.txt
COPY ret2win /app/ret2win
RUN chmod +x /app/ret2win
ENTRYPOINT socat TCP4-listen:7802,reuseaddr,fork,su=nobody EXEC:"./ret2win",pty,echo=0
