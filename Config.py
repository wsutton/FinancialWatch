#config settings
import datetime
from datetime import date, timedelta 

#Quandl API key
auth_tok = "kz_8e2T7QchJBQ8z_VSi"
#Rows of data to pull from Quandl
num_days = 500
#Pull data up to this date
most_recent_date = datetime.date.today()
#Convert price values to returns (Bool)
convert_returns = True 

def ticker_dictionary():
	ticker_dict = {
					'FX': {'USD/MXN': 'CURRFX/MXNUSD.1', 'USD/CAD': 'CURRFX/USDCAD.1', 'NZD/USD': 'CURRFX/NZDUSD.1', 'USD/JPY': 'CURRFX/USDJPY.1',
							'GBP/USD': 'CURRFX/GBPUSD.1', 'USD/ZAR': 'CURRFX/USDZAR.1', 'AUD/USD': 'CURRFX/AUDUSD.1', 'EUR/USD': 'CURRFX/EURUSD.1'
							},
					'STOCKS': {		
								},
					'COMMODITIES': {
									},
					'ETFs': {
							 }
	
					}
	return ticker_dict 
