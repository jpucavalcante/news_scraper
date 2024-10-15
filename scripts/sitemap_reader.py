import requests
from bs4 import BeautifulSoup
from lxml import etree
import yaml



def get_sitemap_items(url, item_path, n_of_items=10):
    try:
        response =  requests.get(url)
    except Exception as e:
        print('Reques failed')
        return None

    if response.status_code == 200:
        xml_content = etree.fromstring(response.content)
        
        items = xml_content.xpath(item_path)

        return items[:n_of_items]
    else:
        print('Request error {response.status_code}')
        return None
    
# WIP
# everything from down here will be deleted, just testing
source_paths = {
    'G1': f'./sources/G1.yml',
    'R7': f'./sources/R7.yml',
    'UOL': f'./sources/UOL.yml'
}

for source, source_path in source_paths.items():
    print(source_path)
    with open(source_path, 'r') as file:
        source_dic = yaml.safe_load(file)
    print(source_dic)
    print()

    res = get_sitemap_items(source_dic['sitemap_url'], source_dic['item_path'])
    print(source_dic['item_path'])
    print(res)
    print()