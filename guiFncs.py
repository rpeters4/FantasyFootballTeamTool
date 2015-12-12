import nflgame
import fbTool
import os
import fpPlayer
import fpKicker
import mainMenu
import fbPlayerPoints
import sys
import byeWeekLists
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from sys import platform as _platform

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
            rn,test = QInputDialog.getText(window,'New roster','Please enter the name for the new roster you\'d like to add:').strip()
            rn = str(rn)
            while loopvar == QMessageBox.Yes:
                dn,test = QInputDialog.getText(window,'Defense','Please enter a team to use as defense:').strip()
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
            pn,test = QInputDialog.getText(window,'Input dialog','Enter Player to Add\'s Name:').strip()
            if test:
                tn,test = QInputDialog.getText(window,'Input dialog','Enter name of NFL team player plays on:').strip()
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
    button1.move(135,25)
    button2 = QPushButton('Compare two fantasy teams',window)
    button2.move(135,75)
    def comparetwoplayerswindow():
        window1 = QWidget()
        window1.setFixedSize(1000,400)
        window1.setWindowTitle('Player Comparison')
        #Player One stuff
        prompt1 = QLabel('Enter Player One:',window1)
        prompt1.move(10,25)
        input1 = QLineEdit(window1)
        input1.move(150,25)
        input1.setFixedWidth(200)
        input1.setToolTip('Example: Aaron Rodgers')
        prompt12 = QLabel('Choose year:', window1)
        prompt12.move(10,75)
        input12 = QComboBox(window1)
        input12.addItem("Choose year")
        input12.addItem("2009")
        input12.addItem("2010")
        input12.addItem("2011")
        input12.addItem("2012")
        input12.addItem("2013")
        input12.addItem("2014")
        input12.addItem("2015")
        input12.move(150,75)
        def handleActivated(oneyear):
            print('handleChanged: %s' % oneyear)
        input12.currentIndexChanged['QString'].connect(handleActivated)
        prompt13 = QLabel('Enter week(s):', window1)
        prompt13.move(10,125)
        input13 = QLineEdit(window1)
        input13.move(150,125)
        input13.setFixedWidth(200)
        input13.setToolTip('Example: 10 11 12 [no commas between weeks]')
        prompt14 = QLabel('Player One points:', window1)
        prompt14.move(10,175)
        player1area = QListWidget(window1)
        player1area.move(150, 175)
        #Player Two stuff
        prompt2 = QLabel('Enter Player Two:',window1)
        prompt2.move(500,25)
        input2 = QLineEdit(window1)
        input2.move(640,25)
        input2.setFixedWidth(200)
        input2.setToolTip('Example: Aaron Rodgers')
        prompt22 = QLabel('Choose year:', window1)
        prompt22.move(500,75)
        input22 = QComboBox(window1)
        input22.addItem("Choose year")
        input22.addItem("2009")
        input22.addItem("2010")
        input22.addItem("2011")
        input22.addItem("2012")
        input22.addItem("2013")
        input22.addItem("2014")
        input22.addItem("2015")
        input22.move(640,75)
        prompt23 = QLabel('Enter week(s):', window1)
        prompt23.move(500,125)
        input23 = QLineEdit(window1)
        input23.move(640,125)
        input23.setFixedWidth(200)
        input23.setToolTip('Example: 10 11 12 [no commas between weeks]')
        prompt24 = QLabel('Player Two points:', window1)
        prompt24.move(500,175)
        player2area = QListWidget(window1)
        player2area.move(640, 175)

        def confirm():
            player1area.clear()
            player2area.clear()
            #Player One stuff
            player1info = []
            points1 = 0
            player1 = str(input1.text()).strip()
            if not nflgame.find(player1, team=None):
                onenoexist = QListWidgetItem("Player does not exist")
                player1area.addItem(onenoexist)
            else:
                player1info.append(player1)
                def handleActivated():
                    print('handleChanged: %d' % int(input12.currentText()))
                    print player1info
                input12.activated['QString'].connect(handleActivated)
                player1year = int(input12.currentText())
                player1info.append(player1year)
                player1week = str(input13.text()).strip()
                p1w = map(int, player1week.split())
                for i in p1w:
                    if i<1 or i>17:
                        weeknoexist1 = QListWidgetItem("Week %i does not exist" % i)
                        player1area.addItem(weeknoexist1)
                        p1w.remove(i)
                    if i>(nflgame.live.current_year_and_week()[1]) and (i>0 and i<18):
                        onenotcurrent = QListWidgetItem("Week %i hasn't occurred yet" % i)
                        player1area.addItem(onenotcurrent)
                        p1w.remove(i)
                    if len(p1w) == 0:
                            oneonlyweek = QListWidgetItem("You have not entered any more weeks")
                            player1area.addItem(oneonlyweek)
                for w in byeWeekLists.byeWeeks:
                    for t in w:
                        if nflgame.find(player1info[0], team=None)[0].team == t and w[-1] in p1w:
                            onebye = QListWidgetItem("%s has a bye in week %d" % (t, w[-1]))
                            player1area.addItem(onebye)
                            p1w.remove(w[-1])
                            print str(p1w)
                            if len(p1w) == 0:
                                oneonlybye = QListWidgetItem("You have not entered any more weeks")
                                player1area.addItem(oneonlybye)
                if len(p1w) > 0:
                    player1info.append(p1w)
                    print player1info
                    points1 = fbPlayerPoints.playerPoints(player1info)
                    item1 = QListWidgetItem("%f" % float(points1))
                    if points1 == float('inf'):
                        onenoexist = QListWidgetItem("Player does not exist")
                        player1area.addItem(onenoexist)
                    else:
                        player1found = nflgame.find(player1info[0], team = None)
                        player1area.addItem(item1)
                        p1 = player1found[0]
                        m1 = p1.stats(player1info[1],player1info[2])
                        if 'passing_yds' in m1.stats:
                            p1passyds = m1.stats['passing_yds']
                            p1passydsin = QListWidgetItem("Passing yards: %d" % int(p1passyds))
                            player1area.addItem(p1passydsin)
                        if 'passing_twoptm' in m1.stats:
                            p1tpm = m1.stats['passing_twoptm']
                            p1tpmin = QListWidgetItem("Two-pt conversions made: %d" % int(p1tpm))
                            player1area.addItem(p1tpmin)
                        if 'passing_ints' in m1.stats:
                            p1passints = m1.stats['passing_ints']
                            p1passintsin = QListWidgetItem("Passing ints: %d" % int(p1passints))
                            player1area.addItem(p1passintsin)
                        if 'passing_tds' in m1.stats:
                            p1passtds = m1.stats['passing_tds']
                            p1passtdsin = QListWidgetItem("Passing TDs: %d" % int(p1passtds))
                            player1area.addItem(p1passtdsin)
                        if 'rushing_tds' in m1.stats:
                            p1rushtds = m1.stats['rushing_tds']
                            p1rushtdsin = QListWidgetItem("Rushing TDs: %d" % int(p1rushtds))
                            player1area.addItem(p1rushtdsin)
                        if 'rushing_yds' in m1.stats:
                            p1rushyds = m1.stats['rushing_yds']
                            p1rushydsin = QListWidgetItem("Rushing yards: %d" % int(p1rushyds))
                            player1area.addItem(p1rushydsin)
                        if 'receiving_yds' in m1.stats:
                            p1recyds = m1.stats['receiving_yds']
                            p1recydsin = QListWidgetItem("Receiving yards: %d" % int(p1recyds))
                            player1area.addItem(p1recydsin)
                        if 'receiving_tds' in m1.stats:
                            p1rectds = m1.stats['receiving_tds']
                            p1rectdsin = QListWidgetItem("Receiving TDs: %d" % int(p1rectds))
                            player1area.addItem(p1rectdsin)
                        if 'receiving_twoptm' in m1.stats:
                            p1rectpm = m1.stats['receiving_twoptm']
                            p1rectpmin = QListWidgetItem("Receiving two-pt conversions made: %d" % int(p1rectpm))
                            player1area.addItem(p1rectpmin)
                        if 'fumbles_lost' in m1.stats:
                            p1fum = m1.stats['fumbles_lost']
                            p1fumin = QListWidgetItem("Fumbles lost: %d" % int(p1fum))
                            player1area.addItem(p1fumin)
                        if 'rushing_twoptm' in m1.stats:
                            p1rushtpm = m1.stats['rushing_twoptm']
                            p1rushtpmin = QListWidgetItem("Rushing two-pt conversions made: %d" % int(p1rushtpm))
                            player1area.addItem(p1rushtpmin)
                    #Player Two stuff
            player2info = []
            points2 = 0
            player2 = str(input2.text()).strip()
            if not nflgame.find(player2, team=None):
                twonoexist = QListWidgetItem("Player does not exist")
                player2area.addItem(twonoexist)
            else:
                player2info.append(player2)
                def handleActivated():
                    print('handleChanged: %d' % int(input22.currentText()))
                    print player2info
                input22.activated['QString'].connect(handleActivated)
                player2year = int(input22.currentText())
                player2info.append(player2year)
                player2week = str(input23.text()).strip()
                p2w = map(int, player2week.split())
                for i in p2w:
                    if i<1 or i>17:
                        weeknoexist2 = QListWidgetItem("Week %i does not exist" % i)
                        player2area.addItem(weeknoexist2)
                        p2w.remove(i)
                    if i>(nflgame.live.current_year_and_week()[1]) and (i>0 and i<18):
                        twonotcurrent = QListWidgetItem("Week %i hasn't occurred yet" % i)
                        player2area.addItem(twonotcurrent)
                        p2w.remove(i)
                    if len(p2w) == 0:
                            twoonlyweek = QListWidgetItem("You have not entered any more weeks")
                            player2area.addItem(twoonlyweek)
                for w in byeWeekLists.byeWeeks:
                    for t in w:
                        if nflgame.find(player2info[0], team=None)[0].team == t and w[-1] in p2w:
                            twobye = QListWidgetItem("%s has a bye in week %d" % (t, w[-1]))
                            player2area.addItem(twobye)
                            p2w.remove(w[-1])
                            print str(p2w)
                            if len(p2w) == 0:
                                twoonlybye = QListWidgetItem("You have not entered any more weeks")
                                player2area.addItem(twoonlybye)
                if len(p2w) > 0:
                    player2info.append(p2w)
                    points2 = fbPlayerPoints.playerPoints(player2info)
                    item2 = QListWidgetItem("%f" % float(points2))
                    if points2 == float('inf'):
                        twonoexist = QListWidgetItem("Player does not exist")
                        player2area.addItem(twonoexist)
                    else:
                        player2found = nflgame.find(player2info[0], team = None)
                        player2area.addItem(item2)
                        p2 = player2found[0]
                        m2 = p2.stats(player2info[1],player2info[2])
                        if 'passing_yds' in m2.stats:
                            p2passyds = m2.stats['passing_yds']
                            p2passydsin = QListWidgetItem("Passing yards: %d" % int(p2passyds))
                            player2area.addItem(p2passydsin)
                        if 'passing_twoptm' in m2.stats:
                            p2tpm = m2.stats['passing_twoptm']
                            p2tpmin = QListWidgetItem("Two-pt conversions made: %d" % int(p2tpm))
                            player2area.addItem(p2tpmin)
                        if 'passing_ints' in m2.stats:
                            p2passints = m2.stats['passing_ints']
                            p2passintsin = QListWidgetItem("Passing ints: %d" % int(p2passints))
                            player2area.addItem(p2passintsin)
                        if 'passing_tds' in m2.stats:
                            p2passtds = m2.stats['passing_tds']
                            p2passtdsin = QListWidgetItem("Passing TDs: %d" % int(p2passtds))
                            player2area.addItem(p2passtdsin)
                        if 'rushing_tds' in m2.stats:
                            p2rushtds = m2.stats['rushing_tds']
                            p2rushtdsin = QListWidgetItem("Rushing TDs: %d" % int(p2rushtds))
                            player2area.addItem(p2rushtdsin)
                        if 'rushing_yds' in m2.stats:
                            p2rushyds = m2.stats['rushing_yds']
                            p2rushydsin = QListWidgetItem("Rushing yards: %d" % int(p2rushyds))
                            player2area.addItem(p2rushydsin)
                        if 'receiving_yds' in m2.stats:
                            p2recyds = m2.stats['receiving_yds']
                            p2recydsin = QListWidgetItem("Receiving yards: %d" % int(p2recyds))
                            player2area.addItem(p2recydsin)
                        if 'receiving_tds' in m2.stats:
                            p2rectds = m2.stats['receiving_tds']
                            p2rectdsin = QListWidgetItem("Receiving TDs: %d" % int(p2rectds))
                            player2area.addItem(p2rectdsin)
                        if 'receiving_twoptm' in m2.stats:
                            p2rectpm = m2.stats['receiving_twoptm']
                            p2rectpmin = QListWidgetItem("Receiving two-pt conversions made: %d" % int(p2rectpm))
                            player2area.addItem(p2rectpmin)
                        if 'fumbles_lost' in m2.stats:
                            p2fum = m2.stats['fumbles_lost']
                            p2fumin = QListWidgetItem("Fumbles lost: %d" % int(p2fum))
                            player2area.addItem(p2fumin)
                        if 'rushing_twoptm' in m2.stats:
                            p2rushtpm = m2.stats['rushing_twoptm']
                            p2rushtpmin = QListWidgetItem("Rushing two-pt conversions made: %d" % int(p2rushtpm))
                            player2area.addItem(p2rushtpmin)
                           
        cbut = QPushButton('Compare',window1)
        cbut.move(500, 375)
        cbut.clicked.connect(confirm)
        window1.show()
        mainMenu.openWins.append(window1)
        return window1


    button1.clicked.connect(comparetwoplayerswindow)
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
