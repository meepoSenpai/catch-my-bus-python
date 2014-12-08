
from gi.repository import Gtk


class notification_time_list:

	def __init__(self, parent_menu):
		self.parent_menu = parent_menu
		self.new_menu = Gtk.Menu()

		for i in range(15):
			new_menu_item = Gtk.MenuItem()
			new_menu_item.set_label(str(i + 1))

			new_menu_item.connect("activate", self.change_notification_time)
			self.new_menu.append(new_menu_item)
	
	def return_new_menu(self):
		return self.new_menu

	def change_notification_time(self, widget):
		self.parent_menu.time_to_busstop = int(widget.get_label())

