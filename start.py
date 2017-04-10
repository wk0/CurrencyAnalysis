from handle_data import Dataset, make_three_datasets
import datetime

def main():
	usd, bitcoin, gold = make_three_datasets()

	# Based on beginning and end of datasets,
	#	Can be modified based on changed
	start_date = datetime.datetime(year=2011 ,month=9, day=13)
	end_date = datetime.datetime(year=2017, month=3, day=24)




if __name__ == "__main__":
	main()