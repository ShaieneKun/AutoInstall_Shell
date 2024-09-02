#!/bin/bash

sudo dnf install -y dnf-plugins-core wget

sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

wget https://desktop.docker.com/linux/main/amd64/165256/docker-desktop-x86_64.rpm

sudo dnf install -y ./docker-desktop-x86_64.rpm
