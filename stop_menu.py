__author__ = 'devmeepo'

from gi.repository import Gtk


class stopSwitchMenu(Gtk.Menu):

	def __init__(self, parent_menu):
		self.menu = Gtk.Menu()
		self.parent_menu = parent_menu

		first_stop = Gtk.MenuItem()
		first_stop.set_label("Set to: Dresden - Zellescher Weg")

		second_stop = Gtk.MenuItem()
		second_stop.set_label("Set to: Dresden - Helmholzstraße")

		third_stop = Gtk.MenuItem()
		third_stop.set_label("Set to: Possendorf - Rundteil")

		first_stop.connect("activate", self.change_to_stop_one)
		second_stop.connect("activate", self.change_to_stop_two)
		third_stop.connect("activate", self.change_to_stop_three)

		self.menu.append(first_stop)
		self.menu.append(second_stop)
		self.menu.append(third_stop)

	def change_to_stop_one(self, widget):
		self.parent_menu.set_new_stop("Zellescher Weg", "Dresden")

	def change_to_stop_two(self, widget):
		self.parent_menu.set_new_stop("Helmholzstraße", "Dresden")

	def change_to_stop_three(self, widget):
		self.parent_menu.set_new_stop("Rundteil", "Possendorf")


def create_a_menu(parent_menu):
	return stopSwitchMenu(parent_menu)