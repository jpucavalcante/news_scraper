# news_scrapper
A flexible news scraper that extracts information from various sources using a yaml configuration file. The scraper prioritizes data reliability by letting the yaml file be very flexible and supports both xml sitemap feeds and webpage scraping.

# Features
- Dynamic Configuration: Easily adjustable using a YAML file.
- Multi-Source Support: Handles various news sources with unique structures.
- Stability Hierarchy: Let's you set a preference order for data retrieval, in my usecase: sitemap → meta tags → og (open graph) -> HTML.

# Flowchart
![scrapper_diagram drawio](https://github.com/user-attachments/assets/7e9a8711-cb97-42b3-9e68-4bf02a981beb)

# Example of yaml file:
![image](https://github.com/user-attachments/assets/17f9a248-4af7-474c-ba16-5a5e1132803b)
