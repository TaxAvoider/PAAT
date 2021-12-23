"""
Created on 24/11/2021
Example made using https://oxylabs.io/blog/python-web-scraping
Helpful reference for html syntax: https://www.w3schools.com/tags/default.asp
"""

import requests
from bs4 import BeautifulSoup as Bs
import re

# Test URLs
url1 = f"https://www.wsj.com/market-data/quotes/company-list"
url2 = f"https://www.wsj.com/market-data/quotes/company-list/sector/chemicals"
url3 = "https://www.wsj.com/market-data/quotes/company-list/sector/fishing"

# Sneaky little deception. Credit to Bowen
headers = {
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/75.0.3770.142 Safari/537.36'
    }

"""
Gets access to the overall url in the page
"""
def get_page_data(url):

    subj_list = requests.get(url, headers=headers).content
    soup = Bs(subj_list, features="html.parser")

    # Searching for the
    items = soup.find("ul", {"class": "cl-tree cl-list"})

    links = items.find_all("a", attrs={'href': re.compile("^https://")})
    return links


"""
Takes a url for the page, and returns the number of pages
Used in connection with the sector access page
"""
def page_access(url):
    # Getting page number test
    pge_lst = requests.get(url, headers=headers).content
    soup2 = Bs(pge_lst, features="html.parser")
    page_num = soup2.find("ul", {"class": "cl-pagination"})
    pages = page_num.find_all("a")
    if len(pages) == 0:
        return 1
    else:
        # Purpose of -2 is to exclude next and previous items of pages list
        return len(pages) - 2


"""
Inputs the url page, and takes all stocks for that given page
Outputs the a list of all urls of stocks
"""
def stock_sector(sector):
    # gets the url of all stocks
    # Need to change the names
    sector_list = requests.get(sector, headers=headers).content
    sector_soup = Bs(sector_list, features="html.parser")
    stock_list = sector_soup.find("table", class_="cl-table")
    stock_links = stock_list.find_all("a", attrs={'href': re.compile("^https://")})
    stock_url_list = []
    # Cycles through each page of the given stock
    for stock_url in stock_links:
        stock_url_list.append(stock_url.get('href'))
    return stock_url_list


# Water utilities test
# print(len(stock_sector(links[-1].get('href'))))
# Chemicals test
# print(len(stock_sector(get_page_data(url1)[4].get('href'))))
# Aerospace and defence test
# print(len(stock_sector(links[32].get('href'))))

# for page in get_page_data(url1):
#     print(f"{page.text}: {page_access(page.get('href'))}")

for page in stock_sector(url2):
    x = None
