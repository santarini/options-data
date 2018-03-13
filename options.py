import requests
import bs4 as bs

response = requests.get('https://www.nasdaq.com/symbol/aapl/option-chain?money=all&dateindex=6')
soup = bs.BeautifulSoup(response.text, 'lxml')
print(soup)
