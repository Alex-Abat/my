sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/ask.py  /etc/gunicorn.d/ask.py
sudo ln -sf /home/box/web/etc/hello.conf  /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
