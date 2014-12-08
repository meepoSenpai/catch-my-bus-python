__author__ = 'JustusAdam'

import urllib.request
import json


def escape_german(string):
	for char, escaped in [
		('ä', 'ae'),
		('ü', 'ue'),
		('ö', 'oe'),
		('ß', 'ss'),
		(' ', '%20')
	]:
		string = string.replace(char, escaped)
	return string


def get_departure_list(stop_name, city_name):
	stop_name = escape_german(stop_name)
	city_name = escape_german(city_name)
	url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort=" + city_name +"&hst=" + stop_name + "&vz="

	try:
		file = urllib.request.urlopen(url).read().decode('utf-8')

		content = json.loads(file)
	except urllib.error.URLError as e:
		content= ["No Internet Connection"]

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