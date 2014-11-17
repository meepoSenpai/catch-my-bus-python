import urllib.request

def get_departure_list(stop_name, city_name):
	stop_name = stop_name.replace(" ", "%20")
	stop_name = str(stop_name.encode("utf-8"))
	url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort="+ city_name +"&hst="+ stop_name +"&vz="
	print(url)
	content = urllib.request.urlopen(url).read()

	content = str(content, "utf-8")

	content = content.replace("[", "")
	content = content.replace(",", "")
	content = content.replace("]", "")
	content = content.split("\"")
	print(content)
	if content[5] == "":
		content[5] = "0"
	while content.count("") > 0:
		content.remove("")

	return content

