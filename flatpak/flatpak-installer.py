#!/bin/python3
import subprocess

with open("flatpak-apps.txt", "r") as flatpak_apps_file:
    flatpak_apps: 'list[str]' = flatpak_apps_file.readlines()
    flatpak_apps = [ app.replace("\n", "") for app in flatpak_apps ]

if not flatpak_apps:
    print(f"Flatpaks a serem instalados: {flatpak_apps}")
    
    for app in flatpak_apps:
        subprocess.run(f"flatpak install -y flathub {app}".split())

subprocess.run("flatpak upgrade -y".split())