import pandas as pd


CSV_FILE_PATH = './data/pv_yield.csv'
JSON_FILE_PATH = './data/pv_yield.json'


df = pd.read_csv(CSV_FILE_PATH)

df.to_json(JSON_FILE_PATH, orient='records')
