import requests
import csv
import json

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=5min&outputsize=full&apikey=NMA67JBGVAXFK6SH'
r = requests.get(url)
data = r.json()

# Create a CSV file called "results.csv"
with open('results.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(data.keys())
    writer.writerows(data.values())

print("CSV file created: results.csv")

# Create a JSON file called "results.json"
with open('results.json', 'w') as json_file:
    json.dump(data, json_file)

print("JSON file created: results.json")
