# Options Data

This is a repo of Python 3 programs that use requests and beautiful soup to navigate to the NASDAQ website and scrape option data into CSVs.

Both <a href="https://github.com/santarini/options-data/blob/master/optionsFull.py">optionsFull.py</a> and <a href="https://github.com/santarini/options-data/blob/master/optionsFullMass.py">optionsFullMass.py</a> are independent fully working programs. 

# Contents

###### optiondates.py

This was the second step in the algo, it goes to the NASDAQ website figures out what expiry dates are available for option contracts of your specified ticker.

###### optionsFull.py

This is the first full working version. It finds call, put or both pricing data for a <u>single</u> ticker at a time.

###### optionsFullMass.py

This is the first full mass working version. Whereas <a href="https://github.com/santarini/options-data/blob/master/optionsFull.py">optionsFull.py</a> finds option data for a single ticker and prompts you ever step of the way, <a href="https://github.com/santarini/options-data/blob/master/optionsFullMass.py">optionsFullMass.py</a> can take in several tickers and gives you the option data for all available dates. It was intended to be used for a greater number of tickers.

###### optionsdata.py

This was the base function that I started with. It navigates to the NASDAQ website and pulls call data from AAPL using Requests and BS4.

## Prerequisitese

Python

Beautiful Soup

CSV reader

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
