#!/bin/bash

# show all commands
set -x

sudo apt update
sudo apt -y install default-mysql-client vim

pip install -r requirements.txt