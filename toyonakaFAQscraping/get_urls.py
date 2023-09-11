# using bs4 to extract faqid from html file

import os
import sys
import json
import requests
from bs4 import BeautifulSoup
import time

# get html file from ~/Downloads/toyonaka{id}.html and return it
def get_html(id):
    save_dir = '/Users/A14880/Downloads'
    file_name = f'toyonaka{id}.html'
    file_path = os.path.join(save_dir, file_name)
    with open(file_path, 'rb') as f:
        html = f.read()
    return html

# find all href
# and return the href that contains 'FAQID'
def extract_faqid(html):
    soup = BeautifulSoup(html, 'html.parser')
    hrefs = soup.find_all('a')
    faqids = []
    for href in hrefs:
        if 'FAQID' in href.get('href'):
            # get id from href
            faqid = href.get('href').split('=')[1]
            faqids.append(faqid)
    return faqids
        
# main function that first get html file from ~/Downloads/toyonaka{id}.html
# then extract faqid from the html file
if __name__ == '__main__':
    faqids_li = []
    for id in range(1,5):
        html = get_html(id)
        faqids = extract_faqid(html)
        faqids_li.extend(faqids)
    print(faqids_li)
