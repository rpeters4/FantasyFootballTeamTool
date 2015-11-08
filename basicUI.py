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
from sys import platform as _platform
from PyQt4 import QtGui
import sys


def getLeagueName():
    return raw_input('Please enter league name: ').rstrip()

def getTeamName():
    return raw_input('Please enter team name: ').rstrip()

def getFileName(isOut):
    if isOut:
        return raw_input('please input output filename: ').rstrip()
    else:
        return raw_input('please input input filename: ').rstrip()

def addLeagueUI():
    ln=getLeagueName()
    testVar=fbTool.addLeague(ln)
    if not testVar:
        print 'Successfully added league %s!' % ln
    else:
        print 'Failed to add league...'
        if testVar == 1:
            print 'League %s already exists.'%ln
        else:
            print 'something is horribly broken.'
    raw_input('Press return to continue...').rstrip()

def addRosterUI():
    ln=getLeagueName()
    tn=getTeamName()
    testVar=fbTool.addRoster(ln,tn)
    if not testVar:
        print 'Succesfully added roster %s!' % tn
    else:
        print 'Failed to add team...'
        if testVar == 1:
            print 'Team %s already exists in league %s' %(tn,ln)
        if testVar == 2:
            print 'League %s does not exist.'
            userInVar = ' '
            while userInVar.lower() not in ['y','yes','n''no']:
                userInVar = raw_input('Would you like to add it? (y/n): ').rstrip()
                if userInVar.lower() not in ['y','yes','n','no']:
                    print 'invalid input.  please try again.'
            if userInVar.lower() == 'y' or userInVar.lower()=='yes':
                if not fbTool.addLeague(ln):
                    testVar = fbTool.addRoster(ln,tn)
                    if not testVar:
                        print 'Successfully added roster %s!' % tn
                    else:
                        print 'Failed to add roster...'
                else:
                    print 'something is very broken'
    raw_input('Press return to continue...').rstrip()
                    
def addPlayerUI():
    ln=getLeagueName()
    tn=getTeamName()
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
            userInVar = raw_input('Would you like to add it? (y/n): ').rstrip()
            if userInVar.lower() not in ['y','yes','n','no']:
                print 'Invalid input.  Please try again.'
        if userInVar.lower()=='y' or userInVar.lower()=='yes':
            if not fbTool.addRoster(ln,tn):
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
    if testVar == 4:
        print 'League does not exist.'
        userInVar=' '
        while userInVar.lower() not in ['y','yes','n','no']:
            userInVar = raw_input('Would you like to add the league and team? (y/n): ').rstrip()
            if userInVar.lower() not in ['y','yes','no','n']:
                print 'Invalid input.  Please try again.'
        if userInVar.lower()=='y' or userInVar.lower()=='yes':
            if not fbTool.addLeague(ln):
                if not fbTool.addRoster(ln,tn):
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

    raw_input('Press return to continue...').rstrip()

def printLeagues():
    if fbTool.leagueLists:
        it=1
        print 'League# LeagueName'
        for i in fbTool.leagueLists:
            print '%d       %s' %(it,i.leagueName)
            it=it+1
    raw_input('Press return to continue...').rstrip()

def printTeams():
    leagueName=getLeagueName()
    it=1
    for i in fbTool.leagueLists:
        if i.leagueName==leagueName:
            print 'Teams in league %s:'%leagueName
            print '{:4s} {:11s} '.format('Team#','Team Name')
            for j in i.rosters:
                print '{:2d}    {:15s}'.format(it,j.rosterName)
                it=it+1
        elif i==fbTool.leagueLists[-1]:
            print 'error: league not registered'
    raw_input('Press return to continue...')

def printPlayers():
    leagueName=getLeagueName()
    teamName=getTeamName()
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
                    for k in j.players:
                        print '{:14s} {:16s} {:19s} {:10s} {:9s} '.format(str(k.player_id),k.firstName,k.lastName,k.team,k.position)
                elif j==i.rosters[-1] and not tfound: 
                    print 'Team %s not found'%teamName

        elif i==fbTool.leagueLists[-1] and not lfound:
            print 'League %s not found' %leagueName
    raw_input('Press return to continue...').rstrip()


def printPts():
    leagueName=getLeagueName()
    teamName=getTeamName()
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
                        print 'total points: %f'%sum(points)

                    else:
                        print 'Team is empty'
                elif j==i.rosters[-1] and not tfound: 
                    print 'Team %s not found'%teamName
        elif i==fbTool.leagueLists[-1] and not lfound:
            print 'League %s not found' %leagueName
    raw_input('Press return to continue...').rstrip()

def saveFileUI():
    fn=getFileName(1)
    if not fbTool.writeClassToFile(fn):
        print 'Successfully output to file %s' % fn
        raw_input('Press return to continue...').rstrip()
    else:
        print 'File output failed.'
        raw_input('Press return to continue...').rstrip()

def loadFileUI():
    fn=getFileName(0)
    if not fbTool.readClassFromFile(fn):
        print 'Successfully read from file %s' % fn
        raw_input('Press return to continue...').rstrip()
    else:
        print 'File input failed.'
        raw_input('Press return to continue...').rstrip()

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
 
main()
