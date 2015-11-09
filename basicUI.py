import nflgame
import fbTool
import os
import fpPlayer
import fpKicker
<<<<<<< HEAD
import fpDefense
import fbPlayerPoints
=======
import design
import createLeague
import basicUI
import listLeague
import addRoster
import addPlayer
import writeFile
import loadFile
>>>>>>> refs/remotes/origin/Glenbranch
from sys import platform as _platform
from PyQt4 import QtGui
import sys


def getLeagueName(b):
    if not b:
        printLeagues()
    inp='\n'
    while inp=='\n':
        inp=raw_input('Please enter league name: ').strip()
        if inp == '\n':
            print 'Invalid league name, try again!'
    return inp

def getTeamName(ln):
    if ln is not None:
        printTeams(ln)
    inp = '\n'
    while inp=='\n':
        inp = raw_input('Please enter team name: ').strip()
        if inp == '\n':
            print 'Invalid team name, try again!'
    return inp

def getFileName(isOut):
    inp = '\n'
    while inp=='\n':
        if isOut:
            inp = raw_input('please input output filename: ').strip()
        else:
            inp = raw_input('please input input filename: ').strip()
    return inp
    
def addLeagueUI():
    k=1
    if fbTool.leagueLists:
       k=0 
    ln=getLeagueName(k)
    testVar=fbTool.addLeague(ln)
    if not testVar:
        print 'Successfully added league %s!' % ln
    else:
        print 'Failed to add league...'
        if testVar == 1:
            print 'League %s already exists.'%ln
        else:
            print 'something is horribly broken.'

def addRosterUI(ln,tn,defense):
    inp='y'
    if not defense:
        while inp.lower() not in ['n' or 'no']:
            if inp.lower()=='y' or inp.lower()=='yes':
                defen=raw_input('Please enter team name for defense: ').strip()
                while nflgame.standard_team(defen) is None:
                    defen=raw_input('Invalid team name, please try again: ').strip()
                defen=nflgame.standard_team(defen)
                defense.append(defen)
            else:
                print 'invalid input, try again.'
            inp = raw_input('Would you like to add another team for defense? (y/n): ' ).strip()

    testVar=fbTool.addRoster(ln,tn,defense)
    if not testVar:
        print 'Succesfully added roster %s!' % tn
    else:
        print 'Failed to add team...'
        if testVar == 1:
            print 'Team %s already exists in league %s' %(tn,ln)
            anotherVar = ' '
            while anotherVar not in ['y','yes','n','no']:
                anotherVar =raw_input('Try again?(y/n)').strip()
                if anotherVar.lower() in ['y','yes']:
                    tn=getTeamName(ln)
                    return addRosterUI(ln,tn,defense)
                if anotherVar.lower() in ['n','no']:
                    print 'Team not added...'
                    return -1
                if anotherVar.lower() not in ['y','yes','n','no']:
                    print 'Invalid input.  Please try again.'

        if testVar == 2:
            print 'League %s does not exist.'
            userInVar = ' '
            while userInVar not in ['y','yes','n''no']:
                userInVar = raw_input('Would you like to add it? (y/n): ').strip()
                if userInVar.lower() not in ['y','yes','n','no']:
                    print 'invalid input.  please try again.'
                if userInVar.lower() in ['y','yes']:
                    if not fbTool.addLeague(ln):
                        return addRosterUI(ln,tn,defense)
                if userInVar.lower() in ['n','no']:
                    print 'team not added.'
                    return 1
        if testVar >= 3:
            print '%s already used as defense team in league %s'%(defense[testVar-3],ln)
            oneFinalVar = ' '
            while oneFinalVar not in ['y','yes','n','no']:
                oneFinalVar = raw_input('Try again?(y/n) ').strip()
                if oneFinalVar.lower() in ['y','yes']:
                    addRosterUI(ln,tn,[])
                if oneFinalVar.lower() in ['n','no']:
                    print 'Team not added...'
                    return -1
                if oneFinalVar.lower() not in ['y','yes','n','no']:
                    print 'Invalid input, please try again.'
    return 0
                    
def addPlayerUI():
    ln=getLeagueName(0)
    tn=getTeamName(ln)
    printPlayers(ln,tn)
    plName=raw_input('Please input the desired player to add\'s name: ')
    plTeam=raw_input('Please input the desired player\'s NFL team: ')
    testVar=fbTool.addPlayer(ln,tn,plName,plTeam)
    if not testVar:
        print 'Succesfully added %s to %s from league %s' % (plName,tn,ln)
    else:
        print 'Failed to add player...'
    if testVar == 1:
        print 'Player already rostered in league %s'%ln
    if testVar == 2:
        print 'Player %s not found in database'%plName
    if testVar == 3:
        print 'Team does not exist.'
        userInVar = ' '
        while userInVar.lower() not in ['y','yes','n','no']:
            userInVar = raw_input('Would you like to add it? (y/n): ').strip()
            if userInVar.lower() not in ['y','yes','n','no']:
                print 'Invalid input.  Please try again.'
        if userInVar.lower()=='y' or userInVar.lower()=='yes':
            if not addRosterUI(ln,tn,[]):
                testVar = fbTool.addPlayer(ln,tn,plName,plTeam)
                if not testVar:
                    print 'Successfully added %s to %s from league %s' %(plName,tn,ln)
                else:
                    print 'Failed to add player.'
                if testVar == 1:
                  print 'Player already rostered in league %s'%ln
                if testVar == 2:
                    print 'Player %s not found in database'%plName
            else:
                print 'Failed to add roster.'
                raw_input ('Press return to continue...').strip()
                return -1
    if testVar == 4:
        print 'League does not exist.'
        userInVar=' '
        while userInVar.lower() not in ['y','yes','n','no']:
            userInVar = raw_input('Would you like to add the league and team? (y/n): ').strip()
            if userInVar.lower() not in ['y','yes','no','n']:
                print 'Invalid input.  Please try again.'
        if userInVar.lower()=='y' or userInVar.lower()=='yes':
            if not fbTool.addLeague(ln):
                if not addRosterUI(ln,tn,[]):
                    testVar =fbTool.addPlayer(ln,tn,plName,plTeam)
                    if not testVar:
                        print 'Successfully added %s to %s from league %s' %(plName,tn,ln)
                    else:
                        print 'Failed to add player.'
                    if testVar == 1:
                        print 'Player already rostered in league %s'%ln
                    if testVar == 2:
                        print 'Player %s not found in database'%plName
                else:
                    print 'failed to add team to league'
            else:
                print 'something went horribly wrong.'

def remLeagueUI():
    if printLeagues():
        return 1
    ln = raw_input('Please enter the name of the league you wish to remove: ').strip()
    invar=' '
    while invar.lower() not in ['y','yes','n','no']:
        invar=raw_input('Are you sure you want to do this?  \nYou will lose not only the league, but all of it\'s teams and their rosters! (y/n): ').strip()
        if invar.lower() in ['y','yes']:
            invar = raw_input('Would you like to save before doing so?(y/n): ')
            if invar.lower() in ['y','yes']:
                saveFileUI()
            if invar.lower() in ['n','no']:
                print 'IF YOU SAY SO.....'
                invar = 'y'
            if invar.lower() not in ['y','yes','n','no']:
                print 'Invalid input. Please try again...'
            else:
                if fbTool.removeLeague(ln):
                    print 'LEAGUE DOESN\'T EXIST!'
                else:
                    print 'League %s was deleted.' %ln
        if invar.lower() in ['n','no']:
            print 'I DIDN\'T THINK SO!'
        if invar.lower() not in ['y','yes','n','no']:
            print 'Invalid input.  Please try again...'

