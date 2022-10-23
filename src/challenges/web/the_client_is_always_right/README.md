# Secure Cookies

description here...

## Development Test

```
python3 app.py
```

## Start Docker Test

```
docker build . --tag hth22-web-the-client-is-always-right
docker images

REPOSITORY                             TAG                  IMAGE ID       CREATED          SIZE
hth22-web-the-client-is-always-right   latest               710bf33b0065   4 seconds ago    127MB
python                                 3.9.2-slim-buster    972ef8de24a4   19 months ago    114MB

docker run -p 7502:7502 hth22-web-the-client-is-always-right
```

## Stop Docker Test

```
Ctrl-C
```
