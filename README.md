# Places_remember

## Project description

A Django web application that allows people to store their impressions of places they've visited. 

## Run project 

Before starting the container build, use the following command

`chmod 0777 placesremember/`

Also add to `/etc/hosts`

`127.0.0.1       placesremember.com      www.placesremember.com`

To run a project via Docker, use the following commands:

`docker build -t places_remember_docker .`

`docker-compose up`

Go to the `www.placesremember.com` and you will see the application running