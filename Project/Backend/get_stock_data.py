import requests
import pandas as pd
import json

def get_stock_data(stock):

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

    querystring = {"symbol":{stock},"region":"US"}

    headers = {
        'x-rapidapi-key': "89ea28b151msheaa21d67c3f5434p10204ejsn235298fd67de",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    content = json.loads(response.text)
    return pd.DataFrame(content['prices'])



