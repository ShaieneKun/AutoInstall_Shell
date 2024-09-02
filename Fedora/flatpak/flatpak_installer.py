#!/bin/python3
import subprocess
import utils


def main(flatpak_apps: list[str]):
    INSTALL_LOCATION: str = "system"  # TODO add option to pass "system" as argument
    FLATHUB_URL = "https://flathub.org/repo/flathub.flatpakrepo"

    add_flathub_remote = f"sudo flatpak remote-add --{
        INSTALL_LOCATION} --if-not-exists flathub {FLATHUB_URL}"

    subprocess.run("sudo dnf install -y flatpak".split())
    subprocess.run(add_flathub_remote.split())

    if flatpak_apps:
        print(f"Flatpak apps to install: {flatpak_apps}")

        for app in flatpak_apps:
            subprocess.run(
                f"sudo flatpak install --{INSTALL_LOCATION} -y flathub {app}".split())

    subprocess.run("sudo flatpak upgrade -y".split())


if __name__ == "__main__":
    flatpak_apps: "list[str]" = utils.list_from_file("flatpak-apps.txt")

    main(flatpak_apps)
