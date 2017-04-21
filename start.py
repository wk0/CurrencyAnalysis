from handle_data import Dataset, make_three_datasets, all_dates, get_list_of_common_dates
import datetime

def main():


	# Based on beginning and end of datasets,
	#	Can be modified based on changed
	start_date = datetime.datetime(year=2011 ,month=9, day=13)
	end_date = datetime.datetime(year=2017, month=3, day=24)

	all_possible_dates = all_dates(start_date, end_date)
	usd, bitcoin, gold = make_three_datasets(all_possible_dates)

	print len(usd.date_list)
	print len(bitcoin.date_list)
	print len(gold.date_list)


if __name__ == "__main__":
	main()