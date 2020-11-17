from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QSize, Qt


class ItemCard(QWidget):

    def __init__(self, name, path, w, h):

        super().__init__()

        self.vbox = QVBoxLayout()
        self.picture = QLabel()
        self.name = QLabel(name)

        # set values for the card
        self.setPicture(path, w, h)

        # set size and alignement parameters
        self.name.setAlignment(Qt.AlignCenter)

        self.name.setStyleSheet(
            """QLabel { color : gray; 	font:  11pt 'Arial'; font-weight: bold;
                       }""")

        # this one is for items to choose

        # self.picture.setMinimumSize(QSize(70, 55))
        self.picture.setMinimumSize(QSize(w, h))

        self.picture.setMaximumSize(QSize(w, h))

        self.picture.setAlignment(Qt.AlignCenter)

        # structure the widgets
        self.vbox.addWidget(self.picture, alignment=Qt.AlignCenter)
        self.vbox.addWidget(self.name)

        self.setLayout(self.vbox)

    def setName(self, name):

        self.name.setText(name)

    def setPicture(self, path, w, h):

        pic = QPixmap(path)

        pic = pic.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.picture.setPixmap(pic)

    def changePicture(self, path, w, h):

        pic = QPixmap(path)

        pic = pic.scaled(w, h, Qt.IgnoreAspectRatio)

        self.picture.setPixmap(pic)

    def __repr__(self):

        return self.name.text()
