__author__ = 'JustusAdam'

import json
import requests
from src.departure import Departure


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
    except requests.RequestException:
        content = ['No Internet Connection']

    return content


def compile_menu(station="Helmholtzstraße", city_name="Dresden"):
    departure_list = get_departure_list(station, city_name)
    if departure_list == ["No Internet Connection"]:
        return departure_list
    else:
        return [
            Departure(number, direction, time) for number, direction, time in departure_list
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
