import requests
from bs4 import BeautifulSoup

def delete_iframe(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    src_url = "https://blog.naver.com" + soup.iframe['src']
    return src_url
def title_scrapping(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find('meta', {'property': 'og:title'})['content']
    return title

def text_scrapping(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    soup = soup.find('div', {'class': 'se-main-container'})

    if soup:
        text = soup.get_text()
        text = text.replace('\n', ' ')
    else:
        text = "None"

    return text

def blog_parser(url):
    src_url = delete_iframe(url)
    text = text_scrapping(src_url)
    return text