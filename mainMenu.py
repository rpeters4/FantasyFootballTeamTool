'''
version history:
    0.0.1   -   proof of concept.  did nothing useful
    0.0.5   -   save and load functions implemented
    0.1.0   -   added in the tree display functionality.  Looks pretty OK!
    0.1.1   -   add league button works
    0.1.2   -   remove roster button works
    0.1.4   -   updateRoster crap implemented
    0.1.5   -   added remove league, revamped remove roster to match styles
'''
import sys
import fbTool
import fpKicker
import fpPlayer
import fpDefense
import fbPlayerPoints
import PyQt4.QtCore
import guiFncs
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#global variables (bad practice?  EHHHHHH)
a=QApplication(sys.argv)        #app window
w=QMainWindow()                 #base class for all UI objects in pyqt
w.setFixedSize(800,600)
w.setWindowTitle("FFB team tool v 0.1.5")   #title for the window
tree=QTreeWidget()
leagueItems=[]
rosterItems=[]
playerItems=[]
openWins=[]
dockWidget= PyQt4.QtGui.QDockWidget()
 
def initializeTree():
    leagueCt = 0
    tree.setHeaderLabels(['','League Name','Team Name','Player Name'])
    tree.setColumnHidden(0,True)
    
def updateTree():
    tree.clear()
    for i in fbTool.leagueLists:
        ins = QTreeWidgetItem(tree)
        ins.setText(1,i.leagueName)
        for j in i.rosters:
            ins1 = QTreeWidgetItem(tree)
            ins1.setText(2,j.rosterName)
            rosterItems.append(ins1)
            ins.addChild(rosterItems[len(rosterItems)-1])
            for k in j.players:
                ins2 = QTreeWidgetItem(tree)
                ins2.setText(3,(k.firstName + ' ' + k.lastName))
                playerItems.append(ins2)
                ins1.addChild(playerItems[len(playerItems)-1])
        leagueItems.append(ins)
        tree.addTopLevelItem(leagueItems[len(leagueItems)-1])
    dockWidget.update()

def bt1():          #add new league
    window = guiFncs.createLeague(w)
def bt2():          #Add new roster
    window = guiFncs.addRoster(w)
def bt3():          #Update roster
    window = guiFncs.updateRoster()
    window.show()
    openWins.append(window)
    #print 'update roster stuff here'
def bt4():          #Remove league
    window = guiFncs.deleteLeague()
    if window!=-1:
        window.show()
        openWins.append(window)
    else:
        QMessageBox.critical(w,'error','No leagues currently registered')
    print 'remove league goes here'
def bt5():          #Remove roster
    window = guiFncs.deleteRoster()
    if window!=-1:
        window.show()
        openWins.append(window)
    else:
        QMessageBox.critical(w,'error','No leagues currently registered')
def bt6():          #Trade between rosters 
    print 'trade UI will go here'
def bt7():          #compare points
    print 'point comparison menu will go here'
def bt8():          #save
    if fbTool.leagueLists:
        fileName = QFileDialog.getSaveFileName()
        fbTool.writeClassToFile(fileName)
    else:
        QMessageBox.critical(w,'lolgg','Nothing to save!')
def bt9():          #loads data in append mode
    fileName = QFileDialog.getOpenFileName()
    fbTool.readClassFromFile(fileName)
    updateTree()

