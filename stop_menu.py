__author__ = 'devmeepo'

from gi.repository import Gtk


class stopSwitchMenu:
	def __init__(self, parent_menu):
		self.parent_menu = parent_menu
		self.new_menu = Gtk.Menu()

		first_stop = Gtk.MenuItem()
		first_stop.set_label("Dresden -- Zellescher Weg")

		second_stop = Gtk.MenuItem()
		second_stop.set_label("Dresden -- Helmholtzstraße")

		third_stop = Gtk.MenuItem()
		third_stop.set_label("Possendorf -- Rundteil")

		first_stop.connect("activate", self.change_stop)
		second_stop.connect("activate", self.change_stop)
		third_stop.connect("activate", self.change_stop)

		self.new_menu.append(first_stop)
		self.new_menu.append(second_stop)
		self.new_menu.append(third_stop)

	
	def return_new_menu(self):
		return self.new_menu


	def change_stop(self, widget):
		help_string = widget.get_label()
		help_string = help_string.replace(" ", "", 2)
		help_string = help_string.split("--")
		self.parent_menu.set_new_stop(help_string[1], help_string[0])