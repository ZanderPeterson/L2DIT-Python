# This is the file that the user should execute.

#Standard Libraries
import sys #used for opening a window for the GUI
from datetime import datetime #used in many places for everything to do with dates

#3rd Party Libraries
from PySide6.QtWidgets import QApplication #The library utilised for the GUI

#Local Imports
from widgets import Widget #A local file that contains the "Widget" Class
from orders import Order #A local library that contains the "Order" Class

#Opens a window — the contents and functions of which is managed by an instance of the Widget class.
app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()
