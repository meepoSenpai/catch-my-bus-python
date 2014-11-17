from gi.repository import Gtk
import fetch_station
import os

class catchMyPicon(Gtk.StatusIcon):
    def __init__(self):
        self.statusicon = Gtk.StatusIcon()
        self.statusicon.set_from_file(os.environ['HOME'] + "/.catch-my-bus-python/bus_stop_icon.png")
        self.statusicon.connect("popup-menu", self.right_click_event)
        self.stop_station = "Helmholzstraße"


    def right_click_event(self, icon, button, time):
        self.menu = Gtk.Menu()

        content = fetch_station.get_departure_list(self.stop_station)

        first_menu_element = Gtk.MenuItem()
        first_menu_element.set_label("Current Stop: " + self.stop_station)
        self.menu.append(first_menu_element)

        i = 0
        test = ""
        for x in content:
            if i % 3 != 2:
                test = test + str(x) + " "
            else:
                hours = int(str(x)) // 60
                minutes = int(str(x)) % 60
                hours = str(hours)
                if minutes < 10:
                    test = test + hours + ":" + "0" + str(minutes)
                else:
                    test = test + hours + ":" + str(minutes)
                new_menu_element = Gtk.MenuItem()
                new_menu_element.set_label(test)
                self.menu.append(new_menu_element)
                test = ""
            i = i + 1    

        stop_one = Gtk.MenuItem()
        stop_one.set_label("Set Stop: Zellescher Weg")

        stop_one.connect("activate", self.set_stop_one)

        stop_two = Gtk.MenuItem()
        stop_two.set_label("Set Stop: Helmholzstraße")

        stop_two.connect("activate", self.set_stop_two)
        quit = Gtk.MenuItem()
        quit.set_label("Quit")
        quit.connect("activate", Gtk.main_quit)
        
        self.menu.append(stop_one)
        self.menu.append(stop_two)

        self.menu.append(quit)

        self.menu.show_all()

        def pos(menu, icon):
                return (Gtk.StatusIcon.position_menu(menu, icon))

        self.menu.popup(None, None, pos, self.statusicon, button, time)

    def set_stop_one(self, widget):
        self.stop_station = "Zellescher Weg"

    def set_stop_two(self, widget):
        self.stop_station = "Helmholzstraße"


stop_station = "Technische Universität"
catchMyPicon()
Gtk.main()
