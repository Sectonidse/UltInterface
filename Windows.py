import os
from tkinter import ttk, Tk
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class Window:
    WindowsList = []
    UnixApp = Gtk.Application()
    def add(self, Name):  # Adds a new window to the render list
        if os.name == "nt":
            self.WindowsList.append(Tk())
            self.WindowsList[-1].title(Name)
        elif os.name == "posix":
            self.WindowsList.append(Gtk.ApplicationWindow(application=self.UnixApp))

    def render(self):
        if os.name == "nt":
            self.WindowsList[0].mainloop()




# Hi there!
# It has started.