def remRosterUI():
    if printLeagues():
        return 1
    ln = raw_input('Please enter the name of the league the team is in: ').strip()
    if printTeams(ln):
        return 1
    rn = raw_input('Please enter the name of the team to remove: ').strip()
    invar=' '
    while invar.lower() not in ['y','yes','n','no']:
        invar=raw_input('Are you sure you want to do this?  \nYou will lose all of teami\'s roster information! (y/n): ').strip()
        if invar.lower() in ['y','yes']:
            invar = raw_input('Would you like to save before doing so?(y/n): ')
            if invar.lower() in ['y','yes']:
                saveFileUI()
            if invar.lower() in ['n','no']:
                print 'IF YOU SAY SO.....'
                invar = 'y'
            if invar.lower() not in ['y','yes','n','no']:
                print 'Invalid input. Please try again...'
            else:
                testVar = fbTool.removeRoster(ln,rn)
                if testVar == 1:
                    print 'LEAGUE DOESN\'T EXIST!'
                elif testVar == 2:
                    print 'ROSTER DOESN\'T EXIST!'
                elif not testVar:
                    print 'Team %s was deleted.' %rn
        if invar.lower() in ['n','no']:
            print 'I DIDN\'T THINK SO!'
        if invar.lower() not in ['y','yes','n','no']:
            print 'Invalid input.  Please try again...'

def iSWEARImNotGoingInsane():
    print '                 (__) '
    print '                 (oo) '
    print '           /------\/ '
    print '          / |    ||   '
    print '         *  /\---/\ '
    print '            ~~   ~~   '
    v = raw_input('...\"Have you mooed today?\"...\n').strip()
    if v.lower() in ['y','ye','es','yes']:
        print 'HOORAY! :D'
    if v.lower() in ['n','no']:
        print 'BOOOO!  D:<'
    if v.lower() == 'moo':
        print 'THAT\'S THE SPIRIT!!!!'
    raw_input('Welp!  That was a complete waste of time, wasn\'t it?\nPress return to go back to doing something actually productive...')

def remPlayerUI():
    if printLeagues():
        return 1
    ln = raw_input('Please enter the name of the league the team to remove from is in: ').strip()
    if printTeams(ln):
        return 1
    rn = raw_input('Please enter the name of the team to remove from: ').strip()
    if printPlayers(ln,rn):
        return 1
    pn = raw_input('Please enter the name of the player to remove: ').strip()
    invar=' '
    while invar.lower() not in ['y','yes','n','no']:
        invar=raw_input('Are you sure you want to do this? (y/n): ').strip()
        if invar.lower() in ['y','yes']:
            invar = raw_input('Would you like to save before doing so?(y/n): ')
            if invar.lower() in ['y','yes']:
                saveFileUI()
            if invar.lower() in ['n','no']:
                print 'IF YOU SAY SO.....'
                invar = 'y'
            if invar.lower() not in ['y','yes','n','no']:
                print 'Invalid input. Please try again...'
            else:
                testVar = fbTool.removePlayer(nflgame.find(pn,team=None),ln,rn)
                if testVar == 1:
                    print 'LEAGUE DOESN\'T EXIST!'
                elif testVar == 2:
                    print 'ROSTER DOESN\'T EXIST!'
                elif testVar == 3:
                    print 'PLAYER NOT ROSTERED ON TEAM!'
                elif not testVar:
                    print '%s was removed from %s.' %(pn,rn)
        if invar.lower() in ['n','no']:
            print 'I DIDN\'T THINK SO!'
        if invar.lower() not in ['y','yes','n','no']:
            print 'Invalid input.  Please try again...'

