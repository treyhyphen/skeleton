ARG VARIANT="3.11-bullseye"
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

# Persist bash history
ARG USERNAME=vscode
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && mkdir /commandhistory \
    && touch /commandhistory/.bash_history \
    && chown -R $USERNAME /commandhistory \
    && echo "$SNIPPET" >> "/home/$USERNAME/.bashrc"

# Install extra packages
RUN apt update
RUN apt install -y vim

# Install requirements
COPY ../requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt