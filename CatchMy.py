__author__ = 'devmeepo'

from gi.repository import Gtk
from stop_menu import stopSwitchMenu
import fetch_station
import os

class catchMyPicon(Gtk.StatusIcon):
    def __init__(self):
        self.statusicon = Gtk.StatusIcon()
        self.statusicon.set_from_file(os.environ['HOME'] + "/.catch-my-bus-python/bus_stop_icon.png")
        self.statusicon.connect("popup-menu", self.right_click_event)
        self.stop_station = "Helmholtzstraße"
        self.city_name = "Dresden"


    def right_click_event(self, icon, button, time):
        self.menu = Gtk.Menu()

        current_stop = Gtk.MenuItem()
        current_stop.set_label("Current Stop: " + self.city_name + " - " + self.stop_station)

        self.menu.append(current_stop)


        i = 0
        for item in fetch_station.compile_menu(self.stop_station, self.city_name):
            new_menu_element = Gtk.MenuItem()
            new_menu_element.set_label(item)
            self.menu.append(new_menu_element)
            if i == 4:
                break
            i += 1

        quit = Gtk.MenuItem()
        quit.set_label("Quit")
        quit.connect("activate", Gtk.main_quit)

        pre_submenu = Gtk.MenuItem()
        pre_submenu.set_label("Switch Stops")

        pre_submenu.set_submenu(stopSwitchMenu(self).return_new_menu())

        self.menu.append(pre_submenu)
        
        self.menu.append(quit)

        self.menu.show_all()

        def pos(menu, icon):
                return (Gtk.StatusIcon.position_menu(menu, icon))

        self.menu.popup(None, None, pos, self.statusicon, button, time)


    def set_new_stop(self, stop_station, city_name):
        self.stop_station = stop_station
        self.city_name = city_name


catchMyPicon()
Gtk.main()
