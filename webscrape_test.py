"""
Created on 24/11/2021
Example made using https://oxylabs.io/blog/python-web-scraping
Helpful reference for html syntax: https://www.w3schools.com/tags/default.asp
"""
import time
import requests
from bs4 import BeautifulSoup as Bs
import re
import pandas as pd

# Test URLs
url1 = f"https://www.wsj.com/market-data/quotes/company-list"
url2 = f"https://www.wsj.com/market-data/quotes/company-list/sector/chemicals"
url3 = f"https://www.wsj.com/market-data/quotes/company-list/sector/fishing"
url4 = f"https://www.wsj.com/market-data/quotes/company-list/sector/investing-securities/2"
url5 = f"https://www.wsj.com/market-data/quotes/company-list/sector/investing-securities"

# Creating the database as a test
df = pd.DataFrame(columns=["Name", "Ticker", "region", "exchange"])

# Dictionary of different sectors and industries
sector_dict = {}
f = open("data.txt", "w")

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

    # Searching for the industries
    items = soup.find("ul", {"class": "cl-tree cl-list"})

    # Idea to swap these values around, where every industry has its assigned sector
    # That way its far easier to access the given sector for industry
    if len(sector_dict) == 0:

        sectors = items.find_all("a")
        for sector in sectors:
            sector_name = sector.text
            sector_dict[sector_name] = None

        sector = items.find_all("li")
        for industry in sector:
            if "  " in industry.text:
                industries = industry.text.split("   ")
                for sub_sector in industries[1:]:
                    if sub_sector in list(sector_dict.keys()):
                        sector_dict[sub_sector] = industries[0]
                # Sorted with the value at the beginning with all the keys after with a white space at end
                # sector_dict[industries[0]] = industries[1:]

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
        tot_pages = 0
        for page in pages:
            value = page.text.split("-")
            if value[0] != "Next":
                tot_pages = value[-1]
            else:
                return int(tot_pages)
        # Purpose of -2 is to exclude next and previous items of pages list
        return int(tot_pages)


"""
Helper function cause I'm lazy with my dictionary
"""
def swap_dict():
    keys = list(sector_dict.keys())
    values = list(sector_dict.values())
    for key, val in sector_dict.items():
        print(key)

    return sector_dict


"""
Inputs the url page, and takes all stocks for that given page
Outputs the a list of all urls of stocks
"""
def stock_sector(sector, stock_sector):

    # gets the url of all stocks
    # Need to change the names
    sector_list = requests.get(sector, headers=headers).content
    sector_soup = Bs(sector_list, features="html.parser")

    stock_list = sector_soup.find("table", class_="cl-table")
    # Gets just url and title of all stocks
    stock_links = stock_list.find_all("a", attrs={'href': re.compile("^https://")})
    stock_info = stock_list.find_all("tr")

    total_data = []
    i = 1
    # Loops through every item
    for stock in stock_info[1:]:
        total_data.append(data_sorter(stock, stock_sector))
        # print(data_sorter(stock))
        i += 1

    # Prints the data
    # print(df)

    stock_url_list = []
    # Cycles through each page of the given stock
    for stock_url in stock_links:
        # print(stock_url)
        stock_url_list.append(stock_url.get('href'))
    # return stock_url_list
    return total_data


"""
Takes in the stock data
Outputs a tuple of the data that contains:
(Name, ticker, region, exchange)
"""
def data_sorter(data, sub_sector):
    sorted_data = data.find_all("td")
    # Data is in the form of 3 segments
    # 1: Name, and ticker
    # 2: Region/Country
    # 3: Exchange
    title = sorted_data[0]
    # Extracts the ticker as it is surrounded by two brackets. The \(.*\) is regex (re) notation to find it
    # ticker_raw = re.findall(r'\(.*\)', title.text)
    # ticker = ticker_raw[0][1:len(ticker_raw[0])-1]
    # Need new method if getting ticker as some firms have () in title
    ticker_raw = title.find("a", attrs={"href": re.compile("^http")})
    ticker_raw = ticker_raw.get("href")
    ticker = ticker_raw.split("/")[-1]
    name = title.find("span").text
    region = sorted_data[1].text
    exchange = sorted_data[2].text
    return name, ticker, region, exchange, sector_dict[sub_sector], sub_sector

# Water utilities test
# print(len(stock_sector(links[-1].get('href'))))
# Chemicals test
# print(len(stock_sector(get_page_data(url1)[4].get('href'))))
# Aerospace and defence test
# print(len(stock_sector(links[32].get('href'))))

# for page in get_page_data(url1):
#     print(f"{page.text}: {page_access(page.get('href'))}")

def main():
    num_stocks = 0
    # Gets data on all sectors
    for industry in get_page_data(url1):
        sector = industry.text
        f.write(sector)

        # Loops through each sector
        url = industry.get("href")

        # Gets all stock for the given sector
        num_pages = page_access(url)
        print(sector)
        for urls in range(num_pages):
            stocks_list = stock_sector(f"{url}/{urls+1}", sector)
            f.write(str(stocks_list))
            num_stocks += len(stocks_list)

    print(f"Ran through a total of {num_stocks} different publicly listed stocks")
    return 0


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total run time to get all stocks was {end_time-start_time}\nProgram complete!")
    f.close()
