from helpers import split_version, join_version, verify_patch_version

from typing import Final
import requests
from bs4 import BeautifulSoup
import csv

INITIAL_VERSION: Final = '9.1'


def update_patch_version():
    versions = []
    major_version, minor_version = split_version(INITIAL_VERSION)
    while(verify_patch_version(join_version(major_version, minor_version)) == 200):
        if (minor_version == 1):
            versions.append((join_version(major_version, minor_version)))
            minor_version += 1
        while(verify_patch_version(join_version(major_version, minor_version)) == 200):
            if (major_version == 13 and minor_version == 2):
                versions.append((join_version(major_version, '1b')))
                minor_version = 3
            else:
                versions.append((join_version(major_version, minor_version)))
                minor_version += 1
        major_version += 1
        minor_version = 1

    return versions

def main(): 
    versions = update_patch_version()

    with open('patch_versions.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(versions)

if __name__ == '__main__':
    main()