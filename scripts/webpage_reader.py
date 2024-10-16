import requests
from bs4 import BeautifulSoup

def tag_handler(soup: BeautifulSoup, tag_dic: dict) -> str:
    if tag_dic['tag'] == 'meta':
        return soup.find(tag_dic['tag'], attrs={tag_dic['attribute']:tag_dic['attribute_value']}).get('content')
    else:
        return soup.find(tag_dic['tag'], attrs={tag_dic['attribute']:tag_dic['attribute_value']}).text

def scrape_webpage(url: str, webpage_paths: dict) -> dict:
    try:
        response =  requests.get(url)
    except Exception as e:
        print('Request failed:', e)
        return None
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        webpage_dic = {}
        for item, tag_dic in webpage_paths.items():
            try:
                webpage_dic[item] = tag_handler(soup, tag_dic)
            except Exception as e:
                print('Error {e} at item {item} on url {url}')
                webpage_dic[item] = None

        return webpage_dic
    else:
        print('Request error {response.status_code}')
        return None

def get_webpage_items(urls, webpage_paths):
    webpage_items = []
    for url in urls:
        webpage_item = scrape_webpage(url, webpage_paths)
        webpage_item['url'] = url
        webpage_items.append(webpage_item)
    return webpage_items
