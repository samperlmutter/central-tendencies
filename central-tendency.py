import csv
import statistics

with open('car_data.csv') as csv_file:
    reader = csv.reader(csv_file)
    for cat in reader:
        prices = [int(price[1:].replace(',', ''))
                  for i, row in enumerate(reader)
                  if i is 0
                  for price in row[1:]
                  if price != 'N/A' and price != '']

    mean = statistics.mean(prices)
    median = statistics.median(prices)
    mode = statistics.mode(prices)

    print(f'Mean: {mean}, Median: {median}, Mode: {mode}')
