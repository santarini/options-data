import random
import sys
import os
import requests
import bs4 as bs
import csv

with open("optionTickers.csv") as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        ticker = (row['Ticker'])
        print(ticker)
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
        optionDateFullListCount = len(optionDateFullList)

        i=1
        while i <= (optionDateFullListCount):
            dateID = i
            
            ##GET CALL DATA
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
                calltable = soup.findAll('table')[2]
                with open('option_dfs/' + ticker.upper() + '/calls/'+ optionDateFullList[dateID-1][0] + '.csv', 'a') as csvfile:
                    fieldnames = ['Ticker',
                                  'Expiry',
                                  'Last',
                                  'Change',
                                  'Bid',
                                  'Ask',
                                  'Vol',
                                  'Open Interest',
                                  'Strike',
                                  'Code',
                                  'HREF'
                                  ]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
                    writer.writeheader()
                    for row in calltable.findAll('tr')[1:]:
                        expiry = row.findAll('td')[0].text
                        expiryAnchor = row.findAll('a')[0]
                        optionHREF = expiryAnchor['href']
                        optionCode = expiryAnchor['href'].split('https://www.nasdaq.com/symbol/' + ticker.lower() + '/option-chain/')[1]
                        optionCode = optionCode.split('-')[0]
                        last = row.findAll('td')[1].text
                        chg = row.findAll('td')[2].text
                        bid = row.findAll('td')[3].text
                        ask = row.findAll('td')[4].text
                        vol = row.findAll('td')[5].text
                        openInt = row.findAll('td')[6].text
                        strike = row.findAll('td')[8].text
                        writer.writerow({'Ticker': ticker.upper(),
                                         'Expiry': expiry,
                                         'Last': last,
                                         'Change': chg,
                                         'Bid': bid,
                                         'Ask': ask,
                                         'Vol': vol,
                                         'Open Interest': openInt,
                                         'Strike': strike,
                                         'Code': optionCode,
                                         'HREF': optionHREF
                                         })
            else:
                print ('Already have call data for ' + ticker.upper() +" "+ optionDateFullList[dateID-1][0])

            #GET PUT DATA
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
                puttable = soup.findAll('table')[2]
                with open('option_dfs/' + ticker.upper() + '/puts/'+ optionDateFullList[dateID-1][0] + '.csv', 'a') as csvfile:
                    fieldnames = ['Ticker',
                                  'Expiry',
                                  'Last',
                                  'Change',
                                  'Bid',
                                  'Ask',
                                  'Vol',
                                  'Open Interest',
                                  'Strike',
                                  'Code',
                                  'HREF'
                                  ]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
                    writer.writeheader()
                    for row in puttable.findAll('tr')[1:]:
                        expiry = row.findAll('td')[0].text
                        expiryAnchor = row.findAll('a')[0]
                        optionHREF = expiryAnchor['href']
                        optionCode = expiryAnchor['href'].split('https://www.nasdaq.com/symbol/' + ticker.lower() + '/option-chain/')[1]
                        optionCode = optionCode.split('-')[0]
                        last = row.findAll('td')[10].text
                        chg = row.findAll('td')[11].text
                        bid = row.findAll('td')[12].text
                        ask = row.findAll('td')[13].text
                        vol = row.findAll('td')[14].text
                        openInt = row.findAll('td')[15].text
                        strike = row.findAll('td')[8].text
                        writer.writerow({'Ticker': ticker.upper(),
                                         'Expiry': expiry,
                                         'Last': last,
                                         'Change': chg,
                                         'Bid': bid,
                                         'Ask': ask,
                                         'Vol': vol,
                                         'Open Interest': openInt,
                                         'Strike': strike,
                                         'Code': optionCode,
                                         'HREF': optionHREF
                                         })
            else:
                print ('Already have put data for ' + ticker.upper() +" "+ optionDateFullList[dateID-1][0])
            i +=1
