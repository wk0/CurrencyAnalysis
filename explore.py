from handle_data import Dataset, make_three_datasets
import datetime


def main():
	usd, bitcoin, gold = make_three_datasets()

	start_date = datetime.datetime(year=2011 ,month=9, day=13)
	end_date = datetime.datetime(year=2017, month=3, day=24)

	date_range = all_dates(start_date, end_date)
	print date_range, 'days between', start_date.date(), 'and', end_date.date()
	print ''

	print 'USD dates'
	usd_valid_dates = date_iterate_dataset(start_date, end_date, usd)
	print ''

	# Bitcoin doesn't seem to have breaks on the weekend or
	#	holidays like USD and Gold, but it does have some
	#	days that have 0.0 for all values.
	print 'Bitcoin dates'
	bitcoin_valid_dates = date_iterate_dataset(start_date, end_date, bitcoin)
	print ''

	print 'Gold dates'
	gold_valid_dates = date_iterate_dataset(start_date, end_date, gold)
	print ''

	# Need to figure out what dates are not the same
	if all(x in usd_valid_dates for x in gold_valid_dates):
		print 'All dates between USD and Gold are equal'

def date_iterate_dataset(start_date, end_date, dataset):
	valid_count = 0
	missing_key = 0

	valid_dates = []

	d = start_date
	delta = datetime.timedelta(days=1)
	while d <= end_date:
		d += delta

		try:
			datekey = dataset.access_by_date[str(d.date())]
			valid_dates.append(datekey)
			valid_count += 1

		except KeyError, e:
			#print e
			missing_key += 1

	print 'valid_count', valid_count
	print 'missing_key', missing_key

	return valid_dates



def all_dates(start_date, end_date):
	count = 0

	d = start_date
	delta = datetime.timedelta(days=1)
	while d <= end_date:
		d += delta
		count += 1

	return count



if __name__ == "__main__":
	main()