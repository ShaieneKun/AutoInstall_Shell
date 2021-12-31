#! /bin/bash
x=10
sudo apt-add-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.$x python3.$x-dev python3.$x-venv python3.$x-distutils
python3.$x -m ensurepip
