import requests
from bs4 import BeautifulSoup

URL_BASE  = "https://monip.io/"


def find_your_ip():
    page = requests.get(URL_BASE)
    if(page.status_code == 200):
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find('img', alt=True)
        return result['alt']
    else:
        return None