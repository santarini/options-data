import random
import sys
import os
import requests
import bs4 as bs
import csv

def find_date_index(ticker):
    response = requests.get('https://www.nasdaq.com/symbol/'+ ticker.lower() +'/option-chain')
    soup = bs.BeautifulSoup(response.text, 'lxml')
    optiondatestring = soup.find("div", {"id": "OptionsChain-dates"}).text
    optiondatestring = optiondatestring.lstrip()
    optiondatestring = optiondatestring.replace(" |  ", ",")
    optionDateList = optiondatestring.split(",")
    optionDateFullList = []
    i = 0
    for x in optionDateList:    
        optionDateFullList.append([x,i])
        i +=1
    print("\nThese are the available contract dates for that ticker:")
    i =1
    for index, x in enumerate(optionDateFullList):
        print(str(i) +". " + x[0])
        i += 1
    optionDateFullListCount = len(optionDateFullList)
    selection(ticker, optionDateFullList,optionDateFullListCount)




def selection(ticker, optionDateFullList,optionDateFullListCount):
    startNumber = input("\nWhich dates would you like?\n")
    if (startNumber == "All") or (startNumber == "all"):
        i=1
        while i < optionDateFullListCount:
            get_option_data()
    else:
        numberArray = [int(i) for i in startNumber.split()]
        numberArray.sort()
        if ((len(numberArray) != len(set(numberArray))) == True):
            print("\nYou entered a duplicate")
            print(numberArray)
            selection()
        elif (len(numberArray) > optionDateFullListCount ):
            print("\nYou entered too many numbers")
            print(numberArray)
            selection()
##        elif (max(numberArray) > max(optionDateFullList)):
##            print("\nOne or more of your values is too large")
##            print(numberArray)
##            selection()
        elif (min(numberArray) < 1):
            print("\nOne or more of your values is too small")
            print(numberArray)
            selection()
        else:
            print(numberArray)
            for x in numberArray:
                dateID = x
                print("Getting option data for "+ticker + optionDateFullList[dateID][1])
                get_option_data(ticker, dateID)



def get_option_data(ticker, dateID):
    #create source folder if it doesnt exist yet
    if not os.path.exists('option_dfs'):
        os.makedirs('option_dfs')

    #create sub folder in source folder if it doesnt exist yest
    if not os.path.exists('option_dfs/' + ticker.upper()):
        os.makedirs('option_dfs/' + ticker.upper())

        
    if not os.path.exists('option_dfs/' + ticker.upper() + '/'+ ticker + '.csv'):
        
        response = requests.get('https://www.nasdaq.com/symbol/' + ticker + '/option-chain?money=all&dateindex='+ str(dateID))
        soup = bs.BeautifulSoup(response.text, 'lxml')
        calltable = soup.findAll('table')[5]
        with open('option_dfs/' + ticker.upper() + '/'+ ticker + '.csv', 'a') as csvfile:
            fieldnames = ['Ticker', 'Expiry','Last','Change','Bid','Ask','Vol','Open Interest']
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
                writer.writerow({'Ticker': ticker.upper(),'Expiry': expiry,'Last': last,'Change': chg,'Bid': bid,'Ask': ask,'Vol': vol,'Open Interest': openInt})


ticker = input("What ticker are you looking for? \n")
find_date_index(ticker)
