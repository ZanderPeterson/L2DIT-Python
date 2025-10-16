from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Party Hire Store — Order Tracker")

        input_order_section = QVBoxLayout()

        add_order_label = QLabel("<h1>Create New Order</h1>")
        input_order_section.addWidget(add_order_label)

        self.setLayout(input_order_section)
