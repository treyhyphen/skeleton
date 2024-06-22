ARG VARIANT="3.11-bullseye"
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

RUN apt update
RUN apt install -y vim

COPY ../requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt