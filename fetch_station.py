import urllib.request
import json
import itertools


def get_departure_list(stop_name):
    stop_name = stop_name.replace(" ", "%20")
    stop_name = str(stop_name.encode("ascii", "ignore"))
    url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort=Dresden&hst=" + stop_name + "&vz="


    file = urllib.request.urlopen(url).read().decode('utf-8')

    content = json.loads(file)

    # use this to get an output which is a single list of stuff
    return list(itertools.chain(*content))

    # return content
    # use this to get an output that list of lists
