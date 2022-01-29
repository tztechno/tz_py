from bs4 import BeautifulSoup
import requests

def ask_yahoo(x):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    params = {'p': x}    #search keyword in this case "cyber security"
    html = requests.get('https://search.yahoo.co.jp/search', headers=headers, params=params)
    soup = BeautifulSoup(html.text, 'lxml')
    
    for result in soup.find_all('a'):
        link = result['href']
        if 'http' in link and 'yahoo' not in link:
            print(link)
            break