import nflgame
import fbTool
import os
import fpPlayer
import fpKicker
import mainMenu
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from sys import platform as _platform

#########AND THEN ROB JUMPS IN AND STARTS DOING THINGS COMPLETELY DIFFERENTLY
def addRoster():
    if not fbTool.leagueLists:
        return -1
    window=QWidget()
    window.setFixedSize(300,600)
    window.setWindowTitle('Add Roster')
    list1 = QListWidget()
    list1.setMaximumSize(250,500)
    for i in fbTool.leagueLists:
        list1.addItem(i.leagueName)
    button = QPushButton('Add roster to selected leauge',window)
    button.setToolTip('Adds a new roster to the league selected from the league list')
    button.resize(button.sizeHint())
    button.move(40,570)
    def but():
        if not list1.currentItem():
            QMessageBox.critical(window,'error','Not league selected')
        else:
            defense = []
            ln=str(list1.currentItem().text())
            loopvar = QMessageBox.Yes
            rn,test = QInputDialog.getText(window,'New roster','Please enter the name for the new roster you\'d like to add:')
            rn = str(rn)
            while loopvar == QMessageBox.Yes:
                dn,test = QInputDialog.getText(window,'Defense','Please enter a team to use as defense:')
                if test:
                    d = nflgame.standard_team(str(dn))
                    if d is None:
                        QMessageBox.critical(window,'error','Invalid team name')
                    else:
                        defense.append(d)
                    if defense:
                        loopvar = QMessageBox.question(window,'???','Would you like to add another defense team?',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                elif not defense:
                    QMessageBox.critical(window,'error','Cannot have no defense')
                else:
                    loopvar = QMessageBox.No
            status = fbTool.addRoster(ln,rn,defense)
            if status >=3:
                errstr = 'defense team ' + defense[status-3] + ' is already used'
                QMessageBox.critical(window,'error',errstr)
            elif status ==1:
                QMessageBox.critical(window,'error','Team already exists.')
            elif status:
                QMessageBox.critical(window,'error','Something is horribly wrong')
        mainMenu.updateTree()     
    button.clicked.connect(but)
    grid = QGridLayout()
    grid.setSpacing(10)
    grid.addWidget(list1,0,0)
    window.setLayout(grid)
    return window

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
                            if k.active:
                                list3.addItem((k.firstName + ' ' + k.lastName))
                            else:
                                list3.addItem((k.firstName + ' ' + k.lastName+'(B)'))

    list2.itemClicked.connect(poplist3)

    window.setLayout(grid)
    window.setWindowTitle('Update Rosters')
    button1 = QPushButton('Add player',window)
    button2 = QPushButton('Remove selected player',window)
    button3 = QPushButton('Bench/Unbench player',window)
    button1.setToolTip('Add player to highlighted roster')
    button2.setToolTip('Remove highlighted player from roster')
    button3.setToolTip('Benches/unbenches a player')
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
                    poplist3(list2.currentItem())
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
                if pn[-1]==')':
                    pn=pn[:-3]
                ret = fbTool.removePlayer(nflgame.find(pn,team=None),str(ln),str(rn))
                if ret:
                    QMessageBox.critical(window,'error','SOMETHING BROKE!')
                else:
                    poplist3(list2.currentItem())
            mainMenu.updateTree()
    def but3():
        if not list3.currentItem():
            QMessageBox.critical(window,'error','No player selected')
        else:
            ln=str(list1.currentItem().text())
            rn=str(list2.currentItem().text())
            pn=str(list3.currentItem().text())
            if pn[-1]==')':
                pn=pn[:-3]
            for i in fbTool.leagueLists:
                if i.leagueName == ln:
                    for j in i.rosters:
                        if j.rosterName == rn:
                            for k in j.players:
                                if pn==(k.firstName + ' ' + k.lastName):
                                    fbTool.setPlayerActiveFlag(k)
        poplist3(list2.currentItem())
        mainMenu.updateTree()
    button1.clicked.connect(but1)
    button2.clicked.connect(but2)
    button3.clicked.connect(but3)
    button1.resize(button2.sizeHint())
    button2.resize(button2.sizeHint())
    button3.resize(button2.sizeHint())
    button1.move(40,470)
    button2.move(240,470)
    button3.move(440,470)
    return window

def deleteLeague():
    window = QWidget()
    window.setFixedSize(225,500)
    window.setWindowTitle('Delete league')
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
    window.setWindowTitle('Delete roster')
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

def compare():
    window = QWidget()
    window.setFixedSize(400,150)
    window.setWindowTitle('Compare menu')
    button1 = QPushButton('Compare two players',window)
    button1.move(150,25)
    button2 = QPushButton('Compare two fantasy teams',window)
    button2.move(150,75)
    
    def plcompare():
        def twocompare():
            print str(input1.text()) + ', ' + str(input2.text())
        window1 = QWidget()
        window1.setFixedSize(400,150)
        window1.setWindowTitle('Player Comparison')
        prompt1 = QLabel('Enter first player to compare',window1)
        prompt1.move(10,25)
        input1 = QLineEdit(window1)
        input1.move(150,25)
        input1.setFixedWidth(200)
        player1 = input1.text()
        prompt2 = QLabel('Enter second player to compare',window1)
        prompt2.move(10,75)
        input2 = QLineEdit(window1)
        input2.move(175,75)
        input2.setFixedWidth(200)
        player2 = input2.text()
        cbut = QPushButton('Compare!',window1)
        cbut.clicked.connect(twocompare)
        window1.show()
        mainMenu.openWins.append(window1)
        return window1
        
    
    button1.clicked.connect(plcompare)
    return window

def trade():
    window = QWidget()
    window.setFixedSize(800,600)
    window.setWindowTitle('Trade players')
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
