This file descibes the use of the predicter programs.

STEP 1: Download the files from NASDAQ website.
STEP 2: Use the normal "find&replace" function to delete all "$" signs.
STEP 3: Set "company" and "download_date" at the top of stock_try - 2.py. "company" should be the stock code and "downloading_date" should be in form "mmdd"
STEP 4: Run  stock_try - 2.py and get the .h5 model.

STEP 5: Open model_predict.py and set "company" and "download_date" at the top.
STEP 6: Run model_predict.py and get the predicted data in a "-out.csv" file (e.g. AAPL-0415-out.csv)

*Also two plots would be shown when running the two .py programs