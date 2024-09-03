#!/usr/bin/python3

import sys
import os
import subprocess as sp
import time
import utils
from Fedora.dnf import dnf_installer
from Fedora.flatpak import flatpak_installer

FEDORA_SCRIPTS_PATH = "./Fedora/"
fedora_dnf_scripts_path = f"{FEDORA_SCRIPTS_PATH}dnf/"
fedora_flatpak_scripts_path = f"{FEDORA_SCRIPTS_PATH}flatpak/"


def run_dnf_installer():
    dnf_apps: "list[str]" = utils.list_from_file(
        f"{fedora_dnf_scripts_path}dnf-apps.txt")
    dnf_copr: "list[str]" = utils.list_from_file(
        f"{fedora_dnf_scripts_path}dnf-copr.txt")
    dnf_apps_remove: "list[str]" = utils.list_from_file(
        f"{fedora_dnf_scripts_path}dnf-apps-remove.txt")

    print('\nStarting the "dnf-installer.py" script...')
    dnf_installer.main(dnf_apps,
                       dnf_copr,
                       dnf_apps_remove)
    print('\nFinished the "dnf-installer.py" script...')


def dnf_custom_installs():
    print('\nStarting the custom dnf scripts...')

    dnf_custom_scripts: list[str] = os.listdir(
        f"{fedora_dnf_scripts_path}custom_installs/")

    for script in dnf_custom_scripts:
        print(f'\nStarting the custom dnf script: {script}')
        sp.run(f"{fedora_dnf_scripts_path}custom_installs/{script}")
        print(f'\nFinished the custom dnf script: {script}')


def run_flatpak_installer():
    flatpak_apps: "list[str]" = utils.list_from_file(
        f"{fedora_flatpak_scripts_path}flatpak-apps.txt")

    print('\nStarting the "flatpak_installer.py" script...')
    flatpak_installer.main(flatpak_apps)
    print('\nFinished the "flatpak_installer.py" script...')


def flatpak_extra_setups():
    print('\nStarting the extra_setups.sh flatpak script...')
    sp.run(f"{fedora_flatpak_scripts_path}extra_setups.sh".split())
    print('\nFinished the extra_setups.sh flatpak script...')


def misc_scripts():
    print('\nStarting the misc scripts...')

    misc_scripts: list[str] = os.listdir(
        f"{FEDORA_SCRIPTS_PATH}misc/")

    for script in misc_scripts:
        print(f'\nStarting the misc script: {script}')

        sp.run(f"{FEDORA_SCRIPTS_PATH}misc/{script}")

        print(f'\nFinished the misc script: {script}')


def main():
    print("""
Starting script to setup a fresh Fedora install.
The script installs dnf and flatpak packages.
It also setups fonts and other gnome shell configurations
It runs custom scripts to install programs such as Docker Desktop and VS Code
""")

    time.sleep(6)
    ls = os.listdir()

    if (not ("Fedora" in ls and "fedora-autoinstall.py")):
        print("Execute the program in the same dir as it is stored")
        sys.exit(1)
    sp.run(f"chmod +x -R {FEDORA_SCRIPTS_PATH}".split())

    sp.run('sudo echo Root Access granted'.split())

    run_dnf_installer()
    dnf_custom_installs()

    run_flatpak_installer()
    flatpak_extra_setups()

    misc_scripts()

    print('\nFinished the fedora autoinstall script!')


if __name__ == "__main__":
    main()
