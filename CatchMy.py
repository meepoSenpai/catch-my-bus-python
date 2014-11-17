from gi.repository import Gtk
import fetch_station
import os

class catchMyPicon:

    namelist = ["Hans", "Walter"]

    def __init__(self):
        self.statusicon = Gtk.StatusIcon()
        self.statusicon.set_from_file(os.environ['HOME'] + "/.catch-my-bus-python/bus_stop_icon.png")
        self.statusicon.connect("popup-menu", self.right_click_event)


    def right_click_event(self, icon, button, time):
        self.menu = Gtk.Menu()

        content = fetch_station.get_departure_list()

        i = 0
        test = ""
        for x in content:
	        if i != 2:
		        test = test + str(x) + " "
        	else:
        		hours = int(str(x)) // 60
        		minutes = int(str(x)) % 60
        		hours = str(hours)
        		if minutes < 10:
        			minutes = "0" + str(minutes)
        		else:
        			minutes = str(minutes)
        			test = test + hours + ":" + minutes
	        	new_menu_element = Gtk.MenuItem()
	        	new_menu_element.set_label(test)
	        	self.menu.append(new_menu_element)
        		test = ""
        	i = (i + 1) % 3       
        quit = Gtk.MenuItem()
        quit.set_label("Quit")
        quit.connect("activate", Gtk.main_quit)
        
        self.menu.append(quit)

        self.menu.show_all()

        def pos(menu, icon):
                return (Gtk.StatusIcon.position_menu(menu, icon))

        self.menu.popup(None, None, pos, self.statusicon, button, time)

catchMyPicon()
Gtk.main()