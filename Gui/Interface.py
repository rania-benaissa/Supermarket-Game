# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui/interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1920, 1079)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 4243434))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.historiqueTable = QtWidgets.QTableWidget(self.centralwidget)
        self.historiqueTable.setGeometry(QtCore.QRect(920, 710, 970, 320))
        self.historiqueTable.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.historiqueTable.setStyleSheet("QTableView{\n"
"    border-radius: 5px;\n"
"    border: 3px solid #408c99;\n"
"}\n"
"QScrollBar:vertical {\n"
"   \n"
"    background: #F5F5F5;\n"
"    width: 15px;\n"
"  \n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    border-radius: 7px;\n"
"    background: #D3D3D3;\n"
"     width: 15px;\n"
" \n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    border-radius: 7px;\n"
"    background: #808080;\n"
"     width: 15px;\n"
" \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"      border: none;\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"      border: none;\n"
"      background: none;\n"
"}\n"
"QTableWidget ::section { \n"
"  border-radius: 2px;\n"
"color :#696969;     font:  13pt \'Arial\'; font-weight: bold;  border-top: 0px solid #d6d9dc;;\n"
"border-left: 0px solid #d6d9dc;;\n"
"border-right: 0px solid #d6d9dc;;\n"
" border-bottom: 1px solid #d6d9dc;\n"
"height: 40px; } \n"
"\n"
"QTableView::item {border-bottom: 1px solid #d6d9dc;}")
        self.historiqueTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.historiqueTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.historiqueTable.setShowGrid(False)
        self.historiqueTable.setObjectName("historiqueTable")
        self.historiqueTable.setColumnCount(0)
        self.historiqueTable.setRowCount(0)
        self.historiqueTable.horizontalHeader().setDefaultSectionSize(200)
        self.historiqueTable.horizontalHeader().setHighlightSections(True)
        self.historiqueTable.horizontalHeader().setMinimumSectionSize(200)
        self.historiqueTable.verticalHeader().setVisible(False)
        self.historiqueTable.verticalHeader().setHighlightSections(False)
        self.itemToChoose = QtWidgets.QListWidget(self.centralwidget)
        self.itemToChoose.setGeometry(QtCore.QRect(20, 700, 600, 170))
        self.itemToChoose.setMinimumSize(QtCore.QSize(600, 170))
        self.itemToChoose.setMaximumSize(QtCore.QSize(420, 105))
        self.itemToChoose.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.itemToChoose.setStyleSheet("QAbstractScrollArea {\n"
"    border-radius: 5px;\n"
"    border: 3px solid #408c99;\n"
"}\n"
"QScrollBar:horizontal {\n"
"   \n"
"    background: #F5F5F5;\n"
"    height: 15px;\n"
"  \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    border-radius: 7px;\n"
"    background: #D3D3D3;\n"
"     width: 10px;\n"
" \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"    border-radius: 7px;\n"
"    background: #808080;\n"
"     width: 10px;\n"
" \n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: none;\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: none;\n"
"      background: none;\n"
"}")
        self.itemToChoose.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.itemToChoose.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.itemToChoose.setFlow(QtWidgets.QListView.LeftToRight)
        self.itemToChoose.setObjectName("itemToChoose")
        self.customersCombo = QtWidgets.QComboBox(self.centralwidget)
        self.customersCombo.setGeometry(QtCore.QRect(920, 665, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.customersCombo.setFont(font)
        self.customersCombo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.customersCombo.setStyleSheet("QListView { color: #696969;}\n"
"QComboBox{ color : #696969;padding-left:  20px;  border-radius: 5px;\n"
"    border: 3px solid #408c99;}\n"
"\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(Data/Assets/items/down-arrow.png);\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    padding-right:  20px;\n"
"}\n"
"QComboBox::drop-down \n"
"{\n"
"    border: 0px;\n"
"}")
        self.customersCombo.setObjectName("customersCombo")
        self.itemsToBuy = QtWidgets.QListWidget(self.centralwidget)
        self.itemsToBuy.setGeometry(QtCore.QRect(1200, 193, 600, 170))
        self.itemsToBuy.setMinimumSize(QtCore.QSize(600, 170))
        self.itemsToBuy.setMaximumSize(QtCore.QSize(420, 110))
        self.itemsToBuy.setStyleSheet("QAbstractScrollArea {\n"
"    border-radius: 5px;\n"
"    border: 3px solid #408c99;\n"
"}\n"
"QScrollBar:horizontal {\n"
"   \n"
"    background: #F5F5F5;\n"
"    height: 15px;\n"
"  \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    border-radius: 7px;\n"
"    background: #D3D3D3;\n"
"     width: 10px;\n"
" \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"    border-radius: 7px;\n"
"    background: #808080;\n"
"     width: 10px;\n"
" \n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: none;\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: none;\n"
"      background: none;\n"
"}")
        self.itemsToBuy.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.itemsToBuy.setFlow(QtWidgets.QListView.LeftToRight)
        self.itemsToBuy.setObjectName("itemsToBuy")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(190, 900, 250, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.submitButton.setFont(font)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setStyleSheet("QPushButton {\n"
"\n"
"            background:linear-gradient(to bottom, #599bb3 5%, #408c99 100%);\n"
"            background-color:#599bb3;\n"
"            border-radius:8px;\n"
"            color:#ffffff;\n"
"            padding:15px 15px;\n"
"            text-decoration:none;\n"
"           \n"
"        }\n"
"        QPushButton:hover {\n"
"            background:linear-gradient(to bottom, #408c99 5%, #599bb3 100%);\n"
"            background-color:#408c99;\n"
"        }\n"
"        QPushButton:active {\n"
"            position:relative;\n"
"            top:1px;\n"
"        }")
        self.submitButton.setObjectName("submitButton")
        self.correctItems = QtWidgets.QListWidget(self.centralwidget)
        self.correctItems.setGeometry(QtCore.QRect(50, 200, 600, 170))
        self.correctItems.setMinimumSize(QtCore.QSize(600, 170))
        self.correctItems.setMaximumSize(QtCore.QSize(420, 110))
        self.correctItems.setStyleSheet("QAbstractScrollArea {\n"
"    border-radius: 5px;\n"
"    border: 3px solid #408c99;\n"
"}\n"
"QScrollBar:horizontal {\n"
"   \n"
"    background: #F5F5F5;\n"
"    height: 15px;\n"
"  \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    border-radius: 7px;\n"
"    background: #D3D3D3;\n"
"     width: 10px;\n"
" \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"    border-radius: 7px;\n"
"    background: #808080;\n"
"     width: 10px;\n"
" \n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: none;\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: none;\n"
"      background: none;\n"
"}")
        self.correctItems.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.correctItems.setFlow(QtWidgets.QListView.LeftToRight)
        self.correctItems.setObjectName("correctItems")
        self.score_icon = QtWidgets.QLabel(self.centralwidget)
        self.score_icon.setGeometry(QtCore.QRect(60, 30, 110, 150))
        self.score_icon.setStyleSheet("")
        self.score_icon.setTextFormat(QtCore.Qt.PlainText)
        self.score_icon.setObjectName("score_icon")
        self.mainGame = QtWidgets.QWidget(self.centralwidget)
        self.mainGame.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.mainGame.setAutoFillBackground(False)
        self.mainGame.setObjectName("mainGame")
        self.startButton = QtWidgets.QPushButton(self.mainGame)
        self.startButton.setGeometry(QtCore.QRect(800, 500, 300, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.startButton.setFont(font)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setStyleSheet("QPushButton {\n"
"            background:linear-gradient(to bottom, #599bb3 5%, #408c99 100%);\n"
"            background-color:#599bb3;\n"
"            border-radius:8px;\n"
"            color:#ffffff;\n"
"            padding:15px 15px;\n"
"            text-decoration:none;\n"
"           \n"
"        }\n"
"        QPushButton:hover {\n"
"            background:linear-gradient(to bottom, #408c99 5%, #599bb3 100%);\n"
"            background-color:#408c99;\n"
"        }\n"
"        QPushButton:active {\n"
"            position:relative;\n"
"            top:1px;\n"
"        }")
        self.startButton.setObjectName("startButton")
        self.character = QtWidgets.QWidget(self.centralwidget)
        self.character.setGeometry(QtCore.QRect(600, 450, 381, 551))
        self.character.setObjectName("character")
        self.dialogue = QtWidgets.QLabel(self.centralwidget)
        self.dialogue.setGeometry(QtCore.QRect(900, 200, 371, 241))
        self.dialogue.setStyleSheet("")
        self.dialogue.setText("")
        self.dialogue.setScaledContents(False)
        self.dialogue.setObjectName("dialogue")
        self.text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(920, 250, 231, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text.setFont(font)
        self.text.setAutoFillBackground(False)
        self.text.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.text.setReadOnly(True)
        self.text.setBackgroundVisible(False)
        self.text.setObjectName("text")
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(140, 90, 150, 50))
        self.score.setStyleSheet(" border-radius: 5px;\n"
" border: 3px solid #408c99;\n"
"background-color : white;\n"
" color : gray;     font:  13pt \'Arial\'; \n"
"font-weight: bold;\n"
"                       \n"
"")
        self.score.setTextFormat(QtCore.Qt.PlainText)
        self.score.setAlignment(QtCore.Qt.AlignCenter)
        self.score.setObjectName("score")
        self.next = QtWidgets.QWidget(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(1190, 450, 451, 191))
        self.next.setObjectName("next")
        self.nextButton = QtWidgets.QPushButton(self.next)
        self.nextButton.setGeometry(QtCore.QRect(90, 79, 131, 91))
        self.nextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton.setAutoFillBackground(False)
        self.nextButton.setStyleSheet("QPushButton{background-color: rgba(255, 255, 255, 0);\n"
"\n"
"   border-image: url(\"Data/Assets/items/next.png\"); \n"
"   border-width: 0px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   \n"
"   border-image: url(\"Data/Assets/items/hover_next.png\"); \n"
"   border-width: 0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   \n"
"   border-image: url(\"Data/Assets/items/click_next.png\"); \n"
"   border-width: 0px;\n"
"\n"
"}")
        self.nextButton.setText("")
        self.nextButton.setObjectName("nextButton")
        self.lab = QtWidgets.QLabel(self.next)
        self.lab.setGeometry(QtCore.QRect(50, 10, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lab.setFont(font)
        self.lab.setStyleSheet("color:rgb(255, 255, 255)")
        self.lab.setAlignment(QtCore.Qt.AlignCenter)
        self.lab.setObjectName("lab")
        self.dialogue.raise_()
        self.text.raise_()
        self.character.raise_()
        self.score.raise_()
        self.score_icon.raise_()
        self.itemsToBuy.raise_()
        self.customersCombo.raise_()
        self.historiqueTable.raise_()
        self.itemToChoose.raise_()
        self.submitButton.raise_()
        self.correctItems.raise_()
        self.mainGame.raise_()
        self.next.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My Game"))
        self.submitButton.setText(_translate("MainWindow", "Submit selection"))
        self.score_icon.setText(_translate("MainWindow", "Score"))
        self.startButton.setText(_translate("MainWindow", "Start Game"))
        self.text.setPlainText(_translate("MainWindow", "wcwsvcwc  dqsgsdgdsgsgsdgsdgsgsdgsgsgsdgsdgsgsgsgddddddddddddddddddqsdqsd\n"
""))
        self.score.setText(_translate("MainWindow", "0"))
        self.lab.setText(_translate("MainWindow", "NEXT CLIENT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

