#import and modify the raw data
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
# save to "new_pollution.csv"
new_url = "F:\\CS196_project\\Group13-SP21\\Research\\chensi3\\weather_ML_test\\new_pollution.csv"
dataset.to_csv(new_url)



#import new data and show them in a  graph
import matplotlib.pyplot as plt
# load dataset
dataset = read_csv(new_url, header=0, index_col=0)
values = dataset.values
# specify columns to plot
groups = [0, 1, 2, 3, 5, 6, 7]
i = 1
# plot each column
plt.figure()
for group in groups:
    plt.subplot(len(groups), 1, i)
    plt.plot(values[:, group])
    plt.title(dataset.columns[group], y=0.5, loc='right')
    i += 1
plt.show()


#