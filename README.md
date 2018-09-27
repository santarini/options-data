# Options Data

This is a repo of Python 3 programs that use requests and beautiful soup to navigate to the NASDAQ website and scrape option data into CSVs.

Both <a href="https://github.com/santarini/options-data/blob/master/optionsFull.py">optionsFull.py</a> and <a href="https://github.com/santarini/options-data/blob/master/optionsFullMass.py">optionsFullMass.py</a> are independent fully working programs. As is <a href="https://github.com/santarini/options-data/blob/master/optionsDataFromCSV.py">optionsDataFromCSV.py</a>


# Contents

###### optiondates.py

This was the second step in the algo, it goes to the NASDAQ website figures out what expiry dates are available for option contracts of your specified ticker, and reports back to you.

###### optionsFull.py

This is the first full independent working version. It finds call, put or both pricing data for a <b>single</b> ticker at a time. It also prompts you at every step of the process.

###### optionsFullMass.py

This is the first full mass independent working version. Whereas <a href="https://github.com/santarini/options-data/blob/master/optionsFull.py">optionsFull.py</a> finds option data for a single ticker and prompts you ever step of the way, <a href="https://github.com/santarini/options-data/blob/master/optionsFullMass.py">optionsFullMass.py</a> can take in several tickers and gives you the option data for all available dates. It was intended to be used for a greater number of tickers.

###### optionsdata.py

This was the base function that I started with. It navigates to the NASDAQ website and pulls call data from AAPL using Requests and BS4.

## Prerequisitese

Python

Beautiful Soup

CSV reader

## License

This project is licensed under the MIT License - see the LICENSE.md file for details


## Errors

##### Python: 

- [ ] Near Term Error:

> Getting Call data for KO Near 20Term

> Finished Call data for KO Near 20Term

> Getting Put data for KO Near 20Term

> Finished Put data for KO Near 20Term

> Getting Call data for SAM Near 20Term

> Finished Call data for SAM Near 20Term
	
> Getting Put data for SAM Near 20Term

> Finished Put data for SAM Near 20Term


##### VBA: 

- [ ] Blank CSV Error:

> XOM_puts_Nov_2018.csv

> XOM_calls_jan_2020.csv

> TPR_puts_sep_2018.csv

> UAA_puts_jan_2020.csv

