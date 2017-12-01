# Version check

The idea behind this script to make sure releases are properly versioned through the 
use of GIT tags and a file in the software that contain the current version.

## Usage

```bash
versioncheck -h
usage: versioncheck [-h] project-type git-tag

Check the defined version on the project depending on the project type.

positional arguments:
  project-type  Project type. Accepted values are: python, c
  git-tag       Git tag that specify the version

optional arguments:
  -h, --help    show this help message and exit
```

## Installation
```bash
git clone https://github.com/adriangalera/versioncheck.git
sudo ln -s /home/ubuntu/versioncheck/versioncheck/versioncheck.py /usr/bin/versioncheck
chmod +x /usr/bin/versioncheck
```