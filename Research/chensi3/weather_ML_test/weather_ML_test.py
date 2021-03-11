from pandas import read_csv
from datetime import datetime


def parse(x):
    return datetime.strptime(x, '%Y %m %d %H')

url = "F:\\CS196_project\\Group13-SP21\\Research\\chensi3\\weather_ML_test\\raw_data.csv"
dataset = read_csv(url,  parse_dates = [['year', 'month', 'day', 'hour']], index_col=0, date_parser=parse)
dataset.drop('No', axis=1, inplace=True)

# manually specify column names
dataset.columns = ['pollution', 'dew', 'temp', 'press', 'wnd_dir', 'wnd_spd', 'snow', 'rain']
dataset.index.name = 'date'
# mark all NA values with 0
dataset['pollution'].fillna(0, inplace=True)
# drop the first 24 hours
dataset = dataset[24:]
# summarize first 5 rows
print(dataset.head(5))
# save to file
new_url = "F:\\CS196_project\\Group13-SP21\\Research\\chensi3\\weather_ML_test\\new_pollution.csv"
dataset.to_csv(new_url)