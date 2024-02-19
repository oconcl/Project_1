from dotenv import load_dotenv
import os
import requests
import csv
import json
import pandas as pd

# load the .env file
load_dotenv('alpha_vantage.env')

# Correctly set up the URL for TIME_SERIES_DAILY
API_KEY = os.getenv('API_KEY') 
SYMBOL = 'TSLA'
FUNCTION = 'TIME_SERIES_DAILY'
OUTPUT_SIZE = 'full'
BASE_URL = os.getenv('BASE_URL')

url = f"{BASE_URL}?function={FUNCTION}&symbol={SYMBOL}&outputsize={OUTPUT_SIZE}&apikey={API_KEY}"

# fetch the data
response = requests.get(url)
data = response.json()

time_series_key = None

for key in data.keys():
    if 'Time Series' in key:
        time_series_key = key
        break

if time_series_key is None:
    print("No time series data found")
else:
    time_series_data = data[time_series_key]
    df = pd.DataFrame.from_dict(time_series_data, orient='index').reset_index()
    df.columns = ['Date'] + [col[3:] for col in df.columns[1:]]

    df['Date'] = pd.to_datetime(df['Date'])
    numeric_columns = df.columns.drop('Date')
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')


    # Save to CSV
    df.to_csv('results.csv', index=False)
    print("CSV file created: results.csv")

    # Save to JSON
    df.to_json('results.json', orient='records', date_format='iso')
    print("JSON file created: results.json")