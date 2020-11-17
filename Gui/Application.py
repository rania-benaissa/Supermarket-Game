import sys
sys.path.append('D:/M1/S2/DM/project/')
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QDesktopWidget, QFrame, QHBoxLayout, QHeaderView, QLabel, QTableWidgetItem, QVBoxLayout, QWidget
from Gui.Character import Character
from Algorithm.aPrioriAlgorithm import aPrioriAlgorithm
import pandas as pd
from random import randint, shuffle, choice
from Gui.TransactionWidget import TransactionWidget
from Gui.ItemCard import ItemCard
from PyQt5.QtCore import QParallelAnimationGroup, QPropertyAnimation, QRect, QSequentialAnimationGroup, QSize, Qt 
from PyQt5.QtGui import QBrush, QColor, QImage, QPalette, QPixmap
from pydub import AudioSegment
import pygame
from Gui.Interface import Ui_MainWindow  # importing our generated file
from PyQt5 import QtCore, QtGui, QtWidgets


# set screen BG
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()


def setBackground(wid, name):

    image = QtGui.QPixmap()
    image.load(name)
    image = image.scaled(wid.width(), wid.height())
    # Palette
    palette = QtGui.QPalette()
    palette.setBrush(wid.backgroundRole(), QtGui.QBrush(image))
    wid.setPalette(palette)


