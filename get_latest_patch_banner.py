from helpers import get_latest_version, split_version

import requests
from bs4 import BeautifulSoup

def main():
    version = get_latest_version()
    major_version, minor_version = split_version(version)
    patch_notes_url = f'https://www.leagueoflegends.com/en-us/news/game-updates/patch-{major_version}-{minor_version}-notes/'
    patch_notes_page = requests.get(patch_notes_url)
    print(f'status code: {patch_notes_page.status_code}')
    patch_notes_soup = BeautifulSoup(patch_notes_page.content, 'html.parser')
    banner = patch_notes_soup.find('img')
    banner_url = banner['src']

    filename = banner_url.split('/')[-1]
    r = requests.get(banner_url, allow_redirects=True)
    open('patch_banner.jpg', 'wb').write(r.content)


if __name__ == '__main__':

    main()