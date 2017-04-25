import csv
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt


def load_data(path):
    """Function that handles reading in data. Assumes the first row is a date
    and every other column is a numerical feature.
    :param path: Location of CSV file
    :return: Dictionary mapping dates to features
    """
    parsed_data = dict()

    with open(path) as f:
        f.readline()
        reader = csv.reader(f)

        for line in reader:
            key = datetime.strptime(line[0], '%Y-%m-%d')
            values = [float(l) for l in line[1:]]
            parsed_data[key] = values

    return parsed_data


def percent_change(value_1, value_2):
    if value_1 == 0 or value_2 == 0:
        return "negative"

    change = ((value_1 - value_2)/value_1)*100


    if change > 0: 
        return 'positive'
    else:
        return 'negative'


def generate_class_labels(data, start, end, interval):
    day = timedelta(1)


    fields = ['id', 'open', 'high', 'low', 'close', 'volume (btc)', 'volume (currency)', 'class label']

    with open('results-1week.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        row_id = 1

        while True:
            current_date = start

            starting_value = data[current_date][-1]

            try:
                ending_value = data[current_date+interval][-1]
            except KeyError:
                break

            row = [row_id] + data[current_date][0:-1] + [percent_change(starting_value, ending_value)]

            writer.writerow(row)
            start += day
            row_id += 1

            if start >= end:
                break



if __name__ == "__main__":
    file = "BCHARTS-BITSTAMPUSD.csv"

    data = load_data(file)
    start_date = datetime(year=2011, month=9, day=13)
    end_date = datetime(year=2017, month=3, day=24)
    interval = timedelta(7)

    generate_class_labels(data, start_date, end_date, interval)
