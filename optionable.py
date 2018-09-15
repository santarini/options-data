import requests
import bs4 as bs
import re
import csv

with open("cleanSandP.csv") as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        ticker = (row['Ticker'])
        print(ticker)
        response = requests.get('https://finviz.com/quote.ashx?t='+ ticker)
        soup = bs.BeautifulSoup(response.text, 'lxml')

        #Optionable
        optionable = soup('td', text=re.compile("Optionable"))[0].findNext('td')
        print(optionable.text)

        #recom
        recom = soup('td', text=re.compile("Recom"))[0].findNext('td')
        print(recom.text)
