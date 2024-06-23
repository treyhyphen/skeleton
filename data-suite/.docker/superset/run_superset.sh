#!/bin/bash

set -x

export PATH="$PATH:/home/superset/.local/bin"
export FLASK_RUN_HOST="0.0.0.0"

# If superset_config.py doesn't exist this is probably our first run so we need to init everything
if [ ! -f /home/superset/.superset/superset_config.py ]; then

    # Add necessary config options
    echo "SECRET_KEY = '$(cat /run/secrets/superset_secret_key)'" >> /home/superset/.superset/superset_config.py
    echo "SQLALCHEMY_DATABASE_URI = 'sqlite:////home/superset/.superset/superset.db?check_same_thread=false'" >> /home/superset/.superset/superset_config.py

    # Init the database
    superset db upgrade

    # Create an admin user
    superset fab create-admin \
        --username $(cat /run/secrets/superset_admin_user) \
        --firstname Superset \
        --lastname Admin \
        --email foo@bar.com\
        --password $(cat /run/secrets/superset_admin_pass)

    superset init
fi

superset run --with-threads --reload 