import pandas_datareader.data as web
import pandas_datareader as pdr
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
from BlackScholesModel import BlackScholesModel

def process_stocks_data(tickerCode, startDate, endDate):
	# Tunable parameters
	tickerCode = 'TSLA'
	source = 'yahoo'

	df = web.DataReader(tickerCode, source, startDate, endDate)
	df = df.sort_values(by='Date')
	df = df.dropna()

	df = df.assign(Prev = df.Close.shift(1))
	df['Change'] = ((df.Close - df.Prev)/df.Prev)
	return df

def calculate_volatility(df):
	nTradingDays = len(df)
	sigma = np.sqrt(nTradingDays) * df.Change.std()
	return sigma

def calculate_time_to_maturity(day,month,year):
	currDatetime = dt.datetime.now()
	maturityDatetime = dt.datetime(year,month,day)
	timeToMaturity = np.busday_count(currDatetime.date(), maturityDatetime.date())
	tradingDaysPerYear = 252 # normally, sometimes 253 but resulting in negligible difference
	T = timeToMaturity/tradingDaysPerYear
	return T

def main():
	########################################################################################################
	# Tunable parameters
	# The range of stocks data that wants to be retrieved for calculating volatility
	startDate = dt.datetime(2020,10,9)
	endDate = dt.datetime(2021,10,9)
	tickerCode = 'TSLA'
	# The risk-free interest rate used is the 10-Years U.S. Treasury Yield at 8th Oct 2021 which is 1.613%
	# Obtained from: https://www.marketwatch.com/investing/bond/tmubmusd10y?countrycode=bx
	r = 0.01613
	# The spot price used is the current stock's closing price
	# Find the value at finance.yahoo.com.
	# The value used is TSLA closing price on 8th Oct 2021.
	s = 785.49
	# This is the maturity date
	day = 5
	month = 11
	year = 2021
	# This is the options dataset filename
	optionsFilename = "TSLA-20211105-calls.csv"
	# This is the end of the tunable parameters. No need to change anything starting from this line.
	########################################################################################################

	df = process_stocks_data(tickerCode, startDate, endDate)
	sigma = calculate_volatility(df)
	T = calculate_time_to_maturity(day,month,year)

	# Open the options csv file obtained from options_price_retriever.py
	optionsdf = pd.read_csv(optionsFilename)
	optionsdf = optionsdf.loc[:,"contractSymbol":"ask"]
	strikePrices = optionsdf.strike.tolist()
	callPrices = [BlackScholesModel(s,K,T,r,sigma).callPrice() for K in strikePrices]
	optionsdf['blackScholesPrice'] = callPrices

	optionsdf['difference'] = ((optionsdf.blackScholesPrice - optionsdf.ask)/(optionsdf.blackScholesPrice))*100

	plt.figure()
	ax = sns.distplot(optionsdf.iloc[:50].difference)

	# Examine the distribution
	std = df.Change.std()
	samples = np.random.normal(df.Change.mean() ,std, size=1000000)
	fig, ax = plt.subplots()
	ax = sns.kdeplot(data=df.Change.dropna(), label='Empirical', ax=ax,shade=True)
	ax = sns.kdeplot(data=samples, label='Sampling', ax=ax,shade=True)
	
	plt.xlabel('Change in Stock Price')
	plt.ylabel('Density')
	plt.legend()
	plt.show()
	return

if __name__ == '__main__':
	main()