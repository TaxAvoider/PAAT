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

# Getting page numbere test
url1 = f"https://www.wsj.com/market-data/quotes/company-list/sector/chemicals"
url2 = "https://www.wsj.com/market-data/quotes/company-list/sector/fishing"
pge_lst = requests.get(url2, headers=headers).content
soup2 = bs(pge_lst, features="html.parser")
page_num = soup2.find("ul", {"class": "cl-pagination"})
pages = page_num.find_all("a")
if len(pages) == 0:
    print("Only one page")
else:
    total_pages = []
    for page in pages:
        total_pages.append(page.text)

    for i in range(len(total_pages)):
        if total_pages[i] == "Next":
            print(total_pages[i-1])

"""
Gets stock dater for a given industry in a sector
Need to add feature to search through pages of all stock on each industry
"""
def stock_sector(sector):
    # gets the url of all stocks
    # Need to change the names
    sector_list = requests.get(sector, headers=headers).content
    sector_soup = bs(sector_list, features="html.parser")
    stock_list = sector_soup.find("table", class_="cl-table")
    stock_links = stock_list.find_all("a", attrs={'href': re.compile("^https://")})
    stock_url_list = []
    for stock_url in stock_links:
        stock_url_list.append(stock_url.get('href'))
    return stock_url_list

#for link in links:
#    print(x, link)

#for link in links:
    #stocks = stock_sector(link.get('href'))
# Water utilities test
#print(len(stock_sector(links[-1].get('href'))))
# Chemicals test
#print(len(stock_sector(links[4].get('href'))))
# Aerospace and defence test
#print(len(stock_sector(links[32].get('href'))))

