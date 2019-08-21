import requests, json

_URL = "https://api.robinhood.com/instruments/?"


def get_instrument_url(token, symbol):
	params = {
		'symbol': symbol
	}
	headers = {'Authorization': 'Bearer %s' % (token)}
	r = requests.get(url = _URL, headers = headers, params = params) 
	js = json.loads(r.text)
	return js['results'][0]['url']


