# raad

**raad** (Run As ADmin) is a simple Python CLI tool that uses a double `sudo` call for layered privilege switching to allow you to execute commands as another sudo-enabled user. Can be useful for FreeIPA domain workstations.

## Requirements

- Python 3.6+
- `sudo` installed

## Installation

### From source

```bash
git clone https://github.com/at-elcapitan/raad.git
cd raad
pip install .
```

### Arch Linux (via PKGBUILD)

```bash
git clone https://github.com/at-elcapitan/raad.git
cd raad
makepkg -si
```

## Usage

Once installed, you can use `raad` like this:

### Run a command as another sudo-enabled user:

```bash
raad systemctl restart sshd
```

This wraps:

```bash
sudo -u <stored_username> sudo systemctl restart sshd
```

### Set or change the target admin:

```bash
raad --change aduser
```
