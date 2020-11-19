#!/usr/bin/env python3
import subprocess
import sys
import apt

#packages we need
dependant_packages = [
    'nmap',
    'hydra',
    'git',
    'john',
    'gobuster',

]

all_packages = []

#Let's try to run through

cache = apt.Cache()



for package in apt.Cache():
    all_packages.append(package)
    

print(all_packages)