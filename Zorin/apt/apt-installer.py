#!/bin/python3
import subprocess

import utils

apt_apps: "list[str]" = utils.list_from_file("apt-apps.txt")
apt_ppas: "list[str]" = utils.list_from_file("apt-ppas.txt")

def handle_ppas(ppas: 'list[str]'):
    print(f"\nNumber of ppas: {len(ppas)}")
    print(f"List of ppas: {ppas}\n")

    for ppa in ppas:
        subprocess.run(f"add-apt-repository -y {ppa}".split())
        
def handle_apt_apps(apt_apps: 'list[str]'):
    print(f"\nNumber of packages: {len(apt_apps)}")
    print(f"List of packages: {apt_apps}\n")

    subprocess.run(f"apt list".split() + [*apt_apps])

    print("Installing apps...")
    
    subprocess.run("apt install -y".split() + [*apt_apps])

subprocess.run("apt update".split())

if apt_ppas:
    handle_ppas(apt_ppas)

if apt_apps:
    handle_apt_apps(apt_apps)
    
subprocess.run("apt upgrade -y".split())
subprocess.run("apt auto-remove -y".split())