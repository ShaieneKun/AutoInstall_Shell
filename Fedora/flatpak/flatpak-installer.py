#!/bin/python3
import subprocess
import sys
# Shell commands

# sys.exit()

install_location: str = "system"  # TODO add option to pass "system" as argument
add_flathub_remote = f"sudo flatpak remote-add --{install_location} --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo"


with open("flatpak-apps.txt", "r") as flatpak_apps_file:
    flatpak_apps: list[str] = flatpak_apps_file.readlines()
    flatpak_apps: list[str] = [app.replace("\n", "") for app in flatpak_apps]

if flatpak_apps:
    print(f"Flatpaks to install: {flatpak_apps}")

    subprocess.run(add_flathub_remote.split())

    for app in flatpak_apps:
        subprocess.run(f"sudo flatpak install --{install_location} -y flathub {app}".split())

subprocess.run("flatpak upgrade -y".split())
