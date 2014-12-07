__author__ = 'devmeepo'

from gi.repository import Gtk


class stopSwitchMenu:
	def __init__(self, parent_menu):
		self.parent_menu = parent_menu
		self.new_menu = Gtk.Menu()

		stoplist = open('stop_list.txt', 'r').read().split("\n")

		for item in stoplist:
			new_stop = Gtk.MenuItem()
			new_stop.set_label(item)

			new_stop.connect("activate", self.change_stop)
			self.new_menu.append(new_stop)
	
	def return_new_menu(self):
		return self.new_menu


	def change_stop(self, widget):
		help_string = widget.get_label()
		help_string = help_string.replace(" ", "", 2)
		help_string = help_string.split("--")
		self.parent_menu.set_new_stop(help_string[1], help_string[0])