# This is the file that the user should execute.

import sys
from datetime import datetime

from PySide6.QtWidgets import QApplication

from widgets import Widget
from orders import Order

app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()
