import nflgame
import fbTool
import os
import fpPlayer
import fpKicker
import design
import createLeague
import basicUI
import listLeague
import addRoster
import addPlayer
import writeFile
import loadFile
import basicUI
from sys import platform as _platform
from PyQt4 import QtGui
import sys

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.addLeague.clicked.connect(self.leagueButton)
        self.leagueList.clicked.connect(self.lgButton)
        self.addTeam.clicked.connect(self.teamButton)
        self.writeFile.clicked.connect(self.writeButton)
        self.readFile.clicked.connect(self.readButton)
        self.addPlayer.clicked.connect(self.playerButton)
        self.exit.clicked.connect(self.exitprog)
        self.window2 = None
        self.window3 = None
        self.window4 = None
        self.window5 = None
        self.window6 = None
        self.window7 = None
    def leagueButton(self):
        if self.window2 is None:
            self.window2 = createLeague(self)
        self.window2.show()
    def lgButton(self):
        if self.window3 is None:
            self.window3 = listLeague(self)
        self.window3.show()
    def teamButton(self):
        if self.window4 is None:
            self.window4 = addRoster(self)
    def writeButton(self):
        if self.window5 is None:
            self.window5 = writeFile(self)
    def readButton(self):
        if self.window6 is None:
            self.window6 = loadFile(self)
    def playerButton(self):
        if self.window7 is None:
            self.window7 = addPlayer(self)
    def exitprog(self):
        sys.exit()

class addPlayer(QtGui.QMainWindow, addPlayer.Ui_MainWindow):
    def __init__(self, parent=None):
        super(addPlayer, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):      

        #self.btn = QtGui.QPushButton('Create', self)
        #self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        #self.le = QtGui.QLineEdit(self)
        #self.le.move(130, 22)
        
        self.setGeometry(300, 300, 750, 200)
        self.setWindowTitle('Add Player to Team')
        self.show()
        
    def showDialog(self):

        text, ok = QtGui.QInputDialog.getText(self, 'Add Player to League', 'Enter the name of your league:') 
        text1, ok = QtGui.QInputDialog.getText(self, 'Add Player to League', 'Enter the name of your team:')
        text2, ok = QtGui.QInputDialog.getText(self, 'Add Player to League', 
            'Enter name of player you wish to add:')
        text3, ok = QtGui.QInputDialog.getText(self, 'Add Player to League', 'Enter the team name of that player:')
        #self.le.setText(text+text1+text2+text3)
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

class writeFile(QtGui.QMainWindow, writeFile.Ui_MainWindow):
    def __init__(self, parent=None):
        super(writeFile, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):      

        #self.btn = QtGui.QPushButton('Create', self)
        #self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        #self.le = QtGui.QLineEdit(self)
        #self.le.move(130, 22)
        
        self.setGeometry(300, 300, 750, 200)
        self.setWindowTitle('Write file to disk')
        self.show()
        
    def showDialog(self):
        
        fn, ok = QtGui.QInputDialog.getText(self, 'Write file to disk', 
            'Enter filename:')
        if not fbTool.writeClassToFile(fn):
            self.le.setText("Successfully output to file " + fn)
        else:
            self.le.setText("File input failed.")

class loadFile(QtGui.QMainWindow, loadFile.Ui_MainWindow):
    def __init__(self, parent=None):
        super(loadFile, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):      

        #self.btn = QtGui.QPushButton('Create', self)
        #self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        #self.le = QtGui.QLineEdit(self)
        #self.le.move(130, 22)
        
        self.setGeometry(300, 300, 750, 200)
        self.setWindowTitle('Load file from disk')
        self.show()
        
    def showDialog(self):
        
        fn, ok = QtGui.QInputDialog.getText(self, 'Load file from disk', 
            'Enter filename to load:')
        if not fbTool.readClassFromFile(fn):
            self.le.setText("Successfully loaded file " + fn)
        else:
            self.le.setText("File load failed.")


class addRoster(QtGui.QMainWindow, addRoster.Ui_MainWindow):
    def __init__(self, parent=None):
        super(addRoster, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):      

        #self.btn = QtGui.QPushButton('Create', self)
        #self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        #self.le = QtGui.QLineEdit(self)
        #self.le.move(130, 22)
        
        self.setGeometry(300, 300, 750, 200)
        self.setWindowTitle('Add Team to League')
        self.show()
        
    def showDialog(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Add Team to League', 
            'Enter your league name:')
        text1, ok = QtGui.QInputDialog.getText(self, 'Add Team to League', 'Enter your team name:')
        testVar=basicUI.fbTool.addRoster(text,text1)
        if not testVar:
            self.le.setText("Succesfully added roster " + text1 + "!")
            #self.showDialog()
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

        #self.btn = QtGui.QPushButton('Create', self)
        #self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        #self.le = QtGui.QLineEdit(self)
        #self.le.move(130, 22)
        
        self.setGeometry(300, 300, 700, 200)
        self.setWindowTitle('Create A League')
        self.show()
        
    def showDialog(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'League Name', 
            'Enter your league name:')
        testVar=basicUI.fbTool.addLeague(text)
        if testVar == 0:
            self.le2.setText(text + " has been created!")
            #self.showDialog()
        else:
            #self.le2.setText("Failed to add league...")
            if testVar == 1:
                self.le2.setText("League " + text + " already exists.")
            if testVar == 2:
                self.le2.setText("Something is broken.")

class listLeague(QtGui.QMainWindow, listLeague.Ui_MainWindow):
    def __init__(self, parent=None):
        super(listLeague, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.bttn.clicked.connect(self.showDialog)
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('List of Existing Leagues')
        self.show()

    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'List of Leagues')

def main():
    choice = 0
    if _platform =="linux" or _platform=="linux2":
        os.system('clear')
    elif _platform == "win32":
        os.system('cls')
    else:
        print 'This program doesn\'t run on mac...'
        exit()
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()
    sys.exit(app.exec_())

main()
