# Contains the "Order" class, with every instance tracking a single order.

from datetime import datetime
import math
import random

class Order():
    """
    A Class which will have one instance per order, and tracks various
    order-specific bits of information, such as start/end dates, customer
    name, receipt number, the item, the quantity, raffle info, etc. etc.
    """
    BOX_CAPACITY: int = 25

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
        self.raffle_number: int = random.randint(1, 1000)
        self.deleted: bool = False

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

        #The following equation has been tested to meet the requirement of giving
        #the number of boxes required. At 24 boxes, one is required. 25 also one.
        #at 26 this number jumps to 2. This always gives a whole number.
        return math.ceil(quantity/self.BOX_CAPACITY)

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

        return (end_date - start_date).days #Gets the difference in days

    def print_order(self, print_deleted: bool = False):
        """Prints all the details of the order to console"""
        if (print_deleted and self.deleted) or ((not self.deleted) and (not self.deleted)):
            print(f"Receipt Number: {self.receipt_num}\n" +
                  f"Customer Name:  {self.customer_name}\n" +
                  f"Item Hired:     {self.item_hired}\n" +
                  f"Item Quantity   {self.quantity} ({self.get_boxes_required()} boxes required)\n" +
                  f"Starting Date:  {self.start_date.day}/{self.start_date.month}/{self.start_date.year}\n" +
                  f"Ending Date:    {self.end_date.day}/{self.end_date.month}/{self.end_date.year}\n" +
                  f"Order Duration: {self.get_order_duration_days()} days\n" +
                  f"Raffle Number:  {self.raffle_number}")
        else:
            print(f"Item {self.receipt_num} Previously Deleted")
