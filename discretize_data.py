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
        return "NaN"

    return ((value_1 - value_2)/value_1)*100


def generate_class_labels(data, start, end, interval):
    class_labels = dict()
    while True:
        starting_value = data[start][-1]
        try:
            ending_value = data[start+interval][-1]
        except KeyError:
            break

        class_labels[start] = percent_change(starting_value, ending_value)

        start += interval

        if start == end:
            break

    x = []
    y = []

   #with open("results.txt", "w") as f:
    for key in sorted(class_labels.keys(), reverse=True):
        x.append(key)
        value = class_labels[key]
        if value == 'NaN':
            y.append(0)
        else:
            y.append(value)
            #f.write("%s, %s \n" %(key, class_labels[key]))

    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    file = "BCHARTS-BITSTAMPUSD.csv"

    data = load_data(file)
    start_date = datetime(year=2011, month=9, day=13)
    end_date = datetime(year=2017, month=3, day=24)
    interval = timedelta(30)
    generate_class_labels(data, start_date, end_date, interval)
