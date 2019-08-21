import requests, json

_URL = "https://api.robinhood.com/accounts/"


def get_id(token):
	headers = {'Authorization': 'Bearer %s' % (token)}
	r = requests.get(url = _URL, headers = headers) 
	return json.loads(r.text)


def get_account_url(token):
	headers = {'Authorization': 'Bearer %s' % (token)}
	r = requests.get(url = _URL, headers = headers) 
	js = json.loads(r.text)
	return js['results'][0]['url']


