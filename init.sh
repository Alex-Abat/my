sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/gunicorn_django.conf  /etc/gunicorn.d/gunicorn_django.conf 
sudo ln -sf /home/box/web/etc/gunicorn_hello.conf  /etc/gunicorn.d/gunicorn_hello.conf
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
mysql -uroot -e "create database ask"
