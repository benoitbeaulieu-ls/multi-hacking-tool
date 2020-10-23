#!/usr/bin/env python3
import subprocess
import apt

cache = apt.Cache()

nmap_package = "nmap"


dependant_packages = [
    'nmap',
    'hydra',
    'git',
    'john',
    'gobuster',


]


for package in dependant_packages:

    package_name = cache[package]

if nmap_package in package:
    print('yes the package is here')

else:
    print("nmap is not in")

