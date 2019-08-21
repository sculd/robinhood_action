import requests, json, time
import quote, account, instrument
from auth import CLIENT_ID

_URL = "https://api.robinhood.com/orders/"
_URL_ORDER = "api.robinhood.com/orders/"

def _order_limit_sell(token, account_url, instrument_url, symbol, quantity, price):
	data = {
		'account': account_url,
		'instrument': instrument_url,
		'symbol': symbol,
		'type': 'limit',
		'time_in_force': 'gfd',
		'trigger': 'immediate',
		'price': price,
		'stop_price': None,
		'quantity': quantity,
		'side': 'sell',
		'client_id': CLIENT_ID,
		'extended_hours': False
	} 

	r = requests.post(url = _URL, json = data) 
	return json.loads(r.text)

def _order_market_buy(token, account_url, instrument_url, symbol, quantity, price):
	data = {
		'account': account_url,
		'instrument': instrument_url,
		'symbol': symbol,
		'type': 'market',
		'time_in_force': 'gfd',
		'trigger': 'immediate',
		'price': price,
		'stop_price': None,
		'quantity': quantity,
		'side': 'buy',
		'client_id': CLIENT_ID,
		'extended_hours': False
	} 

	r = requests.post(url = _URL, json = data) 
	return json.loads(r.text)

def _order_status(token, order_id):
	params = {
		'order_id': order_id
	}
	headers = {'Authorization': 'Bearer %s' % (token)}
	r = requests.get(url = _URL, headers = headers, params = params) 
	return json.loads(r.text)

def buy_and_sell(token, symbol, quantity, sell_price_delta):	
	account_url = account.get_account_url(token)
	instrument_url = instrument.get_instrument_url(token, symbol)
	ask_price = quote.get_ask_price(token, symbol)

	buy_response = _order_market_buy(token, account_url, instrument_url, symbol, quantity, ask_price)
	order_id = None
	cnt = 0
	while True:
		time.sleep(1)
		buy_st = _order_status(token, order_id)
		if False:
			sell_st = _order_limit_sell(token, account_url, instrument_url, symbol, quantity, price + sell_price_delta)
			return sell_st
		cnt += 1

	return {}



