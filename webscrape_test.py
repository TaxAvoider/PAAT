"""
Created on 24/11/2021
Example made using https://oxylabs.io/blog/python-web-scraping
Helpful reference for html syntax: https://www.w3schools.com/tags/default.asp
"""

import requests
from lxml import html
from bs4 import BeautifulSoup as bs
import re

# Sneaky little deception. Credit to Bowen
headers = {
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/75.0.3770.142 Safari/537.36'
}

subj_list = requests.get(f"https://www.wsj.com/market-data/quotes/company-list", headers=headers).content
soup = bs(subj_list, features="html.parser")

# Searching for the
items = soup.find("ul", {"class": "cl-tree cl-list"})

links = items.find_all("a", attrs={'href': re.compile("^https://")})
sector_url = ""
for link in links:
    sector_url = (link.get('href'))

# gets the name of all stock
sector_list = requests.get(sector_url, headers=headers).content
sector_soup = bs(sector_list, features="html.parser")
stock_list = sector_soup.find("table", class_="cl-table")
stock_links = stock_list.find_all("a", attrs={'href': re.compile("^https://")})
for stock_url in stock_links:
    print(stock_url.get('href'))