def tradePlayersUI():
    if printLeagues():
        return 1
    le = raw_input('Enter the name of the league the teams are in: ').strip()
    if printTeams(le):
        return 1
    t1 = raw_input('Enter the name of the team to trade from: ').strip()
    t2 = raw_input('Enter the name of the team to trade to: ').strip()
    if printPlayers(le,t1):
        print 'Cannot trade from empty roster %s.' % t1
        return 1
    pls1=[]
    pls2=[]
    plo1=[]
    plo2=[]
    if not printPlayers(le,t2):
        promptInp = ' '
        while promptInp.lower() not in ['n','no']:
            pls1.append(raw_input('Enter player from %s to trade: '%t1).strip())
            promptInp = raw_input('Would you like to trade another player? (y/n): ' ).strip()
            while promptInp.lower() not in ['y','yes','n','no']:
                promptInp = raw_input('Invalid input.  Please try again: ').strip()
        promptInp = ' '
        while promptInp.lower() not in ['n','no']:
            pls2.append(raw_input('Enter player from %s to trade: '%t2).strip())
            promptInp = raw_input('Would you like to trade another player? (y/n): ' ).strip()
            while promptInp.lower() not in ['y','yes','n','no']:
                promptInp = raw_input('Invalid input.  Please try again: ').strip()
        pls1=list(set(pls1))            #cast as set, then as list to rid of 
        pls2=list(set(pls2))            #potential dups
    else:
        promptInp = ' '
        while promptInp.lower() not in ['n','no']:
            pls1.append(raw_input('Enter player from %s to trade: '%t1).strip())
            promptInp = raw_input('Would you like to trade another player? (y/n): ' ).strip()
            while promptInp.lower() not in ['y','yes','n','no']:
                promptInp = raw_input('Invalid input.  Please try again: ').strip()
    
    for i in pls1:
        j=nflgame.find(i,team=None)
        if j:
            plo1.append(j[0])
    for i in pls2:
        j=nflgame.find(i,team=None)
        if j:
            plo2.append(j[0])

    testVar = fbTool.tradePlayers(plo1,plo2,le,t1,t2)
    if not testVar:
        print 'successfully traded'
        print pls1
        print 'from %s to %s for'%(t1,t2)
        print pls2
    if testVar == 1:
        print 'League does not exist.'
    if testVar == 2:
        print 'Roster does not exist.'
    if testVar == 3:
        print 'Player not on roster.'

def playerPointsUI():
    playerInfo = []
    points = 0
    playerInfo.append(raw_input("Enter player: ").strip())
    playerInfo.append(int(raw_input("Enter year: ")))
    w1 = raw_input("Enter week(s): ").strip()
    playerInfo.append(map(int, w1.split()))
    points = fbPlayerPoints.playerPoints(playerInfo)
    if points == float('inf'):
        print 'Player does not exist'
    print 'Points computed: %f'% points
    return points

def printLeagues():
    if fbTool.leagueLists:
        it=1
        print 'League# LeagueName'
        for i in fbTool.leagueLists:
            print '%d       %s' %(it,i.leagueName)
            it=it+1
    else:
        print 'No leagues currently registered...'
        return 1
    return 0

def printTeams(leagueName):
    if leagueName is None:
        leagueName=getLeagueName(0)
    it=1
    for i in fbTool.leagueLists:
        if i.leagueName==leagueName:
            if i.rosters:
                print 'Teams in league %s:'%leagueName
                print '{:4s} {:11s} '.format('Team#','Team Name')
                for j in i.rosters:
                    print '{:2d}    {:15s}'.format(it,j.rosterName)
                    it=it+1
            else:
                print 'No teams registered in %s'%leagueName
        elif i==fbTool.leagueLists[-1]:
            print 'error: league not registered'
            return 1
    return 0

def printPlayers(leagueName,teamName):
    if leagueName is None:
        leagueName=getLeagueName(0)
    if teamName is None:
        teamName=getTeamName(leagueName)
    lfound=False
    tfound=True
    for i in fbTool.leagueLists:
        if i.leagueName == leagueName:
            lfound=True
            for j in i.rosters:
                if j.rosterName == teamName:
                    tfound=True
                    print 'Players on team %s:'%teamName
                    if j.players:
                        print 'PlayerID       First Name       Last Name           NFLTeam    Position'
                    else:
                        print 'Team is empty'
                        return 1
                    for k in j.players:
                        print '{:14s} {:16s} {:19s} {:10s} {:9s} '.format(str(k.player_id),k.firstName,k.lastName,k.team,k.position)
                    print '%s uses %s\'s defense' %(teamName,j.defense)

    if not lfound:
        print 'League %s not found...' %leagueName
        return 1
    elif not tfound:
        print 'Team %s not found...' %teamName
        return 1
    return 0

