import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from .departure_item import DepartureItem

class Menu(Gtk.Menu):

    def __init__(self, parent):
        Gtk.Menu.__init__(self)
        self.parent_widget = parent
        self.append(Gtk.MenuItem.new_with_label('Current Stop'))
        self.append(Gtk.SeparatorMenuItem())
        self.append(Gtk.MenuItem.new_with_label(
            '{} - {}'.format(self.parent_widget.icon_props['last_stop'],
                             self.parent_widget.icon_props['stop_station'])))
        self.append(Gtk.MenuItem.new_with_label('Departure Notification'))
        self.append(Gtk.MenuItem.new_with_label('Change notification timer'))
        self.append(Gtk.SeparatorMenuItem())
        self.append(Gtk.MenuItem.new_with_label('Quit'))
        self.get_children()[-1].connect('activate', self.parent_widget.quit_program)
        self.show_all()

    def create_departure_list(self, departures):
        for elem in self.get_children():
            if elem.get_label() == 'Departure Notification':
                departure_selection = elem
                break
        sub_menu = Gtk.Menu()
        for elem in departures:
            new_elem = DepartureItem(elem, self.parent_widget)
            sub_menu.append(new_elem)
        sub_menu.show_all()
        departure_selection.set_submenu(sub_menu)
