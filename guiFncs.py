import nflgame
import fbTool
import os
import fpPlayer
import fpKicker
import createLeague
import addRoster
import removeRoster
import addPlayer
import mainMenu
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from sys import platform as _platform

class addPlayer(QtGui.QMainWindow, addPlayer.Ui_MainWindow):
    def __init__(self, parent=None):
        super(addPlayer, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
    def initUI(self):      
        self.btn.clicked.connect(self.showDialog)
        self.setGeometry(300, 300, 750, 200)
        self.setWindowTitle('Add Player to Team')
        self.show()        
    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Add Player to League', 'Enter the name of your league:') 
        text1, ok = QtGui.QInputDialog.getText(self, 'Add Player to League', 'Enter the name of your team:')
        text2, ok = QtGui.QInputDialog.getText(self, 'Add Player to League', 
            'Enter name of player you wish to add:')
        text3, ok = QtGui.QInputDialog.getText(self, 'Add Player to League', 'Enter the team name of that player:')
        testVar=fbTool.addPlayer(text,text1,text2,text3)
        if not testVar:
            self.le.setText("Succesfully added " + text2 + " to " + text1 + " from league " + text)
        if testVar == 1:
            self.le.setText("Player already rostered in league " + text)
        if testVar == 2:
            self.le.setText("Player " + text2 + " not found in database")
        if testVar == 3:
            self.le.setText("Team does not exist.")
        if testVar == 4:
            self.le.setText("League does not exist.")
        else:
            self.le.setText("Failed to add player...")

class addRoster(QtGui.QMainWindow, addRoster.Ui_MainWindow):
    def __init__(self, parent=None):
        super(addRoster, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):      
        self.btn.clicked.connect(self.showDialog)
        self.setGeometry(300, 300, 750, 200)
        self.setWindowTitle('Add Team to League')
        self.show()
        
    def showDialog(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Add Team to League', 
            'Enter your league name:')
        text1, ok = QtGui.QInputDialog.getText(self, 'Add Team to League', 'Enter your team name:')
        testVar=fbTool.addRoster(text,text1)
        if not testVar:
            self.le.setText("Succesfully added roster " + text1 + "!")
        else:
            self.le.setText("Failed to add team...")
            if testVar == 1:
                self.le.setText("Team " + text1 + " already exists in league " + text)
            if testVar == 2:
                self.le.setText("League " + text + " does not exist. Choose 'Add league to be tracked' button on main menu to add it.")
            
            
        
class createLeague(QtGui.QMainWindow, createLeague.Ui_MainWindow):
    def __init__(self, parent=None):
        super(createLeague, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):      
        self.btn.clicked.connect(self.showDialog)
        self.setGeometry(300, 300, 700, 200)
        self.setWindowTitle('Create A League')
        self.show()
        
    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'League Name', 
            'Enter your league name:')
        testVar=fbTool.addLeague(text)
        if testVar == 0:
            self.le2.setText(text + " has been created!")
        else:
            if testVar == 1:
                self.le2.setText("League " + text + " already exists.")
            if testVar == 2:
                self.le2.setText("Something is broken.")
        mainMenu.updateTree()

class removeRoster(QtGui.QMainWindow, removeRoster.Ui_MainWindow):
    def __init__(self, parent=None):
        super(removeRoster, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.btn.clicked.connect(self.showDialog)
        self.setGeometry(300, 300, 700, 200)
        self.setWindowTitle('Remove A Roster')
        self.show()

    def showDialog(self):
        leagueName, ok = QtGui.QInputDialog.getText(self, 'Remove Roster', 'Enter the league you would like to remove a roster from:')
        rosterName, ok = QtGui.QInputDialog.getText(self, 'Remove Roster', 'Enter the roster you would like to remove:')
        returnValue = fbTool.removeRoster(leagueName, rosterName)
        if returnValue == 0:
            self.le2.setText(rosterName + " has been removed")
        elif returnValue == 1:
            self.le2.setText("League " + leagueName + " does not exist.")
        elif returnValue == 2:
            self.le2.setText("Roster " + rosterName + " does not extist.")
        else:
            self.le2.setText("Unknown Error")
        mainMenu.updateTree()

def updateRoster():
    window=QWidget()
    window.setFixedSize(650,500)
    list1 = QListWidget()
    list2 = QListWidget()   
    list3 = QListWidget()
    list1.setMaximumSize(200,425)
    list2.setMaximumSize(200,425)
    list3.setMaximumSize(200,425)
    grid = QGridLayout()
    grid.setSpacing(10)
    grid.heightForWidth(425)
    grid.addWidget(list1,1,0)
    grid.addWidget(list2,1,5)
    grid.addWidget(list3,1,10)

    if fbTool.leagueLists:
        for i in fbTool.leagueLists:
            list1.addItem(i.leagueName)

    def poplist2(item):
        list2.clear()
        for i in fbTool.leagueLists:
            if i.leagueName == item.text():
                for j in i.rosters:
                    list2.addItem(j.rosterName)

    list1.itemClicked.connect(poplist2)
 
    def poplist3(item):
        list3.clear()
        for i in fbTool.leagueLists:
            if i.leagueName == list1.currentItem().text():
                for j in i.rosters:
                    if j.rosterName == item.text():
                        for k in j.players:
                            list3.addItem((k.firstName + ' ' + k.lastName))

    list2.itemClicked.connect(poplist3)

    window.setLayout(grid)
    window.setWindowTitle('Update Rosters')
    button1 = QPushButton('Add player',window)
    button2 = QPushButton('Remove player',window)
    button1.setToolTip('Add player to highlighted roster')
    button2.setToolTip('Remove highlighted player from roster')
    def but1():
        if not list2.currentItem():
            QMessageBox.critical(window,'error','No roster selected')
        else:
            mainMenu.updateTree()
    def but2():
        if not list3.currentItem():
            QMessageBox.critical(window,'error','No player selected')
        else:
            mainMenu.updateTree()
    button1.clicked.connect(but1)
    button2.clicked.connect(but2)
    button1.resize(button2.sizeHint())
    button2.resize(button2.sizeHint())
    button1.move(150,470)
    button2.move(300,470)
    return window
