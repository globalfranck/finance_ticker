from flask import Flask
import requests

app = Flask(__name__)

API_URL = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{ticker}'

# Defining a function to fetch the stock price using the FMP API

def fetch_price(ticker):
	data = requests.get(API_URL.format(ticker=ticker.upper()), params={'apikey': 'demo'}).json()
	return data["price"]

# http://localhost:5000/stock/AAPL

# Routing the user URL /stock/ticker to a page where the price of the ticker is shown

@app.route('/stock/<ticker>')
def stock(ticker):
	price = fetch_price(ticker)
	return "The price of {ticker} is {price}".format(ticker=ticker, price=price)

# Routing the user to a blank page

@app.route('/')
def home_page():
	return 'Try /stock/AAPL'
