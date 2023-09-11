# scraping question and answer from shibuya city website
# each question, answer and the url is saved as a json file with the number of question as the file name
# each url is like https://shibuya-faq.dga.jp/faq_detail.html?id=6407&category=97&page=1
# scraper first curl html from the url, then parse the html with beautifulsoup
# then save the question, answer and url as a json file
# the json file is saved in res directory that is below the directory of this file

import os
import sys
import json
import requests
from bs4 import BeautifulSoup
import time

# get html file from url with requests
def get_html(url):
    headers_dic = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    r = requests.get(url, headers=headers_dic)
    return r.content

# parse html file with beautifulsoup
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# get question from html file
def get_qa(soup):
    q = soup.find('div', class_='ttlQuestion')
    # get_text if q is not None
    if q is not None:
        q = q.get_text(strip=True)
    return q

# get answer from html file
def get_ans(soup):
    a = soup.find('div', class_='answeBox')
    # get_text if a is not None
    if a is not None:
        a = a.get_text(strip=True)
    return a

# main function first curl html file from url
# then parse the html file with beautifulsoup
if __name__ == '__main__':
    res_json = {}
    for id in range(6207,6408):
        res_json[id] = {}
        url = f"https://shibuya-faq.dga.jp/faq_detail.html?id={id}"
        text = get_html(url)
        soup = parse_html(text)
        q = get_qa(soup)
        a = get_ans(soup)
        res_json[id]['question'] = q
        res_json[id]['title'] = "よくある質問"
        res_json[id]['answer'] = a        
        res_json[id]['url'] = url
    print(res_json)
    # save json file
    save_dir = '/Users/A14880/dev/sandbox/shibuyaFAQscraping/'
    file_name = 'res.json'
    file_path = os.path.join(save_dir, file_name)
    with open(file_path, 'w') as f:
        json.dump(res_json, f, indent=4, ensure_ascii=False)