FROM python:3.10.6-slim-buster
RUN python -m pip install fastapi uvicorn[standard] --no-cache-dir
WORKDIR /app
COPY postmalone.py flag.txt ./
CMD [ "uvicorn", "postmalone:app", "--reload", "--host", "0.0.0.0", "--port", "7501" ]
