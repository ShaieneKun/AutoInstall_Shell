#!/bin/python3
import subprocess

with open("flatpak-apps.txt", "r") as flatpak_apps_file:
    flatpak_apps: 'list[str]' = flatpak_apps_file.readlines()

if not flatpak_apps:
    print(f"Flatpaks a serem instalados: {flatpak_apps}")
    
    for app in flatpak_apps:
        subprocess.run(["flatpak", "install", "-y", "flathub", app])

subprocess.run(["flatpak", "upgrade", "-y"])