# This is the file that the user should execute.

from orders import Order

# The below lines are for testing purposes.
order_test = Order(12345, "Test 'the' Order", "hat", 500)
print(order_test.get_boxes_required())
print(order_test.get_boxes_required(126))
