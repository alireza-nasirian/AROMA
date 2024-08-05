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

## Counting number of successful builds
To count the number of successful builds, you have to run [successful_build_counter.py](pythonScripts/successful_build_counter.py).

This script count the number of unsuccessful builds from build logs.

## Counting number of ok and ko files
In each successful build, there are a number of "ok" files indicating the count of successfully rebuilt files within the package, and a number of "ko" files indicating files that were not successfully rebuilt.

To count the number of ok and ko files you have to run [ok_ko_counter.py](project/ok_ko_counter.py).

This script count the number of ok and ko files from build logs.

