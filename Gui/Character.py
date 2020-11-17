from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QRect, QSize, Qt


class Character(QWidget):

    def __init__(self):

        super().__init__()

        self.vbox = QVBoxLayout()
        self.picture = QLabel()
        self.name = QLabel()

        # set size and alignement parameters
        self.name.setAlignment(Qt.AlignCenter)

        self.name.setStyleSheet(
            """QLabel { color : white; 	font: 75 13pt 'Arial'; font-weight: bold;
                        background-color : #408c99;
                        border-radius:5px;}""")

        self.picture.setAlignment(Qt.AlignCenter)

        # structure the widgets
        self.vbox.addWidget(self.name, alignment=Qt.AlignCenter)

        self.vbox.addWidget(self.picture, alignment=Qt.AlignCenter)

        self.setLayout(self.vbox)

    def setName(self, name):

        self.name.setText(name)

        self.name.setFrameStyle(QFrame.NoFrame)

    def setPicture(self, path):

        pic = QPixmap(path)

        self.picture.setPixmap(pic)
        self.name.setMinimumSize(QSize(110, 20))

    def __repr__(self):

        return self.name.text()
