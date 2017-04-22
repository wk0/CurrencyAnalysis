from handle_data import Dataset, make_three_datasets, all_dates, get_list_of_common_dates
import datetime
import matplotlib
import matplotlib.pyplot as plt

def main():

	# First date and Last date for the datasets
	start_date = datetime.datetime(year=2011 ,month=9, day=13)
	end_date = datetime.datetime(year=2017, month=3, day=24)
	max_possible_dates = all_dates(start_date, end_date)

	# You can also acess intervals of data using different time ranges
	#	by just creating a different list of dates using all_dates(start, end)

	usd, bitcoin, gold = make_three_datasets(max_possible_dates)

	plot_date_price(usd, 1)
	plot_date_price(bitcoin, 7)
	plot_date_price(gold, 1)


def plot_date_price(dataset, price_row_index):
	to_date = []
	price = []

	for row in dataset.datetime_rows:
		#print row
		to_date.append(row[0])
		price.append(row[price_row_index])

	dates = matplotlib.dates.date2num(to_date)

	plt.plot(dates, price)
	plt.show()


if __name__ == "__main__":
	main()