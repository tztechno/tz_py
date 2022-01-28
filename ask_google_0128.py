import requests, lxml, webbrowser  
from bs4 import BeautifulSoup

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}

def ask_google(x):
    
    params = {'q': x}    #search keyword in this case "cyber security"

    html = requests.get('https://www.google.com/search', headers=headers, params=params).text
    soup = BeautifulSoup(html, 'lxml')
    links=[]
    # container with all needed data
    for result in soup.select('.tF2Cxc'):
        link = result.select_one('.yuRUbf a')['href']
        print(link)
        links+=[link]
    
    return links

ask_google('Alexa')