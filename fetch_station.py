import urllib.request

def get_departure_list():
	content = urllib.request.urlopen("http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort=Dresden&hst=Zellescher%20Weg&vz=").read()
	#content = "[[\"11\",\"Bhlau\",\"3\"],[\"11\",\"Zschertnitz\",\"6\"],[\"61\",\"Lbtau\",\"20\"],[\"61\",\"E Pohlandplatz\",\"23\"],[\"11\",\"Bhlau\",\"33\"],[\"11\",\"Zschertnitz\",\"36\"],[\"11\",\"Gorbitz\",\"48\"],[\"61\",\"Btf. Gruna\",\"53\"],[\"11\",\"Zschertnitz\",\"66\"],[\"11\",\"Bhlau\",\"73\"]]"

	content = str(content, "utf-8")

	content = content.replace("[", "")
	content = content.replace(",", "")
	content = content.replace("]", "")
	content = content.split("\"")
	while content.count("") > 0:
		content.remove("")
	return content

