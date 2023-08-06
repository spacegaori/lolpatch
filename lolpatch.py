from helpers import split_version, join_version, verify_patch_version
from update_patch_versions import update_patch_version, get_latest_version

import argparse
from bs4 import BeautifulSoup
import re
import sys


def main(version, language):
    versions = update_patch_version()
    print(versions)
    
    # print(version)
    # major_version, minor_version = split_version(version)
    # patch_notes_url = f'https://www.leagueoflegends.com/{language}/news/game-updates/patch-{version[:2]}-{version[3:]}-notes/'
    # patch_notes_page = requests.get(patch_notes_url)
    # print(f'status code: {patch_notes_page.status_code}')
    # patch_notes_soup = BeautifulSoup(patch_notes_page.content, 'html.parser')

    # title = f'PATCH {version} NOTES'
    # datetime = patch_notes_soup.find('time')['datetime']
    # date = datetime[:10]
    # print(title, date)
    # if ((int(major_version) == 13 and int(minor_version) >= 14) or int(major_version) >= 14):
    #     midpatch_updates = patch_notes_soup.find('h2', id = 'patch-mid-patch-updates')
    # else:
    #     midpatch_updates = patch_notes_soup.find('h2', id='patch-midpatch-updates')
    # if midpatch_updates != None:
    #     print(midpatch_updates.text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('version', nargs='?', default=get_latest_version())
    parser.add_argument('language', nargs='?', default='en-us')
    args = parser.parse_args()

    main(args.version, args.language)