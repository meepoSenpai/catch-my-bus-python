import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gsf',  '1')

from gi.repository import Gtk, GLib, Gsf
import os
from .departure_item import DepartureItem
from .gtk_popup import Menu

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
        if os.path.isfile("{0}/last_config".format(ASSET_STR)):
            config_path = "{0}/last_config".format(ASSET_STR)
        else:
            config_path = "{0}/standard_config".format(ASSET_STR)
        with open(config_path, 'r') as config:
            self.icon_props = {'last_stop' : config.readline().replace("\n", ""),
                               'stop_station' : config.readline().replace("\n", ""),
                               'notification_timer' : -1,
                               'timer_offset' : config.readline().replace("\n", "")}
        self.right_click_menu = Menu(self)
        self.is_active = True
        self.departures = []
        self.status = True
        self.cur_notification = {}

    def do_popup_menu(self, button, time):
        '''
        Overloaded method for right click menu
        '''
        self.right_click_menu.popup(None, None, None, self, button, time)

    def create_tooltip(self):
        '''
        Creates the tooltips displaying the future Departures
        '''
        if not self.status:
            tooltip = 'No Internet Connection'
        else:
            tooltip = ""
            for elem in self.departures[::-1]:
                if tooltip == "":
                    tooltip = tooltip + str(elem)
                else:
                    tooltip = tooltip + '\n' + str(elem)
        self.set_tooltip_text(tooltip)


    def quit_program(self, widget):
        '''
        Will simply quit the Gtk main loop. Nothing else.
        '''
        self.is_active = False
        Gtk.main_quit()

    def update_departurelist(self, departures):
        '''
        Will update the List of departures.
        '''
        departures.reverse()
        if departures == [] or "No Internet Connection" in departures:
            self.status = False
            self.departures = []
            self.create_tooltip()
            return
        elif self.departures == [] and "No Internet Connections" not in departures:
            self.departures = departures
        if departures != ["No Internet Connection"] and \
           departures[-1].direction == self.departures[-1].direction:
            for new_item, item in zip(departures, self.departures):
                item.update_arrival_time(new_item.arrival_time)
        else:
            self.departures = departures
        self.status = True
        self.right_click_menu.create_departure_list(list(reversed(self.departures)))
        self.create_tooltip()

    def gtk_main(self):
        Gtk.main()

    def clear_notification(self):
        notification_keys = list(self.cur_notification.keys())
        for elem in notification_keys:
            self.cur_notification.pop(elem)

    def notify_user(self):
        while self.cur_notification['time'] != 0:
            self.cur_notification['time'] = self.cur_notification['time'] - 1
        self.cur_notification['notification'].show()
        self.clear_notification()
