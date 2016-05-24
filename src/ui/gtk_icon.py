import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gsf',  '1')

from gi.repository import Gtk, GLib, Gsf
import os
from .departure_item import DepartureItem

ASSET_PATH = os.path.dirname(os.path.realpath(__file__))
ASSET_STR = "{0}/../assets".format(ASSET_PATH)

class StopIcon(Gtk.StatusIcon):
    '''
    The GTK icon that displays the stops and the times when busses arrive
    at the chosen station.
    '''

    def __init__(self):
        '''
        Constructor doesn't need extra params
        '''
        Gtk.StatusIcon.__init__(self)
        self.set_from_file("{0}/bus_stop_icon.png".format(ASSET_STR))
        print("{}/bus_stop_icon.png".format(ASSET_STR))
        if os.path.isfile("{0}/last_config".format(ASSET_STR)):
            config_path = "{0}/last_config".format(ASSET_STR)
        else:
            config_path = "{0}/standard_config".format(ASSET_STR)
        with open(config_path, 'r') as config:
            self.icon_props = {'last_stop' : config.readline().replace("\n", ""),
                               'stop_station' : config.readline().replace("\n", ""),
                               'notification_timer' : -1,
                               'timer_offset' : config.readline().replace("\n", "")}
        self.right_click_menu = self.generate_popup_menu()
        self.left_click_menu = self.init_left_click_menu()
        self.is_active = True
        self.connect("popup-menu", self.right_click)
        self.departures = []
        self.connect("activate", self.print_button)

    def right_click(self, icon, button, time):
        self.right_click_menu.popup(None, None, self.position_menu, icon, button, time)

    def print_button(self, icon):
        time = Gsf.Timestamp()
        self.left_click_menu.popup(None, None, self.position_menu,
                                   self, 3, time.seconds)

    def generate_popup_menu(self):
        '''
        This function generates the right-click menu to switch stops
        or the notification time and takes no parameters.
        Returns a Gtk.Menu
       '''

        parent_menu = Gtk.Menu()
        item_list = []
        item_list.append(Gtk.MenuItem())
        item_list[-1].set_label("Current Stop")
        item_list.append(Gtk.SeparatorMenuItem())
        item_list.append(Gtk.MenuItem())
        item_list[-1].set_label("{0} - {1}".format(self.icon_props['last_stop'],
                                                   self.icon_props['stop_station']))
        item_list.append(Gtk.MenuItem())
        item_list[-1].set_label("Switch Station")
        item_list.append(Gtk.MenuItem())
        item_list[-1].set_label("Change notification timer")
        item_list.append(Gtk.SeparatorMenuItem())
        item_list.append(Gtk.MenuItem())
        item_list[-1].set_label("Quit")
        item_list[-1].connect("activate", self.quit_program)
        for elem in item_list:
            parent_menu.append(elem)
        parent_menu.show_all()
        return parent_menu

    def init_left_click_menu(self):
        parent_menu = Gtk.Menu()
        no_connections_item = Gtk.MenuItem("No initial connection")
        parent_menu.append(no_connections_item)
        parent_menu.show_all()
        return parent_menu

    def generate_left_click_menu(self):
        self.left_click_menu = Gtk.Menu()
        self.departures.reverse()
        for item in self.departures:
            menu_item = DepartureItem(item)
            menu_item.connect('activate', menu_item.set_to_notify)
            self.left_click_menu.append(menu_item)
        self.left_click_menu.show_all()
        self.departures.reverse()

    def quit_program(self, widget):
        self.is_active = False
        Gtk.main_quit()

    def update_departurelist(self, departures):
        departures.reverse()
        if departures == []:
            return
        elif self.departures == []:
            self.departures = departures
        if departures[-1].direction == self.departures[-1].direction:
            for new_item, item in zip(departures, self.departures):
                item.update_arrival_time(new_item.arrival_time)
        else:
            self.departures = departures
        self.generate_left_click_menu()

    def gtk_main(self):
        Gtk.main()
