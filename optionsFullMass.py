import random
import sys
import os
import requests
import bs4 as bs
import csv

def get_tickers():
    tickers = input("Please enter your tickerss: \n")
    #create array
    tickers = [str(i) for i in tickers.split()]
    print(tickers)
    for x in tickers:
        ticker = x
        find_date_index(ticker)
    print("Done!")

def find_date_index(ticker):
    response = requests.get('https://www.nasdaq.com/symbol/'+ ticker.lower() +'/option-chain')
    soup = bs.BeautifulSoup(response.text, 'lxml')
    optiondatestring = soup.find("div", {"id": "OptionsChain-dates"}).text
    optiondatestring = optiondatestring.lstrip()
    optiondatestring = optiondatestring.replace(" |  ", ",")
    optionDateList = optiondatestring.split(",")
    optionDateFullList = []
    i = 1
    for x in optionDateList:    
        optionDateFullList.append([x,i])
        i +=1
    optionDateFullListCount = len(optionDateFullList)
    selection(ticker, optionDateFullList,optionDateFullListCount)
    

def selection(ticker, optionDateFullList,optionDateFullListCount):
    i=1
    while i < (optionDateFullListCount - 2):
            dateID = i
            print("Getting option data for "+ ticker.upper() + " " + optionDateFullList[dateID-1][0])
            get_option_data(ticker, dateID,optionDateFullList)
            i +=1


def get_option_data(ticker, dateID, optionDateFullList):
    #create source folder if it doesnt exist yet
    if not os.path.exists('option_dfs'):
        os.makedirs('option_dfs')

    #create sub folder in source folder if it doesnt exist yest
    if not os.path.exists('option_dfs/' + ticker.upper()):
        os.makedirs('option_dfs/' + ticker.upper())

        
    if not os.path.exists('option_dfs/' + ticker.upper() + '/'+ optionDateFullList[dateID-1][0] + '.csv'):
        
        response = requests.get('https://www.nasdaq.com/symbol/' + ticker + '/option-chain?money=all&dateindex='+ str(dateID-1))
        soup = bs.BeautifulSoup(response.text, 'lxml')
        calltable = soup.findAll('table')[5]
        with open('option_dfs/' + ticker.upper() + '/'+ optionDateFullList[dateID-1][0] + '.csv', 'a') as csvfile:
            fieldnames = ['ticker', 'Expiry', 'Last', 'Change', 'Bid', 'Ask', 'Vol', 'Open Interest', 'Strike']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
            writer.writeheader()
            for row in calltable.findAll('tr')[1:]:
                expiry = row.findAll('td')[0].text
                last = row.findAll('td')[1].text
                chg = row.findAll('td')[2].text
                bid = row.findAll('td')[3].text
                ask = row.findAll('td')[4].text
                vol = row.findAll('td')[5].text
                openInt = row.findAll('td')[6].text
                strike = row.findAll('td')[8].text
                writer.writerow({'ticker': ticker.upper(),'Expiry': expiry,'Last': last,'Change': chg,'Bid': bid,'Ask': ask,'Vol': vol,'Open Interest': openInt, 'Strike': strike})
    else: print ('Already have ' + 'option_dfs/' + ticker.upper() + '/'+ optionDateFullList[dateID-1][0] + '.csv')


get_tickers()
