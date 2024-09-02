#!/usr/bin/python3

import sys
import os
import subprocess as sp
import utils
from Fedora.dnf import dnf_installer


print("""
Starting script to setup a fresh Fedora install.
The script installs dnf and flatpak packages.
It also setups fonts and other gnome shell configurations
It runs custom scripts to install programs such as Docker Desktop and VS Code
""")

ls = os.listdir()

if (not ("Fedora" in ls and "fedora-autoinstall.py")):
    print("Execute the program in the same dir as it is stored")
    sys.exit(1)

fedora_scripts_path = "./Fedora/"

sp.run(f"chmod +x -R {fedora_scripts_path}".split())

# dnf installer
fedora_dnf_scripts_path = f"{fedora_scripts_path}dnf/"

dnf_apps: "list[str]" = utils.list_from_file(
    f"{fedora_dnf_scripts_path}dnf-apps.txt")
dnf_copr: "list[str]" = utils.list_from_file(
    f"{fedora_dnf_scripts_path}dnf-copr.txt")
dnf_apps_remove: "list[str]" = utils.list_from_file(
    f"{fedora_dnf_scripts_path}dnf-apps-remove.txt")

print('\nStarting the "dnf-installer.py" script...')

# dnf_installer.main(dnf_apps,
#                    dnf_copr,
#                    dnf_apps_remove)

print('\nFinished the "dnf-installer.py" script...')

print('\nStarting the custom dnf scripts...')

dnf_custom_scripts: list[str] = os.listdir(f"{fedora_dnf_scripts_path}custom_installs/")

for script in dnf_custom_scripts:
    print(f'\nStarting the custom dnf script: {script}')

    sp.run(f"{fedora_dnf_scripts_path}custom_installs/{script}")

    print(f'\nFinished the custom dnf script: {script}')

print('\nFinished the custom dnf scripts...')


# dnf custom installs
# flatpak installer
# flatpak extra-setups
# others