def printPts():
    leagueName=getLeagueName(0)
    teamName=getTeamName(leagueName)
    weekNum=int(raw_input('Please enter a week number: '))
    points=[]
    it=0
    plfound=False
    tfound=False
    year=int(raw_input('Enter a year (2009-2015):').rstrip())
    for i in fbTool.leagueLists:
        if i.leagueName == leagueName:
            lfound=True
            for j in i.rosters:
                if j.rosterName == teamName:
                    tfound=True
                    if j.players:
                        print 'Calculating points for %s on week %d...'%(teamName,weekNum)
                        for k in j.players:
                            if k.position != 'LE' and k.position != 'RE' and k.position != 'OLB' and k.position != 'CB' and k.position != 'MLB' and k.position != 'DT' and k.position != 'DB' and k.position != 'DE' and k.position != 'FS' and k.position != 'SS':
                                playersName=k.firstName+' '+k.lastName
                                plyToApp = nflgame.find(playersName,k.team)[0]
                                if k.position == 'K':
                                    points.append(fpKicker.kickerScore(plyToApp,year,weekNum))
                                else:
                                    points.append(fpPlayer.fantasyPoints(plyToApp,year,weekNum))
                        print 'PlayerID       First Name       Last Name           NFLTeam    Points'
                        for k in j.players:
                            if k.position != 'LE' and k.position != 'RE' and k.position != 'OLB' and k.position != 'CB' and k.position != 'MLB' and k.position != 'DT' and k.position != 'DB' and k.position != 'DE' and k.position != 'FS' and k.position != 'SS':
                                print '{:14s} {:16s} {:19s} {:10s} {:9f} '.format(str(k.player_id),k.firstName,k.lastName,k.team,points[it])
                                it = it+1
                        dpoints=0
                        for l in j.defense:
                            dpoints = dpoints+fpDefense.fpDefense(l,year,weekNum)
                        p=sum(points)
                        print 'total offensive points: %f'%p
                        print 'total defensive points: %f'%dpoints
                        print 'total points: %f'%(p+dpoints)
                    else:
                        print 'Team is empty'
                elif j==i.rosters[-1] and not tfound: 
                    print 'Team %s not found'%teamName
        elif i==fbTool.leagueLists[-1] and not lfound:
            print 'League %s not found' %leagueName

def saveFileUI():
    fn=getFileName(1)
    if not fbTool.writeClassToFile(fn):
        print 'Successfully output to file %s' % fn
    else:
        print 'File output failed.'

