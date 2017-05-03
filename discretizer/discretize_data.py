import csv

from datetime import datetime
from datetime import timedelta

INTERVALS = {
    "DAY": timedelta(1),
    "WEEK": timedelta(7),
    "MONTH": timedelta(30)
}

BUY =   1
SELL =  -1

BINARY_THRESHOLD = 0

def load_raw_data(path, time_attribute, class_attribute):
    raw_data = dict()

    with open(path) as f:
        f.readline()
        reader = csv.reader(f)

        for line in reader:
            key = datetime.strptime(line[0], '%Y-%m-%d')
            values = [float(l) for l in line[1:-1]]
            raw_data[key] = values

    return raw_data

def load_data(path, time_attribute, class_attribute):
    parsed_data = dict()

    with open(path) as f:
        reader = csv.DictReader(f)

        for row in reader:
            parsed_data[datetime.strptime(row[time_attribute], '%Y-%m-%d')] = float(row[class_attribute])

    return parsed_data


def percent_change(value_1, value_2):
    return ((value_1 - value_2)/value_1)*100


def investor_classification(value_1, value_2):
    if value_1 == 0 or value_2 == 0:
        return "HOLD"

    change = ((value_1 - value_2)/value_1)*100

    if change < SELL:
        return "SELL"

    elif change > BUY:
        return "BUY"

    else:
        return "HOLD"


def binary_classification(value_1, value_2):
    if value_1 == 0 or value_2 == 0:
        return "NEGATIVE"

    change = ((value_1 - value_2)/value_1)*100

    if change > BINARY_THRESHOLD:
        return "POSITIVE"
    else:
        return "NEGATIVE"


def generate_class_labels(data, change_function, interval):
    labels = dict()
    for k, v in sorted(data.items()):
        try:
            labels[k] = change_function(v, data[k+interval])
        except KeyError:
            break

    return labels

if __name__ == "__main__":
    file = "bitcoin_raw.csv"

    time_attribute = "Date"
    class_attribute = "Weighted Price"

    raw = load_raw_data(file, time_attribute, class_attribute)
    parse = load_data(file, time_attribute, class_attribute)

    start_date = datetime(year=2011, month=9, day=13)
    end_date = datetime(year=2017, month=3, day=24)
    interval = timedelta(7)

    # Change the interval
    labels = generate_class_labels(parse, investor_classification, INTERVALS['MONTH'])

    for k, v in labels.items():
        labels[k] = raw[k] + [v]

    fields = ['id', 'open', 'high', 'low', 'close', 'volume (btc)', 'volume (currency)', 'class label']

    # Modify the name for each interval
    with open('bitcoin_monthly.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        row_id = 1

        for k, v in sorted(labels.items()):
            writer.writerow([row_id] + v)
            row_id += 1