class mywindow(QtWidgets.QMainWindow):

    # to center the screen
    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(
            QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def maximizeWindow(self):
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)

        myscreen = QApplication.desktop()
        width = myscreen.width()
        height = myscreen.height()
        self.setFixedSize(width, height)

    def __init__(self):

        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.maximizeWindow()

        # INITIALISATIONS

        self.initGame()

      

    def setWidgetsStyle(self):

        # main windows configuration
        setBackground(self, "Data\Assets\supermarket.jpg")
        self.center()

        # remove bg and border
        self.ui.text.viewport().setAutoFillBackground(False)
        self.ui.text.setFrameStyle(QFrame.NoFrame)



        # set bubble image
        self.ui.dialogue.setPixmap(QPixmap("Data/Assets/items/bubble_chat.png").scaled(self.ui.dialogue.width(), self.ui.dialogue.height(),
                                                                                       Qt.KeepAspectRatio, Qt.SmoothTransformation))

        # set score image
        self.ui.score_icon.setPixmap(QPixmap("Data/Assets/items/money.png").scaled(108,150))

       
        # initially hide those widgets
        self.ui.itemToChoose.hide()
        self.ui.correctItems.hide()
        self.ui.itemsToBuy.hide()
        self.ui.submitButton.hide()
        self.ui.next.hide()  
                

    def initGame(self):

        # make a better view
        self.setWidgetsStyle()

        self.ui.submitButton.setEnabled(False)
        # get items and customers for csv files
        self.items = pd.read_csv('Data/items.csv', delimiter=',')
        # reecupere les clients du fichier Csv
        self.customers = self.getCustomers()
        self.purchases = pd.read_csv('Data/transactions.csv', sep=',')

        # lunch a priori algorithm
        self.apriori = aPrioriAlgorithm(
            self.purchases, self.items, 0.01, 1, 50)
        self.apriori.run()
        self.textCorrect = ["Thanks for your help !",
                            "Thank you, now i can cook yummy dishes !", "You guessed well !\n thank you"]

        self.textIncorrect = ["I wish you could help me out !",
                              "Noo, now my daughter will be disappointed"]

        # add customers to comboBox
        self.ui.customersCombo.addItems([row[0] for row in self.customers])

        self.ui.historiqueTable = self.createTable()

        # create a character
        self.character = Character()
        self.ui.character.setLayout(self.character.vbox)

        # show game starter
        self.ui.mainGame.setAutoFillBackground(True)
        setBackground(self.ui.mainGame, "Data\Assets\supermarket.jpg")

        # set score value
        self.score = 0

        # SIGNALS
        self.ui.startButton.clicked.connect(self.startGame)
        self.ui.customersCombo.currentIndexChanged.connect(self.changeCustomer)

        self.ui.itemToChoose.itemSelectionChanged.connect(self.selectItems)

        self.ui.nextButton.clicked.connect(self.nextClient)
        self.ui.submitButton.clicked.connect(
            lambda: self.submitSelection(self.selected))

        self.ui.submitButton.released.connect(self.playSound)
        self.ui.nextButton.released.connect(self.playSound)
        self.ui.startButton.released.connect(self.playSound)


        # start playing the background music
        pygame.mixer.music.load("Data/Assets/audio/music.mp3")
        pygame.mixer.music.play(loops=-1) 



    def playSound(self):

        pygame.mixer.find_channel().play(pygame.mixer.Sound("Data/Assets/audio/button_click.ogg"))

    def nextClient(self):

        self.resetGame()

        self.startGame()

    def getCustomers(self):

        df = pd.read_csv('Data/customers.csv', delimiter=',')

        # Create a list of tuples for Dataframe rows using list comprehension
        return [tuple(row) for row in df.values]

    # create transactions table
    def createTable(self):

        table = self.ui.historiqueTable

        # setting shape
        table.setColumnCount(1)

        # those two lines are to make the columns fit the widget
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        table.horizontalHeader().setStretchLastSection(True)

        # insert horiz header
        table.setHorizontalHeaderLabels(["Transactions"])

        # populate table with first customers values
        self.populateTable(self.customers[0][0])

        return table

    # populate transactions table
    def populateTable(self, name):

        # pour chaque transaction si elle appartient a name
        rows = self.purchases.loc[self.purchases['name'] == name]

        if(not rows.empty):

            self.ui.historiqueTable.setRowCount(len(rows))

            # loop through the "name"'s transactions
            for i in range(0, len(rows)):

                widget = TransactionWidget()

                for j in range(0, len(rows.columns)):

                    # get item
                    value = self.items.loc[self.items['name']
                                           == rows.iloc[i, j]]

                    if(not value.empty):

                        item = ItemCard(
                            value.iloc[0, 0], value.iloc[0, 1], 55, 55)

                        widget.addElement(item)

                # add transaction to table

                self.ui.historiqueTable.setCellWidget(i, 0, widget)

            self.ui.historiqueTable.resizeRowsToContents()

    # change customer in the ComboBox
    def changeCustomer(self):

        # get the current selected customer
        name = self.ui.customersCombo.currentText()

        # populate from scratch custumor's transactions table
        self.ui.historiqueTable.setRowCount(0)
        self.populateTable(name)

    # populate list of items to guess
    def populateItemsToBuy(self, nb):

        itemList = self.ui.itemsToBuy

        # get the apprpriate association rule
        rule = self.apriori.assocRules[nb]

        # add antecedents
        self.addItems(rule.antecedent, itemList)

        # add unknown items
        self.addUnknownItems(rule.consequent, itemList)

        # then we populate items to choose
        self.populateItemsToChoose(rule)

        # then populate correct items
        self.populateCorrectItems(rule)

        self.nbRuleConsequent = len(rule.consequent)

    # populate list of items to choose
    def populateItemsToChoose(self, rule):

        itemList = []

        # nombre d'items random a mettre
        nbRandom = 10 - len(rule.consequent)

        # this is to get random item's names
        for i in range(0, nbRandom):

            value = randint(0, len(self.items) - 1)

            # si l item existe deja dans la liste ou fait partie des consequents ou des antecedants
            while self.items.iloc[value, 0] in itemList or self.items.iloc[value, 0] in rule.consequent or self.items.iloc[value, 0] in rule.antecedent:
                value = randint(0, len(self.items) - 1)

            itemList.append(self.items.iloc[value, 0])

        # get the necessary consequents
        for element in rule.consequent:
            itemList.append(element)

        # shuffle the list
        shuffle(itemList)

        # now we display the list values
        self.addItems(itemList, self.ui.itemToChoose)

    # populate the correct items list
    def populateCorrectItems(self, rule):

        self.addItems(rule.antecedent, self.ui.correctItems)
        self.addItems(rule.consequent, self.ui.correctItems)

    # add items to a list
    def addItems(self, itemList, listWidget):

        for element in itemList:

            # search for the items in dataframe
            value = self.items.loc[self.items['name']
                                   == element]

            # create an item card
            item = ItemCard(
                value.iloc[0, 0], value.iloc[0, 1], 110, 80)

            widgetItem = QtWidgets.QListWidgetItem(listWidget)
            # Set size hint
            widgetItem.setSizeHint(item.sizeHint())

            # Add QListWidgetItem into QListWidget
            listWidget.addItem(widgetItem)
            listWidget.setItemWidget(
                widgetItem, item)

    # add unknown items to a list
    def addUnknownItems(self, itemList, listWidget):
        # add unknow items
        for element in itemList:

            item = ItemCard("Unknown", "Data/Assets/items/unknown.png", 110, 80)

            widgetItem = QtWidgets.QListWidgetItem(listWidget)

            # Set size hint
            widgetItem.setSizeHint(item.sizeHint())

            # Add QListWidgetItem into QListWidget
            listWidget.addItem(widgetItem)
            listWidget.setItemWidget(
                widgetItem, item)

    # choose the items from the liste
    def selectItems(self):

        # get selected items
        items = self.ui.itemToChoose.selectedItems()

        self.selected = []

        # convert them into text
        for item in items:

            self.selected.append(str(self.ui.itemToChoose.itemWidget(item)))

        if(len(self.selected) != self.nbRuleConsequent):

            self.ui.submitButton.setEnabled(False)
        else:

            self.ui.submitButton.setEnabled(True)

    # submit button signal
    def submitSelection(self, items):

        correct = False
       
        self.ui.correctItems.show()
        self.ui.submitButton.setEnabled(False)
        self.ui.itemToChoose.setEnabled(False)

        for i in range(0, self.nbRuleConsequent):
            # remove the last item
            self.ui.itemsToBuy.takeItem(len(self.ui.itemsToBuy) - 1)

        index = len(self.ui.itemsToBuy)

        # add the selected items
        self.addItems(items, self.ui.itemsToBuy)

        itemsToBuy = []

        correctItems = []

        for i in range(index, len(self.ui.itemsToBuy)):

            itemsToBuy.append(str(self.ui.itemsToBuy.itemWidget(
                self.ui.itemsToBuy.item(i))))

            correctItems.append(str(self.ui.correctItems.itemWidget(
                self.ui.correctItems.item(i))))

        for i in range(0, len(itemsToBuy)):

            if itemsToBuy[i] in correctItems:

                self.ui.itemsToBuy.item(index).setBackground(QColor("#7DCEA0"))
                self.score += 200
                correct = True
            else:
                self.ui.itemsToBuy.item(index).setBackground(QColor("#F1948A"))

            index += 1

        self.ui.score.setText(str(self.score))

        if(correct):
            self.ui.text.setPlainText(choice(self.textCorrect))
            pygame.mixer.find_channel().play(pygame.mixer.Sound('Data/Assets/audio/victory.ogg'))

        else:
            self.ui.text.setPlainText(choice(self.textIncorrect))
            pygame.mixer.find_channel().play(pygame.mixer.Sound('Data/Assets/audio/gameover.wav'))

        self.animate2.start()

        # show the next button
        self.ui.next.show()

    # choose a random character and animate it
    def chooseACharacter(self):

        # choose a random character
        char = randint(0, 5)

        self.character.setName(self.customers[char][0])
        self.character.setPicture(self.customers[char][1])

        w = self.character.vbox.sizeHint().width()
        h = self.character.vbox.sizeHint().height()


        # 450, 350, 300, 400

        x = 630
          
        if( self.customers[char][0] == "Nani Lola" or self.customers[char][0] == "Sophie" or self.customers[char][0] =="Jane"):
            y = 950 - h
        else:
            y = 1000 - h

        self.ui.character.move(x, y)

        self.ui.character.setGeometry(QRect(x, y, 0, h))

        self.animation = self.animate(self.ui.character, 0, h, w, h)

        self.ui.customersCombo.setCurrentIndex(char)

        

    # animate according to width or height
    def animate(self, wid, wInit, hInit, w, h):

        anim = QPropertyAnimation(wid, b'geometry')
        anim.setDuration(800)
        anim.setStartValue(
            QRect(wid.x(), wid.y(), wInit, hInit))
        anim.setEndValue(
            QRect(wid.x(), wid.y(), w, h))

        return anim

    # animate according to X
    def animateX(self, wid, xInit, x):

        anim = QPropertyAnimation(wid, b'geometry')
        anim.setDuration(1200)
        anim.setStartValue(
            QRect(xInit, wid.y(), wid.width(), wid.height()))
        anim.setEndValue(
            QRect(x, wid.y(), wid.width(), wid.height()))

        return anim

    # after dialogs we show lists
    def AnimateLists(self):

        
        # show the widgets
        self.ui.itemToChoose.show()
        self.ui.itemsToBuy.show()
        self.ui.submitButton.show()

        anim3 = 20
        anim4 = 210
        anim5 = 1250

        self.ui.itemToChoose.move(
            -anim3 - self.ui.itemToChoose.width(), self.ui.itemToChoose.y())

        self.ui.submitButton.move(
            -anim4 - self.ui.submitButton.width(), self.ui.submitButton.y())

        self.ui.itemsToBuy.move(
            anim5 + self.ui.itemsToBuy.width(), self.ui.itemsToBuy.y())

        self.animate3 = self.animateX(
            self.ui.itemToChoose, self.ui.itemToChoose.x(), anim3)

        self.animate4 = self.animateX(
            self.ui.submitButton, self.ui.submitButton.x(), anim4)

        self.animate5 = self.animateX(
            self.ui.itemsToBuy, self.ui.itemsToBuy.x(), anim5)

        self.group2 = QParallelAnimationGroup()
        self.group2.addAnimation(self.animate3)
        self.group2.addAnimation(self.animate4)

        self.group3 = QSequentialAnimationGroup()
        self.group3.addAnimation(self.animate5)
        self.group3.addAnimation(self.group2)

        self.group3.start()

    # set all animations
    def setAnimations(self):

        dialogueY = -320

        self.animate1 = self.animate(self.ui.dialogue, self.ui.dialogue.width(), 0,
                                     self.ui.dialogue.width(), self.ui.dialogue.height())

        self.ui.dialogue.move(self.ui.dialogue.x(), dialogueY)

        x = self.ui.text.x()
        y = self.ui.text.y()
        w = self.ui.text.width()
        h = 131

        self.ui.text.setGeometry(QRect(x, y, w, 0))

        self.animate2 = self.animate(self.ui.text, self.ui.text.width(), 0,
                                     self.ui.text.width(), h)

        self.group = QSequentialAnimationGroup()
        self.group.addAnimation(self.animation)
        self.group.addAnimation(self.animate1)
        self.group.addAnimation(self.animate2)

        self.group.start()

        pygame.mixer.find_channel().play(pygame.mixer.Sound('Data/Assets/audio/customer.ogg'))

        self.group.finished.connect(self.AnimateLists)

    def startGame(self):

        # hide the main screen
        self.ui.mainGame.hide()

        # choose a random character to show
        self.chooseACharacter()

        # nbr of items to guess
        self.nbRuleConsequent = 0

        # populate items to choose and items to buy
        ruleIndex = randint(0, len(self.apriori.assocRules) - 1)
        self.populateItemsToBuy(ruleIndex)

        self.ui.text.setPlainText(
            "Hello ! could you help me  please ? ")
        # add the current transaction

        # set all animations
        self.setAnimations()

        

    def resetGame(self):


        self.ui.itemToChoose.hide()
        self.ui.correctItems.hide()
        self.ui.itemsToBuy.hide()
        self.ui.submitButton.hide()
        self.ui.next.hide()

        self.ui.submitButton.setEnabled(True)
        self.ui.itemToChoose.setEnabled(True)

        self.ui.itemToChoose.clear()
        self.ui.correctItems.clear()
        self.ui.itemsToBuy.clear()


app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())

