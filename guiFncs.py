import nflgame
import fbTool
import os
import fpPlayer
import fpKicker
import addRoster
import mainMenu
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from sys import platform as _platform

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
            
#########AND THEN ROB JUMPS IN AND STARTS DOING THINGS COMPLETELY DIFFERENTLY
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
        list3.clear()
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
            ln = list1.currentItem().text()
            rn = list2.currentItem().text()
            pn,test = QInputDialog.getText(window,'Input dialog','Enter Player to Add\'s Name:')
            if test:
                tn,test = QInputDialog.getText(window,'Input dialog','Enter name of NFL team player plays on:')
                ret=fbTool.addPlayer(str(ln),str(rn),str(pn),str(tn))
                if ret == 1:
                    QMessageBox.critical(window,'error','Could not add player: Player already rostered')
                if ret == 2:
                    QMessageBox.critical(window,'error','Could not add player: Player does not exist')
                if not ret:
                    mainMenu.updateTree()
                    for i in fbTool.leagueLists:
                        if i.leagueName == str(ln):
                            for j in i.rosters:
                                if j.rosterName == str(rn):
                                    list3.clear()
                                    for k in j.players:
                                        list3.addItem((k.firstName+' '+k.lastName))
            mainMenu.updateTree()
    def but2():
        if not list3.currentItem():
            QMessageBox.critical(window,'error','No player selected')
        else:
            ln = list1.currentItem().text()
            rn = list2.currentItem().text()
            pn = str(list3.currentItem().text())
            te = QMessageBox.question(window,'???','Are you sure you want to delete this player?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            if te == QMessageBox.Yes:
                ret = fbTool.removePlayer(nflgame.find(pn,team=None),str(ln),str(rn))
                if ret:
                    QMessageBox.critical(window,'error','SOMETHING BROKE!')
                else:
                    list3.clear()
                    for i in fbTool.leagueLists:
                        if i.leagueName == str(ln):
                            for j in i.rosters:
                                if j.rosterName == str(rn):
                                    for k in j.players:
                                        list3.addItem((k.firstName+' '+k.lastName))
            mainMenu.updateTree()
    button1.clicked.connect(but1)
    button2.clicked.connect(but2)
    button1.resize(button2.sizeHint())
    button2.resize(button2.sizeHint())
    button1.move(150,470)
    button2.move(300,470)
    return window

def deleteLeague():
    window = QWidget()
    window.setFixedSize(225,500)
    grid = QGridLayout()
    grid.setSpacing(10)
    grid.heightForWidth(425)
    if not fbTool.leagueLists:
        return -1
    else:
        li = QListWidget()
        li.setMaximumSize(200,425)
        for i in fbTool.leagueLists:
            li.addItem(i.leagueName)
        grid.addWidget(li,0,0)
        button = QPushButton('Remove League',window)
        button.setToolTip('Deletes selected league from Database')
        def but1():
            if li.currentItem():
                ln = li.currentItem().text()
                te = QMessageBox.question(window,'???','Are you sure you want to delete this league? (it will remove the league and all of the teams on the league)',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
                if te == QMessageBox.Yes:
                    fbTool.removeLeague(str(ln))
                    li.clear()
                    for i in fbTool.leagueLists:
                        li.addItem(i.leagueName)
                    mainMenu.updateTree()
            else:
                QMessageBox.critical(window,'error','No league selected')
        button.clicked.connect(but1)
        button.resize(button.sizeHint())
        button.move(60,470)       
        window.setLayout(grid)
        return window
def deleteRoster():
    window = QWidget()
    window.setFixedSize(550,500)
    grid = QGridLayout()
    grid.setSpacing(10)
    grid.heightForWidth(425)
    if not fbTool.leagueLists:
        return -1
    else:
        list1 = QListWidget()
        list2 = QListWidget()
        list1.setMaximumSize(200,425)
        list2.setMaximumSize(200,425)
        for i in fbTool.leagueLists:
            list1.addItem(i.leagueName)
        grid.addWidget(list1,0,0)
        grid.addWidget(list2,0,5)
        def poplist2(item):
            list2.clear()
            for i in fbTool.leagueLists:
                if i.leagueName == item.text():
                    for j in i.rosters:
                        list2.addItem(j.rosterName)
        list1.itemClicked.connect(poplist2)
        button = QPushButton('Remove Roster',window)
        button.setToolTip('Deletes selected league from Database')
        def but1():
            if list2.currentItem():
                ln = list1.currentItem().text()
                rn = list2.currentItem().text()
                te = QMessageBox.question(window,'???','Are you sure you want to delete this roster?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
                if te == QMessageBox.Yes:
                    fbTool.removeRoster(str(ln),str(rn))
                    for i in fbTool.leagueLists:
                        if i.leagueName == str(ln):
                            list2.clear()
                            for j in i.rosters:
                                list2.addItem(j.rosterName)
                    mainMenu.updateTree()
            else:
                QMessageBox.critical(window,'error','No roster selected')
        button.clicked.connect(but1)
        button.resize(button.sizeHint())
        button.move(60,470)       
        window.setLayout(grid)
        return window

def trade():
    window = QWidget()
    window.setFixedSize(800,600)
    grid = QGridLayout()
    grid.setSpacing(10)
    if not fbTool.leagueLists:
        return -1
    else:
        button = QPushButton('Trade Selected Players',window)
        button.resize(button.sizeHint())
        button.move(20,570)
        leagues = QListWidget()
        rosters1 = QListWidget()
        rosters2 = QListWidget()
        roster1 = QListWidget()
        roster2 = QListWidget()

        roster1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        roster2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        pl1 = []
        pl2 = []
        grid.addWidget(leagues,0,0)
        grid.addWidget(rosters1,0,1)
        grid.addWidget(rosters2,1,1)
        grid.addWidget(roster1,0,2)
        grid.addWidget(roster2,1,2)
        for i in fbTool.leagueLists:
            leagues.addItem(i.leagueName)
        def popRosters():
            roster1.clear()
            roster2.clear()
            rosters1.clear()
            rosters2.clear()
            for i in fbTool.leagueLists:
                if i.leagueName == str(leagues.currentItem().text()):
                    for j in i.rosters:
                        rosters1.addItem(j.rosterName)
                        rosters2.addItem(j.rosterName)
        def popRoster1():
            roster1.clear()
            for i in fbTool.leagueLists:
                if i.leagueName == str(leagues.currentItem().text()):
                    for j in i.rosters:
                        if j.rosterName == str(rosters1.currentItem().text()):
                            for k in j.players:
                                roster1.addItem((k.firstName+' '+k.lastName))
        def popRoster2():
            roster2.clear()
            for i in fbTool.leagueLists:
                if i.leagueName == str(leagues.currentItem().text()):
                    for j in i.rosters:
                        if j.rosterName == str(rosters2.currentItem().text()):
                            for k in j.players:
                                roster2.addItem((k.firstName+' '+k.lastName))
        def makePlayerList1():
            for h in pl1:
                pl1.pop()
            itemsList = roster1.selectedItems()
            for i in itemsList:
                name = str(i.text())
                i2push = nflgame.find(name)
                if i2push:
                    pl1.append(i2push[0])
        def makePlayerList2():
            for h in pl2:
                pl2.pop()
            itemsList = roster2.selectedItems()
            for i in itemsList:
                name = str(i.text())
                i2push = nflgame.find(name)
                if i2push:
                    pl2.append(i2push[0])
        def but():
            if not leagues.currentItem():
                QMessageBox.critical(window,'error','League not selected from league list')
            elif not rosters1.currentItem():
                QMessageBox.critical(window,'error','Roster not selected from top rosters box')
            elif not rosters2.currentItem():
                QMessageBox.critical(window,'error','Roster not selected from bottom rosters box')
            elif not roster1.currentItem():
                QMessageBox.critical(window,'error','Player not selected from top roster')
            elif not roster2.currentItem():
                QMessageBox.critical(window,'error','Player not selected from the bottom roster')
            elif roster1.currentItem().text()==roster2.currentItem().text():
                QMessageBox.critical(window,'error','Roster cannot trade to self')
            else:
                ln = str(leagues.currentItem().text())
                r1 = str(rosters1.currentItem().text())
                r2 = str(rosters2.currentItem().text())
                ret = fbTool.tradePlayers(pl1,pl2,ln,r1,r2)
                if ret:
                    QMessageBox.critical(window,'error','Something is broken.')
                else:
                    popRoster1()
                    popRoster2()
                    mainMenu.updateTree()
        leagues.itemClicked.connect(popRosters)
        rosters1.itemClicked.connect(popRoster1)
        rosters2.itemClicked.connect(popRoster2)
        roster1.itemClicked.connect(makePlayerList1)
        roster2.itemClicked.connect(makePlayerList2)
        button.clicked.connect(but)
        window.setLayout(grid)
        return window

def pointsStuff():
    i=0