def loadFileUI():
    fn=getFileName(0)
    if not fbTool.readClassFromFile(fn):
        print 'Successfully read from file %s' % fn
    else:
        print 'File input failed.'

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
<<<<<<< HEAD
    choice = '0'
    
    while choice != '15':
        if choice == 'CHOOCHOO':
            os.system('sl')
        if _platform =="linux" or _platform=="linux2":
            if choice == 'CHOOCHOO':
                os.system('sl')
            os.system('clear')
        elif _platform == "win32":
            os.system('cls')
        else:
            print 'This program doesn\'t run on mac...'
            sys.exit()
        print '==================================================================='
        print 'Fantasy Football Team Tool - (UGLY) Command Line Interface'
        print '==================================================================='
        print 'Please choose one of the following options:'
        print '1 - Add league to be tracked'
        print '2 - Add team to an existing league'
        print '3 - Add a player to an existing team\'s roster'
        print '4 - Delete an existing League'
        print '5 - Delete an existing Roster'
        print '6 - Delete an existing Player off of a Roster'
        print '7 - Trade players between Rosters'
        print '8 - Print a list of registered leagues'
        print '9 - Print a list of teams registered to a given league'
        print '10 - Print a list of a team\'s current roster'
        print '11 - Print fantasy points for teams in a league for given week'
        print '12 - Print a specific player\'s points'
        print '13 - Write current league structures to a file'
        print '14 - Read league structures from a file'
        print '15 - Exit the program'
        choice=raw_input('Please enter an option: ').strip()
        if choice == '\n':
            choice = '0'

        if choice in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','moo']:
            if choice=='1':
                addLeagueUI()
                raw_input ('Press return to continue...').strip()
            if choice=='2':
                ln=getLeagueName(0)
                tn=getTeamName(ln)
                addRosterUI(ln,tn,[])
                raw_input('Press return to continue...').strip()
            if choice=='3':
                addPlayerUI()
                raw_input ('Press return to continue...').strip()
            if choice=='4':
                remLeagueUI()
                raw_input ('Press return to continue...').strip()
            if choice=='5':
                remRosterUI()
                raw_input ('Press return to continue...').strip()
            if choice=='6':
                remPlayerUI()
                raw_input ('Press return to continue...').strip()
            if choice=='7':
                tradePlayersUI()
                raw_input ('Press return to continue...').strip()
            if choice=='8':
                printLeagues()
                raw_input ('Press return to continue...').strip()
            if choice=='9':
                printTeams(None)
                raw_input ('Press return to continue...').strip()
            if choice=='10':
                printPlayers(None,None)
                raw_input ('Press return to continue...').strip()
            if choice=='11':
                printPts()
                raw_input ('Press return to continue...').strip()
            if choice=='12':
                playerPointsUI();
                raw_input ('Press return to continue...').strip()
            if choice=='13':
                saveFileUI()
                raw_input ('Press return to continue...').strip()
            if choice=='14':
                loadFileUI()
                raw_input ('Press return to continue...').strip()
            if choice=='15':
                print 'exiting...\n'
            if choice.lower()=='moo': 
                iSWEARImNotGoingInsane()
        else:
            print 'ERROR: Invalid input\n'
            raw_input('Press return to continue...').strip()

        if _platform =="linux" or _platform=="linux2":
            os.system('clear')
        elif _platform == "win32":
            os.system('cls')

=======
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
##    print 'Fantasy Football Team Tool - CLI interface'
##    print 'Please choose one of the following options:'
##    print '1 - Add league to be tracked'
##    print '2 - Add team to an existing league'
##    print '3 - Add a player to an existing team\'s roster'
##    print '4 - Print a list of registered leagues'
##    print '5 - Print a list of teams registered to a given league'
##    print '6 - Print a list of a team\'s current roster'
##    print '7 - Print fantasy points for teams in a league for given week'
##    print '8 - Write current league structures to a file'
##    print '9 - Read league structures from a file'
##    print '10 - Exit the program'
##    choice=raw_input('Please enter an option: ').rstrip()
##    if choice == '\n':
##        choice = '0'
##    
##    while choice != '10':
##        if choice in ['1','2','3','4','5','6','7','8','9','10']:
##            if choice=='1':
##                addLeagueUI()
##            if choice=='2':
##                addRosterUI()
##            if choice=='3':
##                addPlayerUI()
##            if choice=='4':
##                printLeagues()
##            if choice=='5':
##                printTeams()
##            if choice=='6':
##                printPlayers()
##            if choice=='7':
##                printPts()
##            if choice=='8':
##                saveFileUI()
##            if choice=='9':
##                loadfileUI()
##            if choice=='10':
##                print 'exiting...\n'
## 
##        else:
##            print 'ERROR: Invalid input\n'
##            raw_input('Press return to continue...').rstrip()

##        if _platform =="linux" or _platform=="linux2":
##            os.system('clear')
##        elif _platform == "win32":
##            os.system('cls')               
##        print 'Please choose one of the following options:'
##        print '1 - Add league to be tracked'
##        print '2 - Add team to an existing league'
##        print '3 - Add a player to an existing team\'s roster'
##        print '4 - Print a list of registered leagues'
##        print '5 - Print a list of teams registered to a given league'
##        print '6 - Print a list of a team\'s current roster'
##        print '7 - Print fantasy points for teams in a league for given week'
##        print '8 - Write current league structures to a file'
##        print '9 - Read league structures from a file'
##        print '10 - Exit the program'
##        choice = raw_input('Please enter an option: ').rstrip()
##    
##        if choice == '\n':
##            choice = '0'
 
>>>>>>> refs/remotes/origin/Glenbranch
main()
