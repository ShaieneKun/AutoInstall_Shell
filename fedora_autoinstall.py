#!/usr/bin/python3

import sys, os, subprocess as sp
import utils
from Fedora.dnf import dnf_installer


print("""
Starting script to setup a fresh Fedora install.
The script installs dnf and flatpak packages.
It also setups fonts and other gnome shell configurations
It runs custom scripts to install programs such as Docker Desktop and VS Code
""")

ls = os.listdir()

if (not ("Fedora" in  ls and "fedora-autoinstall.py")):
    print("Execute the program in the same dir as it is stored")
    sys.exit(1)

fedora_scripts_path = "./Fedora/"
sp.run(f"chmod +x -R {fedora_scripts_path}".split())

# dnf installer

dnf_apps: "list[str]" = utils.list_from_file(f"{fedora_scripts_path}dnf/dnf-apps.txt")
dnf_copr: "list[str]" = utils.list_from_file(f"{fedora_scripts_path}dnf/dnf-copr.txt")
dnf_apps_remove: "list[str]" = utils.list_from_file(f"{fedora_scripts_path}dnf/dnf-apps-remove.txt")

print('\nRunning the "dnf-installer.py" script...')

dnf_installer.dnf_installer_test()

# sp.run(f"{fedora_scripts_path}dnf/dnf-installer.py".split())

print('\nFinished the "dnf-installer.py" script...')


# dnf custom installs
# flatpak installer
# flatpak extra-setups
# others
