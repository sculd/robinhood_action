import requests, os, json

_URL_AUTH = "https://api.robinhood.com/oauth2/token/"

CLIENT_ID = os.environ['RH_CLIENT_ID']
DEFICE_ID = os.environ['RH_DEVICE_TOKEN']

def get_auth():
	data = {
		'username': os.environ['RH_ID'],
		'password': os.environ['RH_PW'],
		"grant_type":"password",
		"client_id": CLIENT_ID,
		'device_token': DEFICE_ID,
		'expires_in': 86400,
		'scope': "internal"
	} 

	r = requests.post(url = _URL_AUTH, json = data) 
	return json.loads(r.text)

def get_token():
	auth = get_auth()
	return auth['access_token']
