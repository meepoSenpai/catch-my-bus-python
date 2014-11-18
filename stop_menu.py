__author__ = 'devmeepo'

from gi.repository import Gtk


def stopSwitchMenu(parent_menu):
	parent_menu = parent_menu
	new_menu = Gtk.Menu()

	first_stop = Gtk.MenuItem()
	first_stop.set_label("Set to: Dresden - Zellescher Weg")

	second_stop = Gtk.MenuItem()
	second_stop.set_label("Set to: Dresden - Helmholzstraße")

	third_stop = Gtk.MenuItem()
	third_stop.set_label("Set to: Possendorf - Rundteil")

	first_stop.connect("activate", parent_menu.change_to_stop_one)
	second_stop.connect("activate", parent_menu.change_to_stop_two)
	third_stop.connect("activate", parent_menu.change_to_stop_three)

	new_menu.append(first_stop)
	new_menu.append(second_stop)
	new_menu.append(third_stop)

	return new_menu