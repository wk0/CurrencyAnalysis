import datetime

from handle_data import make_three_datasets


def main():
	start_date = datetime.datetime(year=2011 ,month=9, day=13)
	end_date = datetime.datetime(year=2017, month=3, day=24)

	list_of_all_possible_dates = all_dates(start_date, end_date)
	usd, bitcoin, gold = make_three_datasets(list_of_all_possible_dates)

	#print_date_summary(usd, bitcoin, gold, len(list_of_all_possible_dates), start_date, end_date)


	common_dates = get_list_of_common_dates(list_of_all_possible_dates, usd, bitcoin, gold)

	#print len(list_of_all_possible_dates)


def get_list_of_common_dates(list_of_all_possible_dates, usd, bitcoin, gold):
	set_of_all_possible_dates = set(list_of_all_possible_dates)

	set_of_all_three_dates = set_of_all_possible_dates.intersection(usd.date_set)
	set_of_all_three_dates = set_of_all_three_dates.intersection(bitcoin.date_set)
	set_of_all_three_dates = set_of_all_three_dates.intersection(gold.date_set)

	#print len(set_of_all_three_dates), 'dates in all three'
	return set_of_all_three_dates


def print_date_summary(usd, bitcoin, gold, date_range, start_date, end_date):
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

	get_unique_dates(usd, gold)
	get_unique_dates(usd, bitcoin)
	get_unique_dates(gold, bitcoin)

def get_unique_dates(one, two):
	one_set = one.date_set
	two_set = two.date_set

	missing_one = two_set - one_set
	missing_two = one_set - two_set

	dates_not_in_both = list(missing_one) + list(missing_two)
	#print dates_not_in_both
	print len(dates_not_in_both),'dates not in both', one.name, 'and', two.name



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

	list_of_all_possible_dates = []
	current_date = start_date
	delta = datetime.timedelta(days=1)

	while current_date < end_date:
		current_only_date = current_date.date()
		date_string = current_only_date.strftime('%Y-%m-%d')
		list_of_all_possible_dates.append(date_string)

		current_date += delta

	return list_of_all_possible_dates


if __name__ == "__main__":
	main()