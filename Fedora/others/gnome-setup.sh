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
