# django-dot-pkce-example
Django project example using django-oauth-toolkit to perform OAuth Authorization Code flow with PKCE

## Prerequisites
You must have `docker` installed on your machine.

## Build and run
```
# Build the image
docker build -t "pkce-example" .

# Run manage.py to perform migrations
docker run -v $(pwd)/pixie:/usr/src/app pkce-example ./manage.py migrate

# Run manage.py to run the server
docker run -p"8000:8000" -v $(pwd)/pixie:/usr/src/app pkce-example
```

## Setup for the dev
A superuser is automatically created in the migrations for convenience : `user=admin, password=admin`