ARG VARIANT="3.11-bullseye"
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

# Persist bash history
ARG USERNAME="vscode"
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && mkdir /commandhistory \
    && touch /commandhistory/.bash_history \
    && chown -R $USERNAME /commandhistory \
    && echo "$SNIPPET" >> "/home/$USERNAME/.bashrc"

# Install extra packages
RUN sudo apt update
RUN sudo apt install -y vim