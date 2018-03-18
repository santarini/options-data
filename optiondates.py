import os
import requests
import bs4 as bs
import csv

response = requests.get('https://www.nasdaq.com/symbol/aapl/option-chain')
soup = bs.BeautifulSoup(response.text, 'lxml')
optiondatestring = soup.find("div", {"id": "OptionsChain-dates"}).text
optiondatestring = optiondatestring.lstrip()
optiondatestring = optiondatestring.replace(" |  ", ",")
optiondatestring = optiondatestring.replace(" ", "_20")
optionDateList = optiondatestring.split(",")
optionDateFullList = []
i = 0
for x in optionDateList:    
    optionDateFullList.append([x,i])
    i +=1
print(optionDateList)
print(optionDateFullList)
