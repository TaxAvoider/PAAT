"""
Created on 24/11/2021
Example made using https://oxylabs.io/blog/python-web-scraping
"""

import requests
from lxml import html
from bs4 import BeautifulSoup

"""
response = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_population_in_2010")

tree = html.fromstring(response.text)
countries = tree.xpath('//span[@class="flagicon"]')
for country in countries:
    print(country.xpath('./following-sibling::a/text()')[0])

url = "https://www.wsj.com/market-data/quotes/company-list"
url = "https://www.nasdaq.com/market-activity/cryptocurrency/btc/historical"

# Boiler plate below
response = requests.get(url)
tree = html.fromstring(response.text)

# Searching for the sector:
# sectors = tree.xpath('//div[@class="index-sector border-box"]')
# print(type(sectors))

price_data = tree.xpath('//tbody[@class="historical-data__table-body"]')
print(price_data)

#for sector in sectors:
#    print(sector)
"""

headers = {
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

subj_list = requests.get(f"https://www.wsj.com/market-data/quotes/company-list", headers=headers).content
soup = BeautifulSoup(subj_list, features="html.parser")

print(soup.find("ul", {"class": "cl-tree cl-list"}))