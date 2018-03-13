import requests
import bs4 as bs

response = requests.get('https://www.nasdaq.com/symbol/aapl/option-chain?money=all&dateindex=6')
soup = bs.BeautifulSoup(response.text, 'lxml')
table = soup.findAll('table')[5]
for row in table.findAll('tr')[1:]:
    expiry = row.findAll('td')[0].text
    last = row.findAll('td')[1].text
    chg = row.findAll('td')[2].text
    bid = row.findAll('td')[3].text
    ask = row.findAll('td')[4].text
    vol = row.findAll('td')[5].text
    openInt = row.findAll('td')[6].text
    print(expiry)
    print(last)
    print(chg)
    print(bid)
    print(ask)
    print(vol)
    print(openInt)
