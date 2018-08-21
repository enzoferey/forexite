# forexite

Download historical data from [Forexite](https://www.forexite.com/).

## Usage

`python main.py [stock_name] [start_month] [start_year] [[end_month] [end_year]]`

**Single month example:**

`python main.py EURUSD 1 2018` (EURUSD stock in January 2018)

**Interval example:**

`python main.py EURUSD 11 2017 3 2018` (EURUSD stock in from November 2017 to March 2018)

> Months in intervals are inclusive, in this last example March 2018 would be included in the data
