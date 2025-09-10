# Contains the "Order" class, with every instance tracking a single order.

import math
from datetime import datetime

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
                 quantity: int,
                 start_date: datetime,
                 end_date: datetime) -> None:
        self.receipt_num: int = receipt_num
        self.customer_name: str = customer_name
        self.item_hired: str = item_hired
        self.quantity: int = quantity
        self.start_date: datetime = start_date
        self.end_date: datetime = end_date

        # Checking if the 'Quantity' is within the acceptable range.
        if self.quantity < 1 or self.quantity > 500:
            raise ValueError("Quantity must be between 1 and 500")

        if (self.end_date - self.start_date).days < 0:
            raise ValueError("Start Date must be before or on End Date")

    def get_boxes_required(self, quantity: int | None = None) -> int:
        """
        Determines the number of boxes required for the order.
        A Quantity can be specified, or self.quantity will be
        utilised instead.
        """
        if not quantity:
            quantity = self.quantity

        return math.ceil(quantity/25)

    def get_order_duration_days(self,
                           start_date: datetime | None = None,
                           end_date: datetime | None = None) -> int:
        """
        Gets the number of days the order goes for.
        A Start date & End date can be specified, or self.start_date
        and self.end_date will be utilised instead.
        """
        if not start_date:
            start_date = self.start_date
        if not end_date:
            end_date = self.end_date

        return (end_date - start_date).days

