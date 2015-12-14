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

notify2.init("CatchMyBus")
asset_path = os.path.dirname(os.path.realpath(__file__))

class catchMyPicon(Gtk.StatusIcon):
    def __init__(self):
        self.assets = asset_path
        self.statusicon = Gtk.StatusIcon()
        self.statusicon.set_from_file("{0}/assets/bus_stop_icon.png".format(str(asset_path)))
        self.statusicon.connect("popup-menu", self.right_click_event)
        try:
            last_stop = open("{0}/assets/last_config".format(asset_path), 'r')
        except FileNotFoundError:
            last_stop = open("{0}/assets/standard_config".format(asset_path), 'r')
        self.city_name = last_stop.readline().replace("\n", "")
        self.stop_station = last_stop.readline().replace("\n", "")
        self.stop_list = compile_menu(self.stop_station, self.city_name)
        self.program_is_running = True
        self.notification_timer = -1
        self.time_to_busstop = int(last_stop.readline().replace("\n", ""))

    def right_click_event(self, icon, button, time):
        """
        Generates the Menu when right-clicking the Icon
        """
        self.menu = Gtk.Menu()

        current_stop = Gtk.MenuItem()
        current_stop.set_label("Current Stop: " + self.city_name + " - " + self.stop_station)

        for item in self.stop_list[:5]:
            new_menu_element = Gtk.MenuItem()
            new_menu_element.set_label(item)
            new_menu_element.connect("activate", self.set_notification_timer)
            self.menu.append(new_menu_element)

        self.menu.append(Gtk.SeparatorMenuItem())

        terminate_application = Gtk.MenuItem()
        terminate_application.set_label("Quit")
        terminate_application.connect("activate", self.quit_program)

        stop_switching_menu = Gtk.MenuItem()
        stop_switching_menu.set_label("Switch Stops")

        stop_switching_menu.set_submenu(stopSwitchMenu(self).return_new_menu())

        time_switcher_menu = Gtk.MenuItem()
        time_switcher_menu.set_label("Change Notification-time")

        time_switcher_menu.set_submenu(notification_time_list(self).return_new_menu())

        manual_refresher = Gtk.MenuItem()
        manual_refresher.set_label("Manual Refresh")
        manual_refresher.connect("activate", self.manual_refresh)

        self.menu.append(current_stop)
        self.menu.append(Gtk.SeparatorMenuItem())


        self.menu.append(stop_switching_menu)
        self.menu.append(time_switcher_menu)
        self.menu.append(manual_refresher)

        self.menu.append(Gtk.SeparatorMenuItem())

        self.menu.append(terminate_application)

        self.menu.show_all()

        def pos(menu, x, y, the_icon):
                return Gtk.StatusIcon.position_menu(menu, x, y, the_icon)

        self.menu.popup(None, None, pos, self.statusicon, button, time)

    def set_new_stop(self, stop_station, city_name):
        """
        Sets the current stop which is to be loaded to the given
        city and station name
        """
        self.stop_station = stop_station
        self.city_name = city_name

        save_last_stop = open("{0}/assets/last_config".format(asset_path), 'w')
        save_last_stop.write(self.city_name + "\n" + self.stop_station + "\n" + str(self.time_to_busstop) + "\n")

        self.update_stoplist()

    def update_stoplist(self):
        """
        Updates the displayed Arrival-times
        """
        self.stop_list = compile_menu(self.stop_station, self.city_name)

    # Ends the GTK main-loop
    def quit_program(self, widget):
        self.program_is_running = False
        Gtk.main_quit()

    def set_notification_timer(self, widget):
        """
        Sets a timer for a notification when the next bus/tram arrives
        """
        string_list_helper = widget.get_label().split(" ")
        time_for_notif = int(string_list_helper[len(string_list_helper) - 1].split(":")[0]) * 60 + int(string_list_helper[len(string_list_helper) - 1].split(":")[1])
        self.notification_timer = time_for_notif - self.time_to_busstop

    def display_alert(self):
        """
        Displays the Notification (at least on Linux systems or systems that have a notify-send command)
        """
        notification = notify2.Notification("Bus arriving soon!",
                                            "The bus will arrive in {0} minutes".format(the_tray.time_to_busstop),
                                            "{0}/assets/bus_stop_icon.png".format(str(asset_path)))
        print(self.assets)
        notification.show()

    def manual_refresh(self, widget):
        self.update_stoplist()


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

from .gtk.gtk_icon import StopIcon

if(__name__ == "__main__"):
    # the_tray = catchMyPicon()
    the_tray = StopIcon()
    # Will launch the thread for updating the notification item
    check_thread = Thread(target=check_for_updates)
    check_thread.start()

    Gtk.main()
