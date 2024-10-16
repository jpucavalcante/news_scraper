import requests
from lxml import etree

def get_sitemap_items(url: str, sitemap_paths: dict, n_of_items: int = 10) -> dict:
    try:
        response =  requests.get(url)
    except Exception as e:
        print('Request failed:', e)
        return None

    if response.status_code == 200:
        root = etree.fromstring(response.content)

        sitemap_items = {}
        sitemap_items['date'] = [child.text for child in root.xpath(sitemap_paths['date_info']['date'])[:n_of_items]]
        sitemap_items['date_format'] = [sitemap_paths['date_info']['date_format']]*n_of_items
        for item, xpath in sitemap_paths.items():
            if item != "date_info":
                sitemap_items[item] = [child.text for child in root.xpath(xpath)[:n_of_items]]
        return sitemap_items
    else:
        print('Request error {response.status_code}')
        return None
