#! /bin/bash

#Installing flatpak
if (( $(apt list --installed flatpak | grep -c flatpak) < 1 ))
then
   apt-get install -y flatpak 
fi

#Adding FlatHub repositories
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo 

#Obtaining apps/packages list from txt file
appList=$(cat ./flatpak-apps.txt) 
echo "Pacotes a serem instalados $appList"

#Instalando 
for app in $appList
do
   flatpak install -y flathub $app
done
