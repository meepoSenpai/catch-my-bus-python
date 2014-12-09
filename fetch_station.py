__author__ = 'JustusAdam'

import json
import requests


def get_departure_list(stop_name, city_name):
	try:
		r = requests.get(
		    url='http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do',
		    params={
		    	'ort': city_name,
		    	'hst': stop_name
		    }
		)
		if r.status_code == 200:
			content = json.loads(r.content.decode('utf-8'))
		else:
			content = ['No Internet Connection']
	except requests.RequestException as e:
		print('Request Exception: ' + str(e))
		content = ['No Internet Connection']

	print(content)

	return content


def compile_menu(station="Heinrich-Zille-Straße", city_name="Dresden"):
	departure_list = get_departure_list(station, city_name)
	if departure_list == ["No Internet Connection"]:
		return departure_list
	else:
		return [
			' '.join([number, direction, ':'.join(split_time(time))]) for number, direction, time in departure_list
		]


def split_time(time):
	if time == "":
		time = 0
	hours = str(int(str(time)) // 60)
	minutes = str(int(str(time)) % 60)
	if len(minutes) < 2:
		minutes = "0" + minutes
	else:
		minutes = str(minutes)
	return hours, minutes


print("Hallo")
