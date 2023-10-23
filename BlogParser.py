import requests
from bs4 import BeautifulSoup

def delete_iframe(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    src_url = "https://blog.naver.com" + soup.iframe['src']
    return src_url

def scrap(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'lxml')    

def get_title(soup: BeautifulSoup):
    title = soup.find('meta', {'property': 'og:title'})['content']

    return title

def get_text(soup: BeautifulSoup):
    soup = soup.find('div', {'class': 'se-main-container'})

    if soup:
        text = soup.get_text()
        text = text.replace('\n', ' ')
        text = text.replace('  ', ' ')
    else:
        text = "None"

    return text

def get_nickname(soup: BeautifulSoup):
    nick = soup.find('meta', {'property': 'naverblog:nickname'})['content']
    return nick

def blog_parser(url):
    print("url:", url)
    src_url = delete_iframe(url)
    soup = scrap(src_url)
    title = get_title(soup)
    text = get_text(soup)
    nick = get_nickname(soup)
    return nick, title, text

if __name__ == '__main__':
    print(blog_parser("https://blog.naver.com/rapunzelli/223244204456"))