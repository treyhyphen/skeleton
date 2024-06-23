#FROM ubuntu:latest
#ARG VARIANT="3.11-bullseye"
#FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}
FROM python:3.11-bullseye

# Switching to root to install required packages
USER root

# Example:  installing the MySQL driver to connect to the metadata database
# If you prefer Postgres, you may want to use `psycopg2-binary` instead
RUN apt update
RUN apt -y install build-essential libssl-dev libffi-dev python3-dev python3-pip libsasl2-dev libldap2-dev default-libmysqlclient-dev pkg-config

RUN useradd -ms /bin/bash superset
USER superset

# Pip install superset and switch back to superset user ...
RUN pip install virtualenv sqlalchemy-redshift mysqlclient
RUN pip install apache-superset

# Add superset_config.py
#RUN echo "SECRET_KEY = '$(cat /run/secrets/superset_secret_key)'" >> /home/superset/.superset/superset_config.py \
#    && echo "SQLALCHEMY_DATABASE_URI = 'sqlite:////home/superset/.superset/superset.db?check_same_thread=false'" >> /home/superset/.superset/superset_config.py

COPY run_superset.sh /tmp