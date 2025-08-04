# Contains the "Order" class, with every instance tracking a single order.

import math

class Order():
    """
    A Class which will have one instance per order, and tracks various
    order-specific bits of information, such as start/end dates, customer
    name, receipt number, the item, the quantity, raffle info, etc. etc.
    """

    def __init__(self,
                 receipt_num: int,
                 customer_name: str,
                 item_hired: str,
                 quantity: int) -> None:
        self.receipt_num: int = receipt_num
        self.customer_name: str = customer_name
        self.item_hired: str = item_hired
        self.quantity: int = quantity

        # Checking if the 'Quantity' is within the acceptable range.
        if self.quantity < 1 or self.quantity > 500:
            raise ValueError("Quantity must be between 1 and 500")

    def get_boxes_required(self, quantity: int | None = None) -> int:
        """
        Determines the number of boxes required for the order.
        A Quantity can be specified, or self.quantity will be
        utilised instead.
        """
        if not quantity:
            quantity = self.quantity

        return math.ceil(quantity/25)

