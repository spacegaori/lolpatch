from helpers import split_version, join_version, verify_patch_version

from typing import Final
import requests
from bs4 import BeautifulSoup

INITIAL_VERSION: Final = '9.1'

def get_latest_version():
    patch_list_url = f'https://www.leagueoflegends.com/en-us/news/tags/patch-notes/'
    patch_list_page = requests.get(patch_list_url)
    patch_list_soup = BeautifulSoup(patch_list_page.content, 'html.parser')

    patch_list = patch_list_soup.find_all('li')

    most_recent_patch = patch_list[0]
    title = most_recent_patch.find('h2').text
    version = title.split(' ')[1]
    
    return version

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
