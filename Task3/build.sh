#!/bin/bash

mkdir tempdir

#Create Dockerfile
echo "FROM debian" > tempdir/Dockerfile
echo "RUN apt-get update ; apt-get -y install apache2" >> tempdir/Dockerfile
echo "RUN a2enmod rewrite ; service apache2 restart" >> tempdir/Dockerfile
echo "RUN sed -i 's/^Listen 80/Listen 8081/g' /etc/apache2/ports.conf ; service apache2 restart" >> tempdir/Dockerfile
echo "RUN sed -i 's/^<VirtualHost \*:80>/<VirtualHost *:8081>/g' /etc/apache2/sites-available/000-default.conf ; service apache2 restart" >> tempdir/Dockerfile
echo "EXPOSE 8081" >> tempdir/Dockerfile

#Build Docker container
cd tempdir
docker build -t apacheinstall .
# Start container and verify
docker run -t -d -p 8080:8080 --name myinstance apacheinstall
docker ps -a
