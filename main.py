# This is the file that the user should execute.

from orders import Order
from datetime import datetime

# The below lines are for testing purposes.
order_test = Order(777,
                   "Jaz",
                   "drumsticks",
                   123,
                   datetime(2025, 9, 10),
                   datetime(2025, 9, 9))
print(order_test.get_boxes_required())
print(f"Number of boxes required: {order_test.get_boxes_required(126)}")
print(f"Order Duration: {order_test.get_order_duration_days()} day(s)")
