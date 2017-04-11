import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class Menu(Gtk.Menu):

    def __init__(self, parent):
        Gtk.Menu.__init__(self)
        self.parent_widget = parent
        self.append(Gtk.MenuItem.new_with_label('Current Stop'))
        self.append(Gtk.SeparatorMenuItem())
        self.append(Gtk.MenuItem.new_with_label(
            '{} - {}'.format(self.parent_widget.icon_props['last_stop'],
                             self.parent_widget.icon_props['stop_station'])))
        self.append(Gtk.MenuItem.new_with_label('Switch Station'))
        self.append(Gtk.MenuItem.new_with_label('Change notification timer'))
        self.append(Gtk.SeparatorMenuItem())
        self.append(Gtk.MenuItem.new_with_label('Quit'))
        self.get_children()[-1].connect('activate', self.parent_widget.quit_program)
        self.show_all()
