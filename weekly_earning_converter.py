import json
import csv

with open('weekly_earnings.json') as json_file:
    data = json.load(json_file)

data_file = open('weekly_earnings.csv', 'w')
csv_writer =csv.writer(data_file)

columns = data['meta']['view']['columns']

header = []
for col in columns:
    header.append(col['name'])

csv_writer.writerow(header)

for line in data['data']:
    csv_writer.writerow(line)

data_file.close()