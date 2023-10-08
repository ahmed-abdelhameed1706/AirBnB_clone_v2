#!/usr/bin/env bash
# script to set up the web servers

sudo apt update -y
sudo apt install nginx -y

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "This is a simple HTML file" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

sudo sed -i '78i\    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }' /etc/nginx/sites-available/default

sudo service nginx restart
