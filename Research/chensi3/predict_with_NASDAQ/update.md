This file is created to descirbe my process of self-learning modeling and ML.

Update 03/25/2021:
1. After reading through the ML modeling tutorial, I think the most proper model for stocks is neural network.
In specific, the LSTM model, as presented by the stock_ML tutorial, is the best for stock modeling.

2. The best way for us to find and collect stock price data is by directly downloading from NASDAQ website.
Take Apple Co. (stock code AAPL in NASDAQ) as an example: 
the historical data is given by https://www.nasdaq.com/market-activity/stocks/aapl/historical
When we download the .csv file, we only need to remove all "$" signs to get a pure dataset of five years.
Then using pandas, we can collect the closing price every day under the "Close/Last" tag.

3. I tried modifying the parameters in the stock_try.py to best fit the predicted curve to the real curve.
Then I imported Starbucks's and Baidu's five-year data to test if the model is preciser than before.
The result is true, but I still need to explore the functions of these parameters and their impact on modeling precisity.

