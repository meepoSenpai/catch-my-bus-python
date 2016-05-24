#! /usr/bin/env python3

__author__ = 'devmeepo'
import os, time
from threading import Thread
from fetch_station import compile_menu
from ui.gtk_icon import StopIcon



ASSET_PATH = os.path.dirname(os.path.realpath(__file__))

def check_for_updates():
    """
    If run will check for bus-arrival-updates every 60 seconds
    """
    i = 1
    departures = compile_menu()
    THE_TRAY.update_departurelist(departures)
    while THE_TRAY.is_active:
        if i % 20 == 0:
            departures = compile_menu()
            THE_TRAY.update_departurelist(departures)
        i += 1
        time.sleep(1)


if(__name__ == "__main__"):
    THE_TRAY = StopIcon()
    # Will launch the thread for updating the notification item
    CHECK_THREAD = Thread(target=check_for_updates)
    CHECK_THREAD.start()
    THE_TRAY.gtk_main()
