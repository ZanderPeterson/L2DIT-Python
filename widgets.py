from datetime import datetime
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Party Hire Store — Order Tracker")

        input_order_section = QVBoxLayout()

        add_order_label = QLabel("<h1>Create New Order</h1>")
        input_order_section.addWidget(add_order_label)

        #Receipt Number Input
        receipt_number_layout = QHBoxLayout()

        add_order_label = QLabel("Receipt Number:")
        receipt_number_layout.addWidget(add_order_label)

        self.receipt_number_input = QTextEdit()
        self.receipt_number_input.setFixedSize(200, 28)
        receipt_number_layout.addWidget(self.receipt_number_input)

        input_order_section.addLayout(receipt_number_layout)

        #Order Name Input
        order_name_layout = QHBoxLayout()

        add_name_label = QLabel("Name:")
        order_name_layout.addWidget(add_name_label)

        self.order_name_input = QTextEdit()
        self.order_name_input.setFixedSize(200, 28)
        order_name_layout.addWidget(self.order_name_input)

        input_order_section.addLayout(order_name_layout)

        #Item Hired
        item_hired_layout = QHBoxLayout()

        item_hired_label = QLabel("Item Hired:")
        item_hired_layout.addWidget(item_hired_label)

        self.item_hired_input = QTextEdit()
        self.item_hired_input.setFixedSize(200, 28)
        item_hired_layout.addWidget(self.item_hired_input)

        input_order_section.addLayout(item_hired_layout)

        #Item Quantity
        item_quantity_layout = QHBoxLayout()

        item_quantity_label = QLabel("Item Quantity:")
        item_quantity_layout.addWidget(item_quantity_label)

        self.item_quantity_input = QTextEdit()
        self.item_quantity_input.setFixedSize(200, 28)
        item_quantity_layout.addWidget(self.item_quantity_input)

        input_order_section.addLayout(item_quantity_layout)

        #Order Start Date
        order_start_date_layout = QHBoxLayout()

        order_start_date_label = QLabel("Item Start Date [DD/MM/YYYY]: ")
        order_start_date_layout.addWidget(order_start_date_label)

        self.item_start_date_input_days = QTextEdit()
        self.item_start_date_input_days.setFixedSize(50, 28)
        order_start_date_layout.addWidget(self.item_start_date_input_days)

        self.item_start_date_input_months = QTextEdit()
        self.item_start_date_input_months.setFixedSize(50, 28)
        order_start_date_layout.addWidget(self.item_start_date_input_months)

        self.item_start_date_input_years = QTextEdit()
        self.item_start_date_input_years.setFixedSize(50, 28)
        order_start_date_layout.addWidget(self.item_start_date_input_years)

        input_order_section.addLayout(order_start_date_layout)

        #Order End Date
        order_end_date_layout = QHBoxLayout()

        order_end_date_label = QLabel("Item End Date [DD/MM/YYYY]: ")
        order_end_date_layout.addWidget(order_end_date_label)

        self.item_end_date_input_days = QTextEdit()
        self.item_end_date_input_days.setFixedSize(50, 28)
        order_end_date_layout.addWidget(self.item_end_date_input_days)

        self.item_end_date_input_months = QTextEdit()
        self.item_end_date_input_months.setFixedSize(50, 28)
        order_end_date_layout.addWidget(self.item_end_date_input_months)

        self.item_end_date_input_years = QTextEdit()
        self.item_end_date_input_years.setFixedSize(50, 28)
        order_end_date_layout.addWidget(self.item_end_date_input_years)

        input_order_section.addLayout(order_end_date_layout)

        submit_order_selection_button = QPushButton("Submit")
        input_order_section.addWidget(submit_order_selection_button)
        submit_order_selection_button.clicked.connect(self.submit_order)

        self.setLayout(input_order_section)

    def submit_order(self):
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
        print(order_to_check)
