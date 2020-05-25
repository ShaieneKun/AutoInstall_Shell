#! /bin/bash

#Installing flatpak

if (( $(apt list --installed flatpak | grep -c flatpak) < 1 ))
then
   apt-get install -y flatpak 
fi

appList=$(cat ./flatpak-apps.txt) #Obtaining apps/packages list from txt file
echo "Pacotes a serem instalados $appList"

#Instalando 
for app in $appList
do
   flatpak install flathub $app
done
