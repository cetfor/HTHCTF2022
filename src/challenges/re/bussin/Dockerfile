FROM ubuntu:jammy
RUN apt update
RUN apt -y install socat
WORKDIR /app
COPY bussin /app/bussin
RUN chmod +x /app/bussin
ENTRYPOINT socat TCP4-listen:7701,reuseaddr,fork,su=nobody EXEC:"./bussin",pty,echo=0
