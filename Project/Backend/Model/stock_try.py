#import libraries
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
#%matplotlib inline (we are not using jupyter notebook)

from matplotlib.pylab import rcParams
rcParams['figure.figsize']=20,10
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense

from sklearn.preprocessing import MinMaxScaler

#read the data from NASDAQ Apple data.csv using pandas
url = "F:\\CS196_project\\Group13-SP21\\Project\\Backend\Model\\AAPL-0415.csv"
df=pd.read_csv(url)
df.head()

#display the data with a graph
df["Date"]=pd.to_datetime(df.Date,format="%m/%d/%Y")
df.index=df['Date']
plt.figure(figsize=(16,8))
plt.plot(df["Close/Last"],label='Close Price history')

#separate the "date" and "close_price" out of the dataset
data=df.sort_index(ascending=True,axis=0)
new_dataset=pd.DataFrame(index=range(0,len(df)),columns=['Date','Close'])
for i in range(0,len(data)):
    new_dataset["Date"][i]=data['Date'][i]
    new_dataset["Close"][i]=data["Close/Last"][i]

#normaliz the new dataset (so it would be more comparable)
new_dataset.index=new_dataset.Date
new_dataset.drop("Date",axis=1,inplace=True)

final_dataset=new_dataset.values

train_data=final_dataset[0:1008,:]
valid_data=final_dataset[1008:,:]

scaler=MinMaxScaler(feature_range=(0,1))
scaled_data=scaler.fit_transform(final_dataset)

x_train_data,y_train_data=[],[]
for i in range(50,len(train_data)):
    x_train_data.append(scaled_data[i-50:i,0])
    y_train_data.append(scaled_data[i,0])
    
x_train_data,y_train_data=np.array(x_train_data),np.array(y_train_data)
x_train_data=np.reshape(x_train_data,(x_train_data.shape[0],x_train_data.shape[1],1))

standard = 1000
flag = False
for i in range(20):
    #Use LSTM to train the model
    lstm_model=Sequential()
    lstm_model.add(LSTM(units=80,return_sequences=True,input_shape=(x_train_data.shape[1],1)))
    lstm_model.add(LSTM(units=80))
    lstm_model.add(Dense(1))
    inputs_data=new_dataset[len(new_dataset)-len(valid_data)-50:].values
    inputs_data=inputs_data.reshape(-1,1)
    inputs_data=scaler.transform(inputs_data)
    lstm_model.compile(loss='mean_squared_error',optimizer='adam')
    lstm_model.fit(x_train_data,y_train_data,epochs=1,batch_size=1,verbose=2)

    #make a check on whether the model is accurate
    X_test=[]
    for i in range(50,inputs_data.shape[0]):
        X_test.append(inputs_data[i-50:i,0])
    X_test=np.array(X_test)
    X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
    predicted_closing_price=lstm_model.predict(X_test)
    predicted_closing_price=scaler.inverse_transform(predicted_closing_price)

    #show the predicted data on a graph
    train_data=new_dataset[:1008]
    valid_data=new_dataset[1008:]
    valid_data['Predictions']=predicted_closing_price

    diff = 0
    for j in range(len(valid_data)):
        close = valid_data["Close"][j]
        pre = valid_data["Predictions"][j]
        diff = diff + (close - pre)**2
    if diff < standard:
        standard = diff
        flag = True
        #save the model
        plt.clf()
        lstm_model.save("AAPL-0415.h5")
        plt.plot(train_data["Close"])
        plt.plot(valid_data[['Close',"Predictions"]])
        plt.title(str(i))
    
if flag == False:
    #plt.plot(train_data["Close"])
    plt.plot(valid_data[['Close',"Predictions"]])









plt.show()