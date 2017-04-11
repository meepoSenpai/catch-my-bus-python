import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class DepartureItem(Gtk.MenuItem):

    def __init__(self, departure, parent):
        Gtk.MenuItem.__init__(self)
        self.parent_widget = parent
        self.departure = departure
        self.set_label(str(self.departure))
        self.connect('activate', self.set_to_notify)

    def set_to_notify(self, widget):
        self.parent_widget.cur_notification = self.departure.get_notification_dict(icon_path="", time=0)
        self.parent_widget.notify_user()
