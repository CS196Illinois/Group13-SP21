from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/services')
def services():
    return render_template('forms.html')

@app.route('/forms', methods = ['GET', 'POST'])
def forms():
    if request.method == 'POST':
        stock_name = request.form('stock_name')
        return render_template('/stock/' + stock_name)
    return render_template('forms.html')
