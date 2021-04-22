#import libraries
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
#%matplotlib inline (we are not using jupyter notebook)

from matplotlib.pylab import rcParams
rcParams['figure.figsize']=20,10
from keras.models import Sequential
from keras.models import load_model
from keras.layers import LSTM,Dropout,Dense

from sklearn.preprocessing import MinMaxScaler

# Please enter COMPANY and DATE HERE

company = "FB"
download_date = "0415"



url = "F:\\CS196_project\\Group13-SP21\\Project\\Backend\Model\\"+company+"-"+download_date+".csv"
df=pd.read_csv(url)
df.head()

#display the data with a graph
df["Date"]=pd.to_datetime(df.Date,format="%m/%d/%Y")
df.index=df['Date']
plt.figure(figsize=(16,8))
l1 = plt.plot(df["Close/Last"],label='Close Price history')

#separate the "date" and "close_price" out of the dataset
data=df.sort_index(ascending=True,axis=0)
new_dataset=pd.DataFrame(index=range(0,len(df)),columns=['Date','Close'])
for i in range(0,len(data)):
    new_dataset["Date"][i]=data['Date'][i]
    new_dataset["Close"][i]=data["Close/Last"][i]

lstm_model = load_model("AAPL-0415.h5")
scaler=MinMaxScaler(feature_range=(0,1))

raw_future = new_dataset["Close"][1138:].astype(float)

future = np.ones((120,1))
future[:,0] = raw_future
#print(future.shape)

for i in range(30):
    print("Log: Get day NO."+str(i)+" successful.")
    #future = np.ones((50,1))
    #future[:,0] = raw_future

    norm_future = scaler.fit_transform(future)
    norm_future = np.reshape(norm_future,(1,120,1))
    predicted_future = lstm_model.predict(norm_future)
    predicted_future=scaler.inverse_transform(predicted_future)

    future[0:119,0] = future[1:,0]
    future[119,0] = predicted_future
    raw_future=future

#print(future.shape)
#future contains the predicted data in the next 30 days

date = "2021-" + download_date[:2] + "-" + download_date[2:]
date = pd.to_datetime(date,format="%Y-%m-%d")

predicted= pd.DataFrame(index=range(30),columns=['Date','Predicted'])
predicted['Date'] = pd.date_range(start=date,periods=30,freq='D')
predicted['Predicted'] = future[90:,0]


url = "F:\\CS196_project\\Group13-SP21\\Project\\Backend\Model\\"+company+"-"+download_date+"-out.csv"
predicted.to_csv(url)

#p=np.array(30,2)
l2 = plt.plot(predicted['Date'],predicted["Predicted"])
plt.legend(labels = ["Real Data (5 years)","Predicted Data (30 days)"])

plt.show()