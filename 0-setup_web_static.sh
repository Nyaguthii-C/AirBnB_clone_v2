#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

#install nginx
sudo apt-get -y update
sudo apt-get install nginx
sudo service nginx start

#sudo mkdir -p /data/
#sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
#mkdir -p data/web_static/releases/test/
#sudo touch data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body> 
    Welcome to The Kenyan Astro page
  </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html

# create a symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group 
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

# Update the Nginx configuration
# to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static {\nalias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart Nginx after updating the configuration
sudo service nginx restart

exit 0
