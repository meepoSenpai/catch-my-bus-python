import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class DepartureItem(Gtk.MenuItem):

    def __init__(self, departure):
        Gtk.MenuItem.__init__(self)
        self.departure = departure
        self.set_label(str(self.departure))

    def set_to_notify(self, widget):
        self.departure.set_to_notify(icon_path="")
