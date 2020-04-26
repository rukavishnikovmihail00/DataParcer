import requests
from bs4 import BeautifulSoup as BS

URL = 'https://vk.com/rukavishnikov_mishka'

def get_url(url):
    r = requests.get(url)
    return r


def parse():
    html = get_url(URL)
    if html.status_code == 200:
        pass
    else:
        print("Something went wrong")

parse()