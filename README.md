# AROMA
This repository contains the code and steps to reproduce the results presented in Section 5.1 of the paper "AROMA: Automatic Reproduction of Maven Artifacts."

## Prerequisites:
* [Docker](https://www.docker.com) or [Podman](https://podman.io)
* `dos2unix` - DOS to MAC/UNIX text file format converter. \
   Can be installed via [homebrew](https://brew.sh) on MAC via: `brew install dos2unix`.

# Steps to Rebuild Packages

## 1. Clone the RC Repository
To clone the repository, use the following command:

```sh
git clone https://github.com/jvm-repo-rebuild/reproducible-central.git
```
## 2. Select Random Packages to Rebuild
To select random package from RC repository, run [select_packages.py](pythonScripts/select_packages.py).
make sure to replace content param with the RC repo path.

This script will generate a .txt file containing paths of random .buildspec files.

## 3. Rebuild Packages
To rebuild packages, run [run_rebuilds.py](pythonScripts/run_rebuilds.py). This scripts will read paths from paths.txt that previous script generated and run [rebuild.sh](shellScripts/rebuild.sh) script on each package and will write rebuild log of each package into a separate .txt file in output_logs directory.

