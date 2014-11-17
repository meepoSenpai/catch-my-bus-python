import urllib.request

def get_departure_list(stop_name):
	stop_name = stop_name.replace(" ", "%20")
	stop_name = str(stop_name.encode("ascii", "ignore"))
	url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort=Dresden&hst=" + stop_name + "&vz="
	content = urllib.request.urlopen(url).read()

	content = str(content, "utf-8")

	content = content.replace("[", "")
	content = content.replace(",", "")
	content = content.replace("]", "")
	content = content.split("\"")
	if content[5] == "":
		content[5] = "0"
	while content.count("") > 0:
		content.remove("")

	return content

