# Post Malone

This is a simple challenge to make sure people know how to send a POST request. 

## Development Test

```
uvicorn postmalone:app --reload
```

## Start Docker Test

```
docker build . --tag hth22-web-post-malone
docker images

REPOSITORY              TAG                  IMAGE ID       CREATED         SIZE
hth22-web-post-malone   latest               f547215b00fc   3 minutes ago   127MB
python                  3.10.6-slim-buster   85d90b416bbd   2 months ago    119MB

docker run -p 7501:7501 hth22-web-post-malone
```

## Stop Docker Test

```
Ctrl-C
```

For more information about Python FastAPI, check out this great article: [https://realpython.com/fastapi-python-web-apis/](https://realpython.com/fastapi-python-web-apis/).
