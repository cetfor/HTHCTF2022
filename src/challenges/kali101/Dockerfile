FROM kalilinux/kali-rolling
RUN apt -y update 
RUN apt -y install man
RUN apt -y install python3-pip
RUN pip3 install python-shell
RUN apt -y install file
RUN apt -y install ncat
RUN apt -y install socat
RUN apt -y install ssh
WORKDIR /app
COPY kali101.py /app/kali101.py
COPY levels.json /app/levels.json
COPY sandbox /app/sandbox
#ENTRYPOINT /bin/bash
ENTRYPOINT socat TCP4-listen:7901,reuseaddr,fork,su=nobody EXEC:"python3 -u kali101.py"
