#! /usr/bin/env python3

__author__ = 'devmeepo'

from gi.repository import Gtk, GLib
from stop_menu import stopSwitchMenu
import fetch_station, os, time
from threading import Thread

class catchMyPicon(Gtk.StatusIcon):
    def __init__(self):
        self.statusicon = Gtk.StatusIcon()
        self.statusicon.set_from_file(os.environ['HOME'] + "/.catch-my-bus-python/bus_stop_icon.png")
        self.statusicon.connect("popup-menu", self.right_click_event)
        self.stop_station = "Staats- und Universitätsbibliothek"
        self.city_name = "Dresden"
        self.stop_list = fetch_station.compile_menu(self.stop_station, self.city_name)
        self.program_is_running = True
        self.notification_timer = -1
        self.time_to_busstop = 5

    # Generates the Menu when right-clicking the Icon
    def right_click_event(self, icon, button, time):
        self.menu = Gtk.Menu()

        current_stop = Gtk.MenuItem()
        current_stop.set_label("Current Stop: " + self.city_name + " - " + self.stop_station)

        self.menu.append(current_stop)
        self.menu.append(Gtk.SeparatorMenuItem())

        for item in self.stop_list[:5]:
            new_menu_element = Gtk.MenuItem()
            new_menu_element.set_label(item)
            new_menu_element.connect("activate", self.set_notification_timer)
            self.menu.append(new_menu_element)

        self.menu.append(Gtk.SeparatorMenuItem())

        terminate_application = Gtk.MenuItem()
        terminate_application.set_label("Quit")
        terminate_application.connect("activate", self.quit_program)

        pre_submenu = Gtk.MenuItem()
        pre_submenu.set_label("Switch Stops")

        pre_submenu.set_submenu(stopSwitchMenu(self).return_new_menu())

        manual_refresher = Gtk.MenuItem()
        manual_refresher.set_label("Manual Refresh")
        manual_refresher.connect("activate", self.manual_refresh)

        self.menu.append(pre_submenu)

        self.menu.append(manual_refresher)
        
        self.menu.append(terminate_application)

        self.menu.show_all()

        def pos(menu, the_icon):
                return Gtk.StatusIcon.position_menu(menu, the_icon)

        self.menu.popup(None, None, pos, self.statusicon, button, time)

    # Sets the current stop which is to be loaded to the given
    # city and station name
    def set_new_stop(self, stop_station, city_name):
        self.stop_station = stop_station
        self.city_name = city_name
        self.update_stoplist()

    # Updates the displayed Arrival-times
    def update_stoplist(self):
        self.stop_list = fetch_station.compile_menu(self.stop_station, self.city_name)

    # Ends the GTK main-loop
    def quit_program(self, widget):
        self.program_is_running = False
        Gtk.main_quit()
    
    # Sets a timer for a notification when the next bus/tram arrives
    def set_notification_timer(self, widget):
        string_list_helper = widget.get_label().split(" ")
        time_for_notif = int(string_list_helper[len(string_list_helper) - 1].split(":")[0]) * 60 + int(string_list_helper[len(string_list_helper) - 1].split(":")[1])
        self.notification_timer = time_for_notif - self.time_to_busstop

    # Displays the Notification (at least on Linux systems or systems that have a notify-send command)
    def display_alert(self):
        os.system("notify-send \"" + str(self.time_to_busstop) + " minutes until the bus arrives\"")

    def manual_refresh(self, widget):
        self.update_stoplist()


# If run will check for bus-arrival-updates every 60 seconds
def check_for_updates():
    i = 1
    while the_tray.program_is_running:
        if i % 60 == 0:
            the_tray.update_stoplist()
            i = 0
            if the_tray.notification_timer >= 0:
                if the_tray.notification_timer == 0:
                    the_tray.display_alert()
                the_tray.notification_timer -= 1

        i += 1

        time.sleep(1)
        

the_tray = catchMyPicon()

# Will launch the thread for updating the notification item
check_thread = Thread(target=check_for_updates)
check_thread.start()


Gtk.main()
