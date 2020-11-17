from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget
from PyQt5.QtCore import Qt


class TransactionWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.hbox = QHBoxLayout()

        # structure the widgets

        self.setLayout(self.hbox)

    def addElement(self, widget):

        self.hbox.addWidget(widget, alignment=Qt.AlignCenter)
