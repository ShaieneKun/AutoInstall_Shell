import subprocess

with open("snap-apps.txt", "r") as snap_apps_file:
    snap_apps: 'list[str]' = snap_apps_file.readlines()

if not snap_apps:
    print(f"snaps a serem instalados: {snap_apps}")
    
    for app in snap_apps:
        subprocess.run(["snap","install", app])

subprocess.run(["snap", "refresh"])