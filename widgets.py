from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit

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

        receipt_number_input = QTextEdit()
        receipt_number_input.setFixedSize(200, 20)
        receipt_number_layout.addWidget(receipt_number_input)

        input_order_section.addLayout(receipt_number_layout)

        #Order Name Input
        order_name_layout = QHBoxLayout()

        add_name_label = QLabel("Name:")
        order_name_layout.addWidget(add_name_label)

        order_name_input = QTextEdit()
        order_name_input.setFixedSize(200, 20)
        order_name_layout.addWidget(order_name_input)

        input_order_section.addLayout(order_name_layout)

        #Item Hired
        item_hired_layout = QHBoxLayout()

        item_hired_label = QLabel("Item Hired:")
        item_hired_layout.addWidget(item_hired_label)

        item_hired_input = QTextEdit()
        item_hired_input.setFixedSize(200, 20)
        item_hired_layout.addWidget(item_hired_input)

        input_order_section.addLayout(item_hired_layout)

        #Item Quantity
        item_quantity_layout = QHBoxLayout()

        item_quantity_label = QLabel("Item Quantity:")
        item_quantity_layout.addWidget(item_quantity_label)

        item_quantity_input = QTextEdit()
        item_quantity_input.setFixedSize(200, 20)
        item_quantity_layout.addWidget(item_quantity_input)

        input_order_section.addLayout(item_quantity_layout)

        #Order Start Date
        order_start_date_layout = QHBoxLayout()

        order_start_date_label = QLabel("Item Start Date [DD/MM/YYYY]: ")
        order_start_date_layout.addWidget(order_start_date_label)

        item_start_date_input_days = QTextEdit()
        item_start_date_input_days.setFixedSize(50, 20)
        order_start_date_layout.addWidget(item_start_date_input_days)

        item_start_date_input_months = QTextEdit()
        item_start_date_input_months.setFixedSize(50, 20)
        order_start_date_layout.addWidget(item_start_date_input_months)

        item_start_date_input_years = QTextEdit()
        item_start_date_input_years.setFixedSize(50, 20)
        order_start_date_layout.addWidget(item_start_date_input_years)

        input_order_section.addLayout(order_start_date_layout)

        #Order End Date
        order_end_date_layout = QHBoxLayout()

        order_end_date_label = QLabel("Item End Date [DD/MM/YYYY]: ")
        order_end_date_layout.addWidget(order_end_date_label)

        item_end_date_input_days = QTextEdit()
        item_end_date_input_days.setFixedSize(50, 20)
        order_end_date_layout.addWidget(item_end_date_input_days)

        item_end_date_input_months = QTextEdit()
        item_end_date_input_months.setFixedSize(50, 20)
        order_end_date_layout.addWidget(item_end_date_input_months)

        item_end_date_input_years = QTextEdit()
        item_end_date_input_years.setFixedSize(50, 20)
        order_end_date_layout.addWidget(item_end_date_input_years)

        input_order_section.addLayout(order_end_date_layout)

        submit_order_selection_button = QPushButton("Submit")
        input_order_section.addWidget(submit_order_selection_button)

        self.setLayout(input_order_section)
