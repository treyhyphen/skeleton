#!/bin/bash

mysql -u root --password=$(cat /run/secrets/db_root_password) -h db < /workspaces/flask-mysql-zappa-lambda/sql/skeleton.sql

export SQLALCHEMY_DATABASE_URI="mysql://root:$(cat /run/secrets/db_root_password)@db:3306/skeleton"
echo 'export SQLALCHEMY_DATABASE_URI="mysql://root:$(cat /run/secrets/db_root_password)@db:3306/skeleton"' >> /home/vscode/.bashrc

sudo service nginx restart
flask run 