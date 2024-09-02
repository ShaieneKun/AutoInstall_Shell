#!/usr/bin/python3
import subprocess
import utils

def dnf_installer_test():
    print("success")


def handle_copr(copr_repos: 'list[str]'):
    print("\nAdding Copr repos...")
    print(f"\nNumber of copr repos: {len(copr_repos)}")
    print(f"List of copr repos: {copr_repos}\n")

    for copr_repo in copr_repos:
        subprocess.run(f"sudo dnf copr enable -y {copr_repo}".split())


def handle_dnf_apps(dnf_apps: 'list[str]'):
    print("\nInstalling dnf packages...:")
    print(f"\nNumber of packages: {len(dnf_apps)}")
    print(f"List of packages: {dnf_apps}\n")

    # subprocess.run(f"dnf list".split() + [*dnf_apps])

    print("Installing apps...")

    subprocess.run("sudo dnf install -y".split() + [*dnf_apps])


def handle_dnf_apps_remove(dnf_apps_to_remove: 'list[str]'):
    print("\nRemoving Apps:")
    print(f"\nNumber of packages: {len(dnf_apps_to_remove)}")
    print(f"List of packages: {dnf_apps_to_remove}\n")

    # subprocess.run(f"dnf list".split() + [*dnf_apps_to_remove])

    subprocess.run("sudo dnf remove -y".split() + [*dnf_apps_to_remove])


def main(
    dnf_apps: "list[str]",
    dnf_copr: "list[str]",
    dnf_apps_remove: "list[str]",
):
    subprocess.run("dnf update".split())

    if dnf_copr:
        handle_copr(dnf_copr)

    if dnf_apps:
        handle_dnf_apps(dnf_apps)

    if dnf_apps_remove:
        handle_dnf_apps_remove(dnf_apps_remove)

    subprocess.run("sudo dnf upgrade -y".split())
    subprocess.run("sudo dnf autoremove -y".split())


if __name__ == "__main__":
    dnf_apps: "list[str]" = utils.list_from_file("dnf-apps.txt")
    dnf_copr: "list[str]" = utils.list_from_file("dnf-copr.txt")
    dnf_apps_remove: "list[str]" = utils.list_from_file("dnf-apps-remove.txt")

    main(dnf_apps,
         dnf_copr,
         dnf_apps_remove)
