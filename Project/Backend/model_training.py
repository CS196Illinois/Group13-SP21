from get_stock_data import get_stock_data, plot_graph, get_final_df, predict
import pandas as pd
import matplotlib.pyplot as plt
import os

def model_training(stock):
    data = get_stock_data(stock)
    data.drop(['denominator', 'splitRatio','type','data', 'numerator'], axis = 1, inplace=True)
    plt.figure(figsize=(10,10))
    data['date'] = pd.to_datetime(data['date'],unit='s')
    data.set_index('date', inplace= True)
    print(data.head())
    plt.plot(data.index, data['close'])
    plt.xlabel("date")
    plt.ylabel("$ price")
    plt.title("DIS Stock Price 1/05/2020 - 1/05/2021")
    plt.savefig(r"C:\Users\ayush\OneDrive\Documents\Projects\cs196\project\plots" + '/plot.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_model(sequence_length, n_features, units=256, cell=LSTM, n_layers=2, dropout=0.3,
                loss="mean_absolute_error", optimizer="rmsprop", bidirectional=False):
    model = Sequential()
    for i in range(n_layers):
        if i == 0:
            # first layer
            if bidirectional:
                model.add(Bidirectional(cell(units, return_sequences=True), batch_input_shape=(None, sequence_length, n_features)))
            else:
                model.add(cell(units, return_sequences=True, batch_input_shape=(None, sequence_length, n_features)))
        elif i == n_layers - 1:
            # last layer
            if bidirectional:
                model.add(Bidirectional(cell(units, return_sequences=False)))
            else:
                model.add(cell(units, return_sequences=False))
        else:
            # hidden layers
            if bidirectional:
                model.add(Bidirectional(cell(units, return_sequences=True)))
            else:
                model.add(cell(units, return_sequences=True))
        # add dropout after each layer
        model.add(Dropout(dropout))
    model.add(Dense(1, activation="linear"))
    model.compile(loss=loss, metrics=["mean_absolute_error"], optimizer=optimizer)
    return model