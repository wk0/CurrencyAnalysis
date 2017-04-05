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

def test():
	print 'Running tests for {0}, {1}, and {2}...'.format(dollar_file_name, bitcoin_file_name, gold_file_name)
	print ''

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

	# -----

	usd = Dataset(usd_data)
	usd.process_lists()

	print 'USD Object Access'
	print usd.access_by_date['2017-03-23']
	print usd.access_by_date['2017-03-22']
	print ''

	bitcoin = Dataset(bitcoin_data)
	bitcoin.process_lists()

	print 'Bitcoin Object Access'
	print bitcoin.access_by_date['2017-03-23']
	print bitcoin.access_by_date['2017-03-22']
	print ''

	gold = Dataset(gold_data)
	gold.process_lists()

	print 'Gold Object Access'
	print gold.access_by_date['2017-03-23']
	print gold.access_by_date['2017-03-22']
	print ''

def make_three_datasets():
	dollar_data = read_input_file(dollar_file_name)
	usd = Dataset(dollar_data)
	usd.process_lists()

	bitcoin_data = read_input_file(bitcoin_file_name)
	bitcoin = Dataset(bitcoin_data)
	bitcoin.process_lists()

	gold_data = read_input_file(gold_file_name)
	gold = Dataset(gold_data)
	gold.process_lists()

	return usd, bitcoin, gold


def read_input_file(file):
	lines = open(file).read().split('\n')

	lists = []
	#print len(lines)
	for line in lines:
		lists.append(line.split(','))

	# empty list at end
	lists.pop()

	return lists


class Dataset:
	# USD
	# ['Date', 'Value']
	# ['2017-03-24', '124.1911']

	# Gold
	# ['Date', 'USD (AM)', 'USD (PM)', 'GBP (AM)', 'GBP (PM)', 'EURO (AM)', 'EURO (PM)']
	# ['2017-03-24', '1244.0', '1247.5', '996.2', '999.62', '1150.82', '1155.31']

	# Bitcoin
	# ['Date', 'Open', 'High', 'Low', 'Close', 'Volume (BTC)', 'Volume (Currency)', 'Weighted Price']
	# ['2017-03-24', '1030.84', '1032.0', '920.0', '929.06', '16072.4170833', '15697051.6813', '976.645367026']

	def __init__(self, rows):
		self.rows = rows
		self.labels = rows[0]

	def process_lists(self):
		by_date = {}

		for row in self.rows:
			r = {}
			# Uses the index labels to create the dictionary
			for index in range(0,len(self.labels)):
				r[self.labels[index]] = row[index]

			by_date[row[0]] = r

		self.access_by_date = by_date




if __name__ == "__main__":
	test()