import nflgame
import fbTool
import os
import fpPlayer
import fpKicker
import createLeague
import addRoster
import addPlayer
import mainMenu

from sys import platform as _platform
from PyQt4 import QtGui
import sys

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

