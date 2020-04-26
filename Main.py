import requests
from bs4 import BeautifulSoup as BS

URL = 'https://ru.wikipedia.org/wiki/Россия'
def get_url(url):
    r = requests.get(url)
    return r


def parse():
    html = get_url(URL)
    if html.status_code == 200:
        get_content(html)
    else:
        print("Something went wrong")


def get_content(html):
    soup = BS(html, 'lxml')
    links = {}
    link = soup.find('a', links)
    print(links)
parse()