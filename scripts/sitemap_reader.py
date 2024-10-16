import requests
from lxml import etree

def sitemap_item_handler(root: etree.ElementTree.Element, item: str, item_val: str|dict, sitemap_items: dict, n_of_items: int):
    if item == "date_info":
        sitemap_items['date'] = [child.text for child in root.xpath(item_val['date'])[:n_of_items]]
        sitemap_items['date_format'] = [item_val['date_format']]*n_of_items
    else:
        sitemap_items[item] = [child.text for child in root.xpath(item_val)[:n_of_items]]
        

def get_sitemap_items(url: str, sitemap_paths: dict, n_of_items: int = 10) -> dict:
    try:
        response =  requests.get(url)
    except Exception as e:
        print('Request failed:', e)
        return None

    if response.status_code == 200:
        root = etree.fromstring(response.content)

        sitemap_items = {}
        for item, item_val in sitemap_paths.items():
            sitemap_item_handler(root, item, item_val, sitemap_items, n_of_items)
        return sitemap_items
    else:
        print('Request error {response.status_code}')
        return None
