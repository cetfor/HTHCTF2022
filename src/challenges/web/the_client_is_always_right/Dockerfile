FROM python:3.10.6-slim-buster
RUN python -m pip install Flask
WORKDIR /app
COPY templates/ /app/templates/
COPY static/ /app/static/
COPY app.py .
CMD ["python", "app.py"]
