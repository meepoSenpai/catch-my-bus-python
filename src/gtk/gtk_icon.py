from gi.repository import Gtk, GLib
import os

ASSET_PATH = os.path.dirname(os.path.realpath(__file__))

class stopIcon(Gtk.StatusIcon):
    '''
    The GTK icon that displays the stops and the times when busses arrive
    at the chosen station.
    '''
    
    def __init__(self):
        '''
        Constructor doesn't need extra params
        '''
        super().__init__()
        self.set_from_file("{0}/assets/bus_stop_icon.png".format(str(ASSET_PATH)))
