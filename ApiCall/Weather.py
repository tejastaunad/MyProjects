import requests
	import json

	# main api url
	url = 'http://api.openweathermap.org/data/2.5/weather?q='
	# put your username/password  api key and city name here
	auth = ('your weathermap.org mailID', 'password of weathermap.org')
	APPID = 'API token from weathermap.org'
	Cityname = 'Bangalore'

	# add a token parameter to the request
	params = {

	}
	response = requests.get(url + Cityname + '&APPID='+APPID ,
	                        params=params, verify=False).json()

	# response contains the geoJSON object,
	# pretty print it to the console
	print json.dumps(response, indent=4)
