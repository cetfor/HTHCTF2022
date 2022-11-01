FROM kalilinux/kali-rolling
RUN apt update 
RUN apt -y install kali-linux-headless
RUN apt -y install socat
RUN apt -y install python3
RUN apt -y install python-pip3
RUN pip install python-shell
WORKDIR /app
COPY kali101.py /app/kali101.py
ENTRYPOINT socat TCP4-listen:7901,reuseaddr,fork,su=nobody EXEC:"python -u /app/kali101.py"
