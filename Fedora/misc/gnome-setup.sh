#!/bin/bash

# gtk3 dark theme
gsettings set org.gnome.desktop.interface gtk-theme 'adw-gtk3-dark' && gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'

# Fonts and Scaling

sudo fc-cache -f -v

gsettings set org.gnome.desktop.interface font-name 'Inter 15'
gsettings set org.gnome.desktop.interface document-font-name 'Inter 15'
gsettings set org.gnome.desktop.interface monospace-font-name 'JetBrains Mono 10'

gsettings set org.gnome.desktop.interface font-hinting full

gsettings set org.gnome.desktop.interface font-antialiasing rgba

gsettings set org.gnome.desktop.interface text-scaling-factor 1.25

sudo fc-cache -f -v

# Other UI Elements
gsettings set org.gnome.desktop.interface enable-hot-corners true

# Cursor
FILE=main.zip

if [ ! -f "$FILE" ]; then
    echo "$FILE was not found. Downloading..."
    wget "https://github.com/vinceliuice/Graphite-cursors/archive/refs/heads/$FILE"
fi

echo "A" | unzip -q $FILE
cd ./Graphite-cursors-main

chmod +x ./install.sh
echo "1" | ./install.sh

cd ..

gsettings set org.gnome.desktop.interface cursor-theme "Graphite-dark-cursors"

# extensions

sudo dnf install -y python3-pip
pip3 install --upgrade gnome-extensions-cli

gext install blur-my-shell@aunetx
gext install gsconnect@andyholmes.github.io
gext install trayIconsReloaded@selfmade.pl
gext install dash-to-dock@micxgx.gmail.com
gext install quicksettings-audio-devices-hider@marcinjahn.com
gext install openbar@neuromorph
gext install CoverflowAltTab@palatis.blogspot.com
gext enable pop-shell
