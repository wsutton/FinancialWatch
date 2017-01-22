#Pull_Data
import quandl as qdl
import pandas as pd 
import Config as cfg
import sys
import datetime
from datetime import date, timedelta
import pdb  

def main():
	''' Ticker list is pulled from command line
	 	Ex. python Pull_QDL_Data.py EUR/USD USD/JPY AUD/USD 
	 	returns closing data for these ticker symbols '''
	
	ticker_list = str(sys.argv[1:])
	ticker_data = get_data(ticker_list, cfg.ticker_dictionary(), cfg.num_days, cfg.most_recent_date, cfg.auth_tok)
	if cfg.convert_returns == True:
		returns_data = convert_returns(ticker_data)
	print returns_data
	return returns_data

def get_data(ticker_list, ticker_dictionary, num_days, end_date, api_key):
	# Pull Data from Quandl
	#Specify beginning row
	start_date = end_date - timedelta(num_days)
	#Initialize data table
	data_table = None 
	#Iterate through ticker categories
	for category, category_dict in ticker_dictionary.iteritems():
		#Iterate through ticker names and corresponding QDL codes
		for ticker_name, ticker_code in category_dict.iteritems():
			#If name in ticker list, join to current build
			if ticker_name in ticker_list:
				current_column = qdl.get(ticker_code, start_date = start_date, end_date = end_date, authtoken = api_key)
				# Rename columns to Ticker_Close
				current_column.columns = [ticker_name + '_Close']
				#If first column in table, data table is current column
				if data_table is None:
					data_table = current_column
				#Otherwise, inner join on Datetime index
				else:
					data_table = data_table.join(current_column, how = 'left', rsuffix = '')
	return data_table 


def convert_returns(data_table, periods = 1):
	#Convert price action to percent return
	data_table = data_table.pct_change(periods = 1).dropna() * 100
	return data_table 

if __name__ == "__main__":
	main()