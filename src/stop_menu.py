__author__ = 'devmeepo'

from gi.repository import Gtk
import os


class stopSwitchMenu:
	def __init__(self, parent_menu):
		self.parent_menu = parent_menu
		self.new_menu = Gtk.Menu()
		stoplist_path = "{0}/assets/stop_list".format(self.parent_menu.assets)

		stoplist = sorted(open(stoplist_path, 'r').read().split("\n"))

		for item in stoplist:
			if item != "":
				new_stop = Gtk.MenuItem()
				new_stop.set_label(item.replace("--", "-"))

				new_stop.connect("activate", self.change_stop)
				self.new_menu.append(new_stop)
	
	def return_new_menu(self):
		return self.new_menu


	def change_stop(self, widget):
		help_string = widget.get_label()
		help_string = help_string.split(" - ")
		self.parent_menu.set_new_stop(help_string[1], help_string[0])
