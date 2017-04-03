import quandl
import csv


"""
	Imports the data from the quandl API, though it may
	be better for us to 'own' the data and just store it
	as a .csv in the repo. Though this should update day
	to day

# Get api key @ quandl.com under account settings
api_key = ""

#https://www.quandl.com/data/FED/JRXWTFB_N_B-Nominal-Broad-Dollar-Index-Business-day
print 'Getting USD...'
nom_broad_dollar_index = quandl.get("FED/JRXWTFB_N_B", authtoken=api_key)

print 'Getting Bitcoin...'
#https://www.quandl.com/data/BCHARTS/BITSTAMPUSD-Bitcoin-Markets-bitstampUSD
bitcoin_usd_index = quandl.get("BCHARTS/BITSTAMPUSD", authtoken=api_key)

print 'Getting Gold...'
#https://www.quandl.com/data/LBMA/GOLD-Gold-Price-London-Fixing
gold_usd = quandl.get("LBMA/GOLD", start_date="2001-12-31", end_date="2005-12-31", authtoken=api_key)

print 'Done loading data from API'

"""

dollar_file_name = 'FED-JRXWTFB_N_B.csv'
bitcoin_file_name = 'BCHARTS-BITSTAMPUSD.csv'
gold_file_name = 'LBMA-GOLD.csv'

def main():
	usd_data = read_input_file(dollar_file_name)
	print 'USD Sample'
	print usd_data[0]
	print usd_data[1]
	print ''

	bitcoin_data = read_input_file(bitcoin_file_name)
	print 'Bitcoin Sample'
	print bitcoin_data[0]
	print bitcoin_data[1]
	print ''

	gold_data = read_input_file(gold_file_name)
	print 'Gold Sample'
	print gold_data[0]
	print gold_data[1]
	print ''


def read_input_file(file):
	lines = open(file).read().split('\n')

	lists = []
	#print len(lines)
	for line in lines:
		lists.append(line.split(','))

	return lists



if __name__ == "__main__":
	main()