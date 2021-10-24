#!/bin/python3
import subprocess

with open("apt-apps.txt", "r") as apt_apps_file:
    apt_apps: 'list[str]' = apt_apps_file.readlines()

with open("apt-ppas.txt", "r") as apt_ppas_file:
    apt_ppas: 'list[str]' = apt_ppas_file.readlines()

def handle_ppas(ppas: 'list[str]'):
    print(f"\nNumber of ppas: {len(apt_apps)}")
    print(f"\nList of packages: {apt_apps}")

    for ppa in ppas:
        ppa = ppa.replace("'", "")
        subprocess.run(["add-apt-repository", "-y", ppa])
        
def handle_apt_apps(apt_apps: 'list[str]'):
    print(f"\nNumber of packages: {len(apt_apps)}")
    print(f"\nList of packages: {apt_apps}")

    subprocess.run(["apt", "list", *apt_apps])

    print("Installing apps...")
    apt_apps = [app.replace("'", "") for app in apt_apps]
    
    subprocess.run(["apt", "install", "-y", *apt_apps])

subprocess.run(["apt", "update"])

if apt_ppas:
    handle_ppas(apt_ppas)

if apt_apps:
    handle_ppas(apt_apps)
    
subprocess.run(["apt", "upgrade", "-y"])