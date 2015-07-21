from gi.repository import Gtk
# from pathlib import Path


class notification_time_list:

	def __init__(self, parent_menu):
		self.parent_menu = parent_menu
		self.new_menu = Gtk.Menu()

		cur_set = Gtk.MenuItem()
		cur_set.set_label("Currently set to " + str(self.parent_menu.time_to_busstop) + " Minutes")
		self.new_menu.append(cur_set)

		for i in range(30):
			new_menu_item = Gtk.MenuItem()
			new_menu_item.set_label(str(i + 1))

			new_menu_item.connect("activate", self.change_notification_time)
			self.new_menu.append(new_menu_item)
	
	def return_new_menu(self):
		return self.new_menu

	def change_notification_time(self, widget):
		self.parent_menu.time_to_busstop = int(widget.get_label())
		save_last_stop = open("{0}/assets/last_config.txt".format(self.parent_menu.assets), 'w')
		save_last_stop.write("{0}\n{1}\n{2}\n".format(self.parent_menu.city_name,
                                                           self.parent_menu.stop_station,
                                                           str(self.parent_menu.time_to_busstop)))