def bt10():         #loads data in destroy mode
    if fbTool.leagueLists:
        te=QMessageBox.question(w,'???','Replace current league data?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if te == QMessageBox.Yes:
            te2=QMessageBox.question(w,'???','Save before doing so?',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if te2 == QMessageBox.Yes:
                fileName=QFileDialog.getSaveFileName()
                fbTool.writeClassToFile(fileName)
            fbTool.leagueLists = []
            fileName = QFileDialog.getOpenFileName()
            fbTool.readClassFromFile(fileName)
    else:
        fileName = QFileDialog.getOpenFileName()
        fbTool.readClassFromFile(fileName)
        updateTree()

def bt11():         #save and quit
    if fbTool.leagueLists:
        fileName = QFileDialog.getSaveFileName()
        if not fbTool.writeClassToFile(fileName):
            sys.exit()
        else:
            QMessageBox.critical(w,'error','Failed saving file.')
            te=QMessageBox.question(w,'???','Do you still want to quit?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            if te==QMessageBox.yes:
                sys.exit()
    else:
        sys.exit()

def bt12():         #quit without saving
    if fbTool.leagueLists:
        te=QMessageBox.question(w,'???','Close without saving?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if te == QMessageBox.Yes:
            sys.exit()
        else:
            QFileDialog.getSaveFileName()
            if not fbTool.writeClassToFile(fileName):
                sys.exit()
            else:
                QMessageBox.critical(w,'error','Failed saving file.')
                te=QMessageBox.question(w,'???','Do you still want to quit?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
                if te==QMessageBox.yes:
                    sys.exit()
    else:
        sys.exit()

def mainMenu():
#declare menubar, doesn't work?
    mBar = w.menuBar()
    fileMenu = mBar.addMenu('&File') 

#Tree view stuff
    initializeTree()
    updateTree()
    dockWidget.setWidget(tree)
    dockWidget.setMaximumWidth(590)
    w.addDockWidget(PyQt4.QtCore.Qt.LeftDockWidgetArea,dockWidget)

#menuBar, doesn't work?
    aLoadButton = QAction(QIcon('exit24.png'),'Load From file (append)',w)
    aLoadButton.setShortcut('Ctrl+l')
    aLoadButton.setStatusTip('Appends from file to current leagues')
    aLoadButton.triggered.connect(bt9)
    
    dLoadButton = QAction(QIcon('exit24.png'),'Load from file (replace)',w)
    dLoadButton.setShortcut('Ctrl+d')
    dLoadButton.setStatusTip('Loads from file, replaces current leagues')
    dLoadButton.triggered.connect(bt10)
    
    saveButton = QAction(QIcon('exit24.png'),'Save to file',w)
    saveButton.setShortcut('Ctrl+S')
    saveButton.setStatusTip('Saves current leagues to file')
    saveButton.triggered.connect(bt8)
    
    quitButton = QAction(QIcon('exit24.png'),'Quit',w)
    quitButton.setShortcut('Ctrl+Q')
    quitButton.setStatusTip('Exits program without saving')
    quitButton.triggered.connect(bt12)

    fileMenu.addAction(aLoadButton)
    fileMenu.addAction(dLoadButton)
    fileMenu.addAction(saveButton)
    fileMenu.addAction(quitButton)

#BUTTONS!
    button1 = QPushButton('Add new league',w)
    button2 = QPushButton('Add roster to league',w)
    button3 = QPushButton('Update roster info',w)
    button4 = QPushButton('Remove League(s)',w)
    button5 = QPushButton('Remove Roster(s)',w)
    button6 = QPushButton('Trade Between Rosters',w)
    button7 = QPushButton('Compare Points',w) #declared here cos it's long
    button8 = QPushButton('Save to File',w)
    button9 = QPushButton('Load from File(append)',w)
    button10 = QPushButton('Load from File (replace)',w)
    button11 = QPushButton('Save And Quit',w)
    button12 = QPushButton('Quit without saving',w)

#BUTTON HOVER OVER TEXT
    button1.setToolTip('Add a new league to be tracked by the program')
    button2.setToolTip('Add a new roster to one of the leagues being tracked')
    button3.setToolTip('Manage the players on specific team')
    button4.setToolTip('Removes a league from program\'s memory')
    button5.setToolTip('Removes a team from a league')
    button6.setToolTip('Trade players from one team to another')
    button7.setToolTip('Compare fantasy points of teams')
    button8.setToolTip('Save the current data to a designated output file')
    button9.setToolTip('Load data from specified data file and append it\'s contents to the current database')
    button10.setToolTip('Load data from specified data file and replace the contents to the current database with the contents of the file')
    button11.setToolTip('Save current database to a file and exit')
    button12.setToolTip('GET OUT!  WE DON\'T WANT YOU ANYWAY')

#BUTTON WAS CLICKED
    button1.clicked.connect(bt1)
    button2.clicked.connect(bt2)
    button3.clicked.connect(bt3)
    button4.clicked.connect(bt4)
    button5.clicked.connect(bt5)
    button6.clicked.connect(bt6)
    button7.clicked.connect(bt7)
    button8.clicked.connect(bt8)
    button9.clicked.connect(bt9)
    button10.clicked.connect(bt10)
    button11.clicked.connect(bt11)
    button12.clicked.connect(bt12) 
    a.aboutToQuit.connect(bt12) #if the 'x' button is pressed, prompt to save
    
#BUTTON SIZES
    button1.resize(button10.sizeHint())
    button2.resize(button10.sizeHint())
    button3.resize(button10.sizeHint())
    button4.resize(button10.sizeHint())
    button5.resize(button10.sizeHint())
    button6.resize(button10.sizeHint())
    button7.resize(button10.sizeHint())
    button8.resize(button10.sizeHint())
    button9.resize(button10.sizeHint())
    button10.resize(button10.sizeHint())
    button11.resize(button10.sizeHint())
    button12.resize(button10.sizeHint())

#BUTTON POSITIONS
    button1.move(610,10)
    button2.move(610,60)
    button3.move(610,110)
    button4.move(610,160)
    button5.move(610,210)
    button6.move(610,260)
    button7.move(610,310)
    button8.move(610,360)
    button9.move(610,410)
    button10.move(610,460)
    button11.move(610,510)
    button12.move(610,560)

    w.show()    #shows the window
    sys.exit(a.exec_())

