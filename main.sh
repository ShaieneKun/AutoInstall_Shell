#! /bin/bash

#File/folder vars | Should the directory structure change, the script will keep on working (Probably)

mainPath=$(pwd) #This file's directory

#Installer using apt-get
aptAppsFolder=$(find ./ -type d -name apt-get) 
aptAppsInstaller="apt-installer.sh"
#Installing from distro repositories (apt-get)

cd $aptAppsFolder
chmod o+x $aptAppsInstaller
./$aptAppsInstaller
cd "$mainPath" 

#Installer using flatpak
flatpakAppsFolder=$(find ./ -type d -name flatpak) 
flatpakAppsInstaller="flatpak-installer.sh"
#Installing from distro repositories (apt-get)

cd $flatpakAppsFolder
chmod o+x $flatpakAppsInstaller
./$flatpakAppsInstaller
cd "$mainPath" 
