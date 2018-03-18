import random
import sys
import os
import requests
import bs4 as bs
import csv

def find_date_index(ticker):
    response = requests.get('https://www.nasdaq.com/symbol/' + ticker +'/option-chain')
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
    optionDateFullList.pop()
    optionDateFullList.pop()
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
        optionType = input("\nWhat type of options would you like?\n\n1.) Calls\n2.) Puts\n3.) Both\n")
        i=1
        while i < optionDateFullListCount:
                dateID = i
                print("Getting option data for "+ ticker.upper() + " " + optionDateFullList[dateID-1][0])
                choose_optionType(optionType, ticker, dateID,optionDateFullList)
                i +=1
        print("Done!")
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
            optionType = input("\nWhat type of options would you like?\n\n1.) Calls\n2.) Puts\n3.) Both\n")
            for x in numberArray:
                dateID = x
                choose_optionType(optionType, ticker, dateID, optionDateFullList)
            print("Done!")

def choose_optionType(optionType, ticker, dateID, optionDateFullList):
    if (optionType == "1") or (optionType == "Calls") or (optionType == "calls") or (optionType == "Call") or (optionType == "call") or (optionType == "c"):
        get_call_data(ticker, dateID, optionDateFullList)
    elif (optionType == "2") or (optionType == "Puts") or (optionType == "puts") or (optionType == "Put") or (optionType == "put")or(optionType == "p"):
        get_put_data(ticker, dateID,optionDateFullList)
    elif (optionType == "3") or (optionType == "Both") or (optionType == "both") or (optionType == "b"):
        get_call_data(ticker, dateID,optionDateFullList)
        get_put_data(ticker, dateID,optionDateFullList)
    else:
        optionType = input("\nWhat type of options would you like?\n\n1.) Calls\n2.) Puts\n3.) Both\n")
        choose_optionType(optionType, ticker, dateID, optionDateFullList)

def get_call_data(ticker, dateID, optionDateFullList):
    #create source folder if it doesnt exist yet
    if not os.path.exists('option_dfs'):
        print("Creating Option DFS Folder")
        os.makedirs('option_dfs')

    #create sub folder in source folder if it doesnt exist yet
    if not os.path.exists('option_dfs/' + ticker.upper()):
        print("Creating " + ticker.upper() + " Folder")
        os.makedirs('option_dfs/' + ticker.upper())

    if not os.path.exists('option_dfs/' + ticker.upper() + '/calls'):
        print("Creating " + ticker.upper() + " Calls Folder")
        os.makedirs('option_dfs/' + ticker.upper()+ '/calls')

    if not os.path.exists('option_dfs/' + ticker.upper() + '/calls/'+ optionDateFullList[dateID-1][0] + '.csv'):
        print("Getting Call data for "+ ticker.upper() + " " + optionDateFullList[dateID-1][0])
        response = requests.get('https://www.nasdaq.com/symbol/' + ticker + '/option-chain?money=all&dateindex='+ str(dateID-1))
        soup = bs.BeautifulSoup(response.text, 'lxml')
        calltable = soup.findAll('table')[5]
        with open('option_dfs/' + ticker.upper() + '/calls/'+ optionDateFullList[dateID-1][0] + '.csv', 'a') as csvfile:
            fieldnames = ['Ticker', 'Expiry', 'Last', 'Change', 'Bid', 'Ask', 'Vol', 'Open Interest', 'Strike']
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
                writer.writerow({'Ticker': ticker.upper(),'Expiry': expiry,'Last': last,'Change': chg,'Bid': bid,'Ask': ask,'Vol': vol,'Open Interest': openInt, 'Strike': strike})
    else: print ('Already have call data for ' + ticker.upper() +" "+ optionDateFullList[dateID-1][0])


def get_put_data(ticker, dateID, optionDateFullList):
    #create source folder if it doesnt exist yet
    if not os.path.exists('option_dfs'):
        print("Creating Option DFS Folder")
        os.makedirs('option_dfs')

    #create sub folder in source folder if it doesnt exist yest
    if not os.path.exists('option_dfs/' + ticker.upper()):
        print("Creating " + ticker.upper() + " Folder")
        os.makedirs('option_dfs/' + ticker.upper())

    if not os.path.exists('option_dfs/' + ticker.upper() + '/puts'):
        print("Creating " + ticker.upper() + " Puts Folder")
        os.makedirs('option_dfs/' + ticker.upper()+ '/puts')

    if not os.path.exists('option_dfs/' + ticker.upper() + '/puts/'+ optionDateFullList[dateID-1][0] + '.csv'):
        print("Getting Put data for "+ ticker.upper() + " " + optionDateFullList[dateID-1][0])
        response = requests.get('https://www.nasdaq.com/symbol/' + ticker + '/option-chain?money=all&dateindex='+ str(dateID-1))
        soup = bs.BeautifulSoup(response.text, 'lxml')
        puttable = soup.findAll('table')[5]
        with open('option_dfs/' + ticker.upper() + '/puts/'+ optionDateFullList[dateID-1][0] + '.csv', 'a') as csvfile:
            fieldnames = ['Ticker', 'Expiry', 'Last', 'Change', 'Bid', 'Ask', 'Vol', 'Open Interest', 'Strike']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
            writer.writeheader()
            for row in puttable.findAll('tr')[1:]:
                expiry = row.findAll('td')[9].text
                last = row.findAll('td')[10].text
                chg = row.findAll('td')[11].text
                bid = row.findAll('td')[12].text
                ask = row.findAll('td')[13].text
                vol = row.findAll('td')[14].text
                openInt = row.findAll('td')[15].text
                strike = row.findAll('td')[8].text
                writer.writerow({'Ticker': ticker.upper(),'Expiry': expiry,'Last': last,'Change': chg,'Bid': bid,'Ask': ask,'Vol': vol,'Open Interest': openInt, 'Strike': strike})
    else: print ('Already have put data for ' + ticker.upper() +" "+ optionDateFullList[dateID-1][0])

ticker = input("What ticker are you looking for? \n")
find_date_index(ticker)
