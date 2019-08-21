import requests, json

_URL = "https://api.robinhood.com/quotes/"


def get_quotes(token, symbols):
	params = {
		'symbols': ','.join(symbols)
	}
	headers = {'Authorization': 'Bearer %s' % (token)}
	r = requests.get(url = _URL, headers = headers, params = params) 
	return json.loads(r.text)


def get_ask_price(token, symbol):
	qts = get_quotes(token, [symbol])
	return qts['results'][0]['ask_price']


