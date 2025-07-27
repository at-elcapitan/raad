import os
import sys
import subprocess

CONFIG_PATH = os.path.expanduser("~/.raad_config")


def load_admin():
    if not os.path.exists(CONFIG_PATH):
        return None

    with open(CONFIG_PATH, "r") as f:
        return f.read().strip()


def save_admin(admin_name):
    with open(CONFIG_PATH, "w") as f:
        f.write(admin_name.strip())


def ask_admin():
    admin = input("Enter the username to run commands as: ").strip()

    if admin:
        save_admin(admin)
        return admin
    
    print("Username cannot be empty.")
    sys.exit(1)


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: raad <command> [args] or raad --change <new_user>")
        sys.exit(1)

    if args[0] == "--change":
        if len(args) < 2:
            print("Please provide a username after --change")
            sys.exit(1)
        new_admin = args[1]
        save_admin(new_admin)
        print(f"Admin username updated: {new_admin}")
        sys.exit(0)

    admin = load_admin()
    if not admin:
        admin = ask_admin()

    cmd = ["sudo", "-u", admin, "sudo"] + args

    try:
        subprocess.run(cmd)
    except Exception as e:
        print(f"Error while executing command: {e}")
        sys.exit(1)
