#! /usr/bin/env python3

__author__ = 'devmeepo'

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gsf', '1')

from gi.repository import Gtk, GLib
from pathlib import Path
from .stop_menu import stopSwitchMenu
from .notification_time_list import notification_time_list
from .fetch_station import compile_menu
import os, time
from threading import Thread
import notify2
from .gtk.gtk_icon import StopIcon

notify2.init("CatchMyBus")
asset_path = os.path.dirname(os.path.realpath(__file__))

def check_for_updates():
    """
    If run will check for bus-arrival-updates every 60 seconds
    """
    i = 1
    departures = compile_menu()
    the_tray.update_departurelist(departures)
    while the_tray.is_active:
        if i % 20 == 0:
            departures = compile_menu()
            the_tray.update_departurelist(departures)
        i += 1
        time.sleep(1)


if(__name__ == "__main__"):
    # the_tray = catchMyPicon()
    print(asset_path)
    the_tray = StopIcon()
    # Will launch the thread for updating the notification item
    check_thread = Thread(target=check_for_updates)
    check_thread.start()

    Gtk.main()
