import requests
import bs4 as bs
import re


response = requests.get('https://finviz.com/quote.ashx?t='+ 'goog')
soup = bs.BeautifulSoup(response.text, 'lxml')

#Optionable
optionable = soup('td', text=re.compile("Optionable"))[0].findNext('td')
print(optionable.text)

#recom
recom = soup('td', text=re.compile("Recom"))[0].findNext('td')
print(recom.text)

