__author__ = 'JustusAdam'

import urllib.request
import json



def get_departure_list(stop_name, city_name):
    stop_name = stop_name.replace("ä", "ae").replace("ü", "ue").replace("ö", "oe").replace("ß", "ss").replace(" ", "%20")
    city_name = city_name.replace("ä", "ae").replace("ü", "ue").replace("ö", "oe").replace("ß", "ss").replace(" ", "%20")
    url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort=" + city_name +"&hst=" + stop_name + "&vz="


    file = urllib.request.urlopen(url).read().decode('utf-8')

    content = json.loads(file)

    return content

def compile_menu(station="Heinrich-Zille-Straße", city_name="Dresden"):
    return [
        ' '.join([number, direction, ':'.join(split_time(time))]) for number, direction, time in get_departure_list(station, city_name)
    ]

def split_time(time):
    hours = str(int(str(time)) // 60)
    minutes = str(int(str(time)) % 60)
    if len(minutes) < 2:
        minutes = "0" + minutes
    else:
        minutes = str(minutes)
    return hours, minutes

a = compile_menu("Heinrich-Zille-Straße")