import requests
from bs4 import BeautifulSoup

def split_version(version):
    split = version.split('.')
    major_version = int(split[0])
    minor_version = int(split[1])

    return major_version, minor_version

def join_version(major_version, minor_version):
    return f'{major_version}.{minor_version}'

def verify_patch_version(version):
    major_version, minor_version = split_version(version)
    if (major_version == 13 and minor_version == 2):
        minor_version = '1b'
    patch_url = f'https://www.leagueoflegends.com/en-us/news/game-updates/patch-{major_version}-{minor_version}-notes/'
    patch_url_status = requests.head(patch_url).status_code
    # print(major_version, minor_version, patch_url_status, patch_url)

    return patch_url_status

def get_latest_version():
    patch_list_url = f'https://www.leagueoflegends.com/en-us/news/tags/patch-notes/'
    patch_list_page = requests.get(patch_list_url)
    patch_list_soup = BeautifulSoup(patch_list_page.content, 'html.parser')

    patch_list = patch_list_soup.find_all('li')

    most_recent_patch = patch_list[0]
    title = most_recent_patch.find('h2').text
    version = title.split(' ')[1]
    
    return version