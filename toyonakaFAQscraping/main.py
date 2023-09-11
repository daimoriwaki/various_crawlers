import os
import sys
import json
import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

# get html file from url with requests
def get_html(url):
    headers_dic = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
    r = requests.get(url, headers=headers_dic)
    return r.content

# rename html file
def rename_html(id, html):
    save_dir = '/Users/A14880/dev/sandbox/toyonakaFAQscraping/docs'
    file_name = f'toyonaka_{id}.html'
    file_path = os.path.join(save_dir, file_name)
    with open(file_path, 'wb') as f:
        f.write(html)

# generate metadata
def generate_metadata(id, url):
    metadata = {}
    id = "toyonaka_" + id
    metadata[id] = {}
    metadata[id]['title'] = 'よくある質問'
    metadata[id]['reiwa'] = 5
    metadata[id]['url'] = url
    metadata[id]['source'] = f'data/docs/{id}.html'
    metadata[id]['load'] = True
    return metadata

if __name__ == '__main__':
    metadata = {}
    for id in tqdm(['1202004', '1202005', '1202003', '1202006', '1202001', '1202040', '1202002', '1202041', '1202012', '1202014', '1202017', '1202010', '4000127', '4000128', '1202008', '1202061', '1202059', '1202058', '1202009', '1202043', '1202019', '1202052', '1202065', '1202056', '1202011', '1202053', '1202054', '1202062', '1202013', '1202067', '1202016', '1202020', '1202063', '1202060', '1202037', '1202018', '1202042', '1202050', '1202047', '1202066']):
        url = f"https://toyofaq.city.toyonaka.osaka.jp/FAQ_P/P200.aspx?FAQID={id}"
        text = get_html(url)
        rename_html(id, text)
        metadata.update(generate_metadata(id, url))
    print(metadata)
    # save json file
    save_dir = '/Users/A14880/dev/sandbox/toyonakaFAQscraping/res'
    file_name = 'res.json'
    file_path = os.path.join(save_dir, file_name)
    with open(file_path, 'w') as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)