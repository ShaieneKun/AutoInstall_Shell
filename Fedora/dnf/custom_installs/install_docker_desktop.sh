dnf -y install dnf-plugins-core

dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

wget https://desktop.docker.com/linux/main/amd64/165256/docker-desktop-x86_64.rpm

dnf install ./docker-desktop-x86_64.rpm
