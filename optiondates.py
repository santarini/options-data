import os
import requests
import bs4 as bs
import csv

response = requests.get('https://www.nasdaq.com/symbol/aapl/option-chain')
soup = bs.BeautifulSoup(response.text, 'lxml')
optiondatecount = soup.find("div", {"id": "OptionsChain-dates"}).text
print(optiondatecount)
