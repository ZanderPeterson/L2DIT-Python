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

# The below lines are for testing purposes.
order_test = Order(777,
                   "Jaz",
                   "drumsticks",
                   123,
                   datetime(2025, 9, 10),
                   datetime(2025, 10, 10))
print(order_test.get_boxes_required())
print(f"Number of boxes required: {order_test.get_boxes_required(126)}")
print(f"Order Duration: {order_test.get_order_duration_days()} day(s)")
print(f"Raffle Number: {order_test.raffle_number}")
