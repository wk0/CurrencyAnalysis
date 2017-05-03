import datetime

import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from handle_data import make_three_datasets, all_dates

years = mdates.YearLocator()
months = mdates.MonthLocator()
yearsFmt = mdates.DateFormatter('%Y')

def main():

	# First date and Last date for the datasets
	start_date = datetime.datetime(year=2011 ,month=9, day=13)
	end_date = datetime.datetime(year=2017, month=3, day=24)
	max_possible_dates = all_dates(start_date, end_date)

	# You can also acess intervals of data using different time ranges
	#	by just creating a different list of dates using all_dates(start, end)
	usd, bitcoin, gold = make_three_datasets(max_possible_dates)

	plot_date_price(usd, 1, xlabel="Date", ylabel="Broad Index", title='USD')
	plot_date_price(bitcoin, 7, xlabel="Date", ylabel="USD", title='Bitcoin')
	plot_date_price(gold, 1, xlabel="Date", ylabel="USD", title='Gold')



	#with open("goldcleaned.csv", "wb") as f:
	#	writer = csv.writer(f)
	#	writer.writerows(gold.rows)



def plot_date_price(dataset, price_row_index, xlabel, ylabel, title):
	to_date = []
	price = []

	for row in dataset.datetime_rows:
		to_date.append(row[0])
		price.append(row[price_row_index])

	dates = matplotlib.dates.date2num(to_date)

	fig, ax = plt.subplots()
	ax.plot(dates, price)

	ax.xaxis.set_major_locator(years)
	ax.xaxis.set_major_formatter(yearsFmt)
	ax.xaxis.set_minor_locator(months)

	plt.xlabel(xlabel, fontsize=18)
	plt.ylabel(ylabel, fontsize=18)
	plt.title(title, fontsize=24)

	plt.show()


if __name__ == "__main__":
	main()