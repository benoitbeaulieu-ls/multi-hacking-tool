#!/usr/bin/env python3
import subprocess
import apt

cache = apt.Cache()
package_name = cache[y]

dependant_packages = [
    'nmap',
    'hydra'
]


for y in dependant_packages:

   
    print(package_name)

