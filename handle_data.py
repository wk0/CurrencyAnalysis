import quandl
import csv
import datetime

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

	print 'USD Object Access'
	print usd.access_by_date['2017-03-23']
	print usd.access_by_date['2017-03-22']
	print ''

	bitcoin = Dataset(bitcoin_data)

	print 'Bitcoin Object Access'
	print bitcoin.access_by_date['2017-03-23']
	print bitcoin.access_by_date['2017-03-22']
	print ''

	gold = Dataset(gold_data)

	print 'Gold Object Access'
	print gold.access_by_date['2017-03-23']
	print gold.access_by_date['2017-03-22']
	print ''

def make_three_datasets(all_possible_dates):
	dollar_data = read_input_file(dollar_file_name)
	usd = Dataset(dollar_data, 'usd')

	bitcoin_data = read_input_file(bitcoin_file_name)
	bitcoin = Dataset(bitcoin_data, 'bitcoin')
	bitcoin = clean_bitcoin(bitcoin)


	gold_data = read_input_file(gold_file_name)
	gold = Dataset(gold_data, 'gold')

	set_of_all_three_dates = get_list_of_common_dates(all_possible_dates, usd, bitcoin, gold)
	all_three_list = list(set_of_all_three_dates)



	pop_unique_dates(usd, all_three_list)
	pop_unique_dates(usd, all_three_list)

	pop_unique_dates(bitcoin, all_three_list)
	pop_unique_dates(bitcoin, all_three_list)
	pop_unique_dates(bitcoin, all_three_list)

	pop_unique_dates(gold, all_three_list)
	pop_unique_dates(gold, all_three_list)


	usd.access_by_date = usd.process_lists()
	usd.date_list = usd.get_list_of_dates()
	usd.date_set = set(usd.date_list)

	bitcoin.access_by_date = bitcoin.process_lists()
	bitcoin.date_list = bitcoin.get_list_of_dates()
	bitcoin.date_set = set(bitcoin.date_list)

	gold.access_by_date = gold.process_lists()
	gold.date_list = gold.get_list_of_dates()
	gold.date_set = set(gold.date_list)




	# must be the same number of dates for each
	assert(len(usd.rows) == len(bitcoin.rows) == len(gold.rows) == len(set_of_all_three_dates))

	return usd, bitcoin, gold


def pop_unique_dates(dataset, all_three_list):
	dataset_before = len(dataset.rows)
	index = 0
	for row in dataset.rows:
		#print row
		if row[0] not in all_three_list:
			dataset.rows.pop(index)
			#print row[0], 'not in all dates'
		index += 1

	dataset_after = len(dataset.rows)
	#print dataset_before - dataset_after, 'dates removed from', dataset.name


def read_input_file(file):
	lines = open(file).read().split('\n')

	lists = []
	#print len(lines)
	for line in lines:
		lists.append(line.split(','))

	# empty list at end
	lists.pop()

	return lists

def clean_bitcoin(bitcoin):
	#print 'clean bitcoin'
	index = 0
	for row in bitcoin.rows:
		#print row
		if row[1] == '0.0' and row[2] == '0.0' and row[3] == '0.0' and row[4] == '0.0' and row[5] == '0.0' and row[6] == '0.0' and row[7] == '0.0':
			bitcoin.rows.pop(index)
			#print 'popped 0'
		index += 1

	bitcoin.access_by_date = bitcoin.process_lists()
	bitcoin.date_list = bitcoin.get_list_of_dates()
	bitcoin.date_set = set(bitcoin.date_list)

	return bitcoin


def get_list_of_common_dates(list_of_all_possible_dates, usd, bitcoin, gold):
	set_of_all_possible_dates = set(list_of_all_possible_dates)

	set_of_all_three_dates = set_of_all_possible_dates.intersection(usd.date_set)
	set_of_all_three_dates = set_of_all_three_dates.intersection(bitcoin.date_set)
	set_of_all_three_dates = set_of_all_three_dates.intersection(gold.date_set)

	#print len(set_of_all_three_dates), 'dates in all three'
	return set_of_all_three_dates


def all_dates(start_date, end_date):

	list_of_all_possible_dates = []
	current_date = start_date
	delta = datetime.timedelta(days=1)

	while current_date < end_date:
		current_only_date = current_date.date()
		date_string = current_only_date.strftime('%Y-%m-%d')
		list_of_all_possible_dates.append(date_string)

		current_date += delta

	return list_of_all_possible_dates



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

	def __init__(self, rows, name):
		self.name = name
		self.rows = rows
		self.labels = rows[0]
		self.access_by_date = self.process_lists()
		self.date_list = self.get_list_of_dates()
		self.date_set = set(self.date_list)

	def process_lists(self):
		by_date = {}

		for row in self.rows:
			r = {}
			# Uses the index labels to create the dictionary
			for index in range(0,len(self.labels)):
				r[self.labels[index]] = row[index]

			by_date[row[0]] = r

		return by_date

	def get_list_of_dates(self):
		dates = []

		dates = self.access_by_date.keys()

		if len(dates) != len(set(dates)):
			raise ValueError('Dates not unique within dataset')

		return dates





if __name__ == "__main__":
	test()