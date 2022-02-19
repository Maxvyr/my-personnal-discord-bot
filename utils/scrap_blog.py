import requests
from bs4 import BeautifulSoup, Comment

URL_BASE  = "https://discord.com/blog"


def blog_discord_date_last_article():
    page = requests.get(URL_BASE)
    if(page.status_code == 200):
        soup = BeautifulSoup(page.content, 'html.parser')
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        return comments[0]
    else:
        return None
    
    
def blog_discord_last_article():
    page = requests.get(URL_BASE)
    if(page.status_code == 200):
        soup = BeautifulSoup(page.content, 'html.parser')
        articles = soup.find_all("div", class_="collection-item-3 w-dyn-item w-col w-col-6")
        link_article = articles[0].find_all('a', href=True)
        link = URL_BASE.removesuffix("/blog") + str(link_article[0]['href'])
        return link
    else:
        return None