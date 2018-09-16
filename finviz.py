import requests
import bs4 as bs
import re
import csv

with open("cleanSandP - Copy.csv") as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    with open('finvizSP.csv', 'a') as csvfile:
        fieldnames = ['Ticker',
                      'Optionable',
                      'Recom',
                      ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
        for row in reader:
            try:
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
                writer.writerow({'Ticker': ticker.upper(),
                                 'Optionable': optionable.text,
                                 'Recom': recom.text
                                 })
            except IndexError:
                writer.writerow({'Ticker': ticker.upper(),
                                 'Optionable': 'Error',
                                 'Recom': 'Error'
                                 })
                continue

 
