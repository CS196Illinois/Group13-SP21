from flask import Flask, render_template, request
import requests
from get_result import get_result
from get_stock_data import get_stock_data
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/services', methods =['GET', 'POST'])
def services():
    if (request.method == 'POST'):
        stock = requests.args['stock']
        return redirect(url_for('stocks', stock = stock))
    else:
        return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/stocks', methods=['POST','GET'])
def stocks():
    if request.method == 'POST' :
        stock = request.form['stock']
        future_price, loss, total_buy_profit, total_sell_profit, total_profit, total_per_trade, pa = get_result(stock)
        return render_template('stocks.html', stock = stock, path = pa)

