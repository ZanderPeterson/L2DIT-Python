from datetime import datetime
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit, QMessageBox

from orders import Order

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Party Hire Store — Order Tracker") #Sets the title of the window

        widget_layout = QVBoxLayout() #Defines the overall layout, which is vertical

        input_order_section = QVBoxLayout() #Defines the layout for the input order section, with is vertical

        add_order_label = QLabel("<h1>Create New Order</h1>") #Adds in the New Order Heading
        input_order_section.addWidget(add_order_label) #Adds heading to input order section layout

        #Receipt Number Input
        receipt_number_layout = QHBoxLayout() #Defines a layout for the receipt number portion, which is horizontal

        add_order_label = QLabel("Receipt Number:") #Adds a label indicating the proceeding field is for the Receipt Number
        receipt_number_layout.addWidget(add_order_label) #Adds this label to the receipt number layout

        self.receipt_number_input = QTextEdit() #Creates a text box
        self.receipt_number_input.setFixedSize(200, 28) #Forces the text box to adhere to a specific size
        receipt_number_layout.addWidget(self.receipt_number_input) #Adds the text box to the receipt number layout

        input_order_section.addLayout(receipt_number_layout) #Adds the receipt number layout to the overall input section layout

        #Order Name Input
        order_name_layout = QHBoxLayout() #Defines a layout for the Customer Name portion, which is horizontal

        add_name_label = QLabel("Name:") #Adds a label prompting the user to input the customer's name
        order_name_layout.addWidget(add_name_label) #Adds this label to order name layout

        self.order_name_input = QTextEdit() #Creates a text box
        self.order_name_input.setFixedSize(200, 28) #Forces the text box to be of a specific size
        order_name_layout.addWidget(self.order_name_input) #Adds this text box to the layout

        input_order_section.addLayout(order_name_layout) #Adds the customer name layout to the overall input section layout

        #Item Hired
        item_hired_layout = QHBoxLayout() #Defines a layout for the Item Hired portion, which is horizontal

        item_hired_label = QLabel("Item Hired:") #Adds a label prompting the user to input the Item Hired
        item_hired_layout.addWidget(item_hired_label) #Adds this label to item hired layout

        self.item_hired_input = QTextEdit() #Creates a text box
        self.item_hired_input.setFixedSize(200, 28) #Forces the text box to be of a specific size
        item_hired_layout.addWidget(self.item_hired_input) #Adds this text box to the layout

        input_order_section.addLayout(item_hired_layout) #Adds this layout to the overall input section layout

        #Item Quantity
        item_quantity_layout = QHBoxLayout() #Defines a layout for the Item Quantity portion, which is horizontal

        item_quantity_label = QLabel("Item Quantity:") #Adds a label prompting the user to input the Item Quantity
        item_quantity_layout.addWidget(item_quantity_label) #Adds this label to item quantity layout

        self.item_quantity_input = QTextEdit() #Creates a text box
        self.item_quantity_input.setFixedSize(200, 28) #Forces the text box to be of a specific size
        item_quantity_layout.addWidget(self.item_quantity_input) #Adds this text box to the layout

        input_order_section.addLayout(item_quantity_layout) #Adds this layout to the overall input section layout

        #Order Start Date
        order_start_date_layout = QHBoxLayout() #Defines a layout for the Start Date portion, which is horizontal

        order_start_date_label = QLabel("Item Start Date [DD/MM/YYYY]: ") #Adds a label prompting the user to input the Start Date, and explains how to input
        order_start_date_layout.addWidget(order_start_date_label) #Adds this label to layout

        self.item_start_date_input_days = QTextEdit() #Creates a text box
        self.item_start_date_input_days.setFixedSize(50, 28) #Forces the text box to be of a specific size — this is smaller than most other fields
        order_start_date_layout.addWidget(self.item_start_date_input_days) #Adds this text book to the layout

        self.item_start_date_input_months = QTextEdit() #Creates a text box
        self.item_start_date_input_months.setFixedSize(50, 28) #Forces the text box to be of a specific size — this is smaller than most other fields
        order_start_date_layout.addWidget(self.item_start_date_input_months) #Adds this text book to the layout

        self.item_start_date_input_years = QTextEdit() #Creates a text box
        self.item_start_date_input_years.setFixedSize(50, 28) #Forces the text box to be of a specific size — this is smaller than most other fields
        order_start_date_layout.addWidget(self.item_start_date_input_years) #Adds this text book to the layout

        input_order_section.addLayout(order_start_date_layout) #Adds this layout to the overall input section layout

        #Order End Date
        order_end_date_layout = QHBoxLayout() #Defines a layout for the End Date portion, which is horizontal

        order_end_date_label = QLabel("Item End Date [DD/MM/YYYY]: ") #Adds a label prompting the user to input the End Date, and explains how to input
        order_end_date_layout.addWidget(order_end_date_label) #Adds this label to layout

        self.item_end_date_input_days = QTextEdit() #Creates a text box
        self.item_end_date_input_days.setFixedSize(50, 28) #Forces the text box to be of a specific size — this is smaller than most other fields
        order_end_date_layout.addWidget(self.item_end_date_input_days) #Adds this text book to the layout

        self.item_end_date_input_months = QTextEdit() #Creates a text box
        self.item_end_date_input_months.setFixedSize(50, 28) #Forces the text box to be of a specific size — this is smaller than most other fields
        order_end_date_layout.addWidget(self.item_end_date_input_months) #Adds this text book to the layout

        self.item_end_date_input_years = QTextEdit() #Creates a text box
        self.item_end_date_input_years.setFixedSize(50, 28) #Forces the text box to be of a specific size — this is smaller than most other fields
        order_end_date_layout.addWidget(self.item_end_date_input_years) #Adds this text book to the layout

        input_order_section.addLayout(order_end_date_layout) #Adds this layout to the overall input section layout

        submit_order_selection_button = QPushButton("Submit") #Creates a button
        input_order_section.addWidget(submit_order_selection_button) #Adds the button to the overall input layout
        submit_order_selection_button.clicked.connect(self.submit_order) #Connections the button clicked event to the function "self.submit_order"

        widget_layout.addLayout(input_order_section) #Adds the input section layout to the overall window layout


        #Output
        output_order_section = QVBoxLayout() #Creates the overall layout for the output section

        add_order_label = QLabel("<h1>Get Order(s)</h1>") #Creates a heading for the output section
        input_order_section.addWidget(add_order_label) #Adds that heading to the layout

        print_all_button = QPushButton("Show All Orders") #Creates a button
        output_order_section.addWidget(print_all_button) #Adds button to the layout
        print_all_button.clicked.connect(self.print_all) #Connects the button with the "self.print_all" function

        #Search Tool
        search_by_receipt_layout = QHBoxLayout() #Defines the layout for the search by receipt section

        search_by_receipt_label = QLabel("Search By Receipt:") #Creates a relevant label
        search_by_receipt_layout.addWidget(search_by_receipt_label) #Adds the label to the layout

        self.search_by_receipt_input = QTextEdit() #Creates a text box
        self.search_by_receipt_input.setFixedSize(180, 28) #Forces the text box to be of a specific size
        search_by_receipt_layout.addWidget(self.search_by_receipt_input) #Adds the text box to the layout

        search_by_receipt_button = QPushButton("Search") #Creates a button
        search_by_receipt_layout.addWidget(search_by_receipt_button) #Adds button to the layout
        search_by_receipt_button.clicked.connect(self.search_by_receipt_function) #Connects the button with the "self.search_by_receipt_function" function

        search_by_receipt_delete_button = QPushButton("Del") #Creates a button
        search_by_receipt_layout.addWidget(search_by_receipt_delete_button) #Adds button to the layout
        search_by_receipt_delete_button.clicked.connect(self.search_by_receipt_delete_function) #Connects the button with the "self.search_by_receipt_delete_function" function

        output_order_section.addLayout(search_by_receipt_layout) #Adds this layout to the overall output section layout

        #Search for Raffle Winner Tool
        search_by_raffle_layout = QHBoxLayout() #Defines the layout for the search by raffle section

        search_by_raffle_label = QLabel("Search For Raffle:") #Creates a relevant label
        search_by_raffle_layout.addWidget(search_by_raffle_label) #Adds the label to the layout

        self.search_by_raffle_input = QTextEdit() #Creates a text box
        self.search_by_raffle_input.setFixedSize(180, 28) #Forces the text box to be of a specific size
        search_by_raffle_layout.addWidget(self.search_by_raffle_input) #Adds the text box to the layout

        search_by_raffle_button = QPushButton("Search") #Creates a button
        search_by_raffle_layout.addWidget(search_by_raffle_button) #Adds button to the layout
        search_by_raffle_button.clicked.connect(self.search_by_raffle_function) #Connects the button with the "self.search_by_raffle_function" function

        output_order_section.addLayout(search_by_raffle_layout) #Adds this layout to the overall output section layout


        widget_layout.addLayout(output_order_section) #Adds the output layout section to the overall window layout

        self.setLayout(widget_layout) #Sets the window layout to be the window layout

        self.orders = [] #Creates an empty list where instances of the Order class will be stored

    def submit_order(self) -> None:
        """
        This function takes all the data that the user has entered, validates it,
        and then puts it into an instance of the Order class.
        If data is invalid, this function will give the user the appropriate
        constructive error.
        """
        #This try except loop checks that the dates are numbers
        try:
            start_time = (int(self.item_start_date_input_years.toPlainText()),
                          int(self.item_start_date_input_months.toPlainText()),
                          int(self.item_start_date_input_days.toPlainText()))
            end_time = (int(self.item_end_date_input_years.toPlainText()),
                        int(self.item_end_date_input_months.toPlainText()),
                        int(self.item_end_date_input_days.toPlainText()))
        except ValueError:
            QMessageBox.critical(self, "Order Input Error!",
                                       "Dates provided are not numbers.",
                                       QMessageBox.Ok | QMessageBox.Cancel)
            return

        #If the dates are invalid (e.g. 30th of February), this try/except will catch that.
        try:
            order_to_check = {
                "receipt_number": self.receipt_number_input.toPlainText(),
                "name": self.order_name_input.toPlainText(),
                "item_hired": self.item_hired_input.toPlainText(),
                "item_quantity": self.item_quantity_input.toPlainText(),
                "start_date": datetime(start_time[0], start_time[1], start_time[2]),
                "end_date": datetime(end_time[0], end_time[1], end_time[2])
            }
        except ValueError:
            QMessageBox.critical(self, "Order Input Error!",
                                 "Dates are invalid",
                                 QMessageBox.Ok | QMessageBox.Cancel)
            return

        #This try/except loop checks that the Receipt Number is an integer
        try:
            order_to_check["receipt_number"] = int(order_to_check["receipt_number"])
        except ValueError:
            QMessageBox.critical(self, "Order Input Error!",
                                 "Receipt Number is not a valid number",
                                 QMessageBox.Ok | QMessageBox.Cancel)
            return

        #This try/except loop checks that the Item Quantity is an integer
        try:
            order_to_check["item_quantity"] = int(order_to_check["item_quantity"])
        except ValueError:
            QMessageBox.critical(self, "Order Input Error!",
                                 "Item Quantity is not a valid number",
                                 QMessageBox.Ok | QMessageBox.Cancel)
            return

        #This try/except loop catches the errors that the Order class may throw.
        #These errors include Quantity being out of the valid bounds, and the
        #start date falling after the end date.
        try:
            created_order = Order(order_to_check["receipt_number"],
                                  order_to_check["name"],
                                  order_to_check["item_hired"],
                                  order_to_check["item_quantity"],
                                  order_to_check["start_date"],
                                  order_to_check["end_date"])
        except ValueError as exception:
            if "Quantity must be between 1 and 500" in str(exception):
                QMessageBox.critical(self, "Order Input Error!",
                                     "Item Quantity is between 1 and 500",
                                     QMessageBox.Ok | QMessageBox.Cancel)
                return
            if "Start Date must be before or on End Date" in str(exception):
                QMessageBox.critical(self, "Order Input Error!",
                                     "Start Date is after End Date",
                                     QMessageBox.Ok | QMessageBox.Cancel)
                return
            return

        #User feedback showed that there should be more feedback on hitting the "Submit" button,
        #hence the print statement.
        print(f"Order {created_order.receipt_num} successfully submitted!")
        self.orders.append(created_order)

    def print_all(self):
        """Prints every single order to the console"""
        for order in self.orders:
            print("—— —— —— —— —— —— —— —— —— ——") #This acts to visually separate the different orders
            order.print_order() #Calls upon a function in the Order class that prints all the relevant data.
        print("—— —— —— —— —— —— —— —— —— ——")

    def search_by_receipt_function(self):
        """Searches through all orders to find a match for the receipt number."""
        #This try/except loop checks that the Receipt Number to Search for is an integer
        try:
            receipt_num_to_search = int(self.search_by_receipt_input.toPlainText())
        except ValueError:
            QMessageBox.critical(self, "Search Input Error!",
                                 "Invalid number to search",
                                 QMessageBox.Ok | QMessageBox.Cancel)
            return

        #Iterates over every order in the list and finds the matching receipt number, if one exists.
        for i, order in enumerate(self.orders):
            if order.receipt_num == receipt_num_to_search:
                order.print_order()
                break
        else:
            QMessageBox.warning(self, "Search Problem!",
                                f"No match was found for {receipt_num_to_search}",
                                QMessageBox.Ok | QMessageBox.Cancel)

    def search_by_receipt_delete_function(self):
        """Searches through all orders to find a match for the receipt number, then deletes the matching order"""
        #This try/except loop checks that the Receipt Number to Search for is an integer
        try:
            receipt_num_to_search = int(self.search_by_receipt_input.toPlainText())
        except ValueError:
            QMessageBox.critical(self, "Search Input Error!",
                                 "Invalid number to search",
                                 QMessageBox.Ok | QMessageBox.Cancel)
            return

        #Iterates over every order in the list and finds the matching receipt number, if one exists.
        for i, order in enumerate(self.orders):
            if order.receipt_num == receipt_num_to_search:
                print(f"Deleting {order.receipt_num}...")
                order.deleted = True
                print("—— —— —— —— —— —— —— —— —— ——")
                break
        else:
            QMessageBox.warning(self, "Search Problem!",
                                f"No match was found for {receipt_num_to_search}",
                                QMessageBox.Ok | QMessageBox.Cancel)

    def search_by_raffle_function(self):
        """
        Searches through all orders to find a match for the raffle number.
        Multiple orders may have the winning raffle number.
        """
        #This try/except loop checks that the Raffle Number to Search for is an integer
        try:
            search_by_raffle_input = int(self.search_by_raffle_input.toPlainText())
        except ValueError:
            QMessageBox.critical(self, "Search Input Error!",
                                 "Invalid number to search",
                                 QMessageBox.Ok | QMessageBox.Cancel)
            return

        # Iterates over every order in the list and finds the matching raffle number(s), if one exists.
        valid_raffle_tickets = 0
        for order in self.orders:
            if order.raffle_number == search_by_raffle_input:
                valid_raffle_tickets = valid_raffle_tickets + 1
                print("—— —— —— —— —— —— —— —— —— ——")
                order.print_order()
        QMessageBox.about(self, "Raffle Search Results",
                               f"Found {valid_raffle_tickets} order(s) with the number of {search_by_raffle_input}")
