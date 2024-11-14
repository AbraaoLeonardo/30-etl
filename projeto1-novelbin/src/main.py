import requests
from bs4 import BeautifulSoup
from os import getcwd, makedirs, path
import re
import argparse
def fetch_data(URL):
    response = requests.get(URL).text
    return response

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    title = soup.find('a', class_='novel-title').get_text()
    chapter = soup.find('span', class_='chr-text').get_text()
    chapter_number = re.search(r'\d+', chapter)
    return paragraphs, title, int(chapter_number.group())

def save_data(paragraphs, title, chapter):
    paths = f'{getcwd()}/novelbin-data/'
    if not path.exists(paths):
        makedirs(paths)

    with open(f'{paths}{title} - {chapter}.txt','w') as files:
        for p in paragraphs:
            files.write(p.get_text() + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch data from a URL.')
    parser.add_argument('--url', type=str, required=True, help='The URL to fetch data from')
    args = parser.parse_args()
    URL = args.url

    html = fetch_data(URL=URL)
    paragraphs, title, chapter = parse_html(html)
    save_data(paragraphs, title, chapter)