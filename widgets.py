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

        self.setLayout(input_order_section)
