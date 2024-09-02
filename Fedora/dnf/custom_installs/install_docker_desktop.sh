#!/bin/bash

sudo dnf install -y dnf-plugins-core wget

sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

FILE=docker-desktop-x86_64.rpm

if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist. Downloading..."
    wget "https://desktop.docker.com/linux/main/amd64/165256/$FILE"

fi

sudo dnf install -y ./$FILE
