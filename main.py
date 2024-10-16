from scripts.sitemap_reader import get_sitemap_items
from scripts.webpage_reader import scrape_webpage, get_webpage_items
import yaml
import pandas as pd
from datetime import datetime

def convert_to_ISO(date_string: str, date_type: str):
    if date_type == 'pubDate':
        return datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %z")
    elif date_type == 'ISO':
        return date_string
    print('Error: date of unknown type to convert_to_ISO function')
    return None

def main():
    source_paths = {
        'G1': f'./sources/G1.yml',
        'R7': f'./sources/R7.yml',
        'UOL': f'./sources/UOL.yml'
    }

    news_df = pd.DataFrame()
    for source, source_path in source_paths.items():
        with open(source_path, 'r') as file:
            source_dic = yaml.safe_load(file)

        sitemap_items = get_sitemap_items(source_dic['sitemap_url'], source_dic['sitemap_paths'])
        webpage_items = get_webpage_items(sitemap_items['url'], source_dic['webpage_paths'])
        
        sitemap_df = pd.DataFrame(sitemap_items)
        webpage_df = pd.DataFrame(webpage_items)
        scrape_df = sitemap_df.merge(webpage_df, on='url')
        scrape_df['source'] = source
        news_df = pd.concat([news_df, scrape_df], axis=0)
    
    news_df['date'] = news_df.apply(lambda x: convert_to_ISO(x['date'], x['date_format']), axis=1)
    column_order = ['source', 'url', 'title', 'subtitle', 'date']
    news_df = news_df[column_order]
    column_translation = {
        'source': 'Veículo',
        'url': 'Link da matéria',
        'title': 'Título da matéria',
        'subtitle': 'Subtítulo',
        'date': 'Data (em ISO)'
    }
    news_df.rename(columns=column_translation, inplace=True)
    news_df.to_csv('./result.csv', index=False)

if __name__ == "__main__":
    main()