'''
version history:
    0.0.1   -   proof of concept.  did nothing useful
    0.0.5   -   save and load functions implemented
    0.1.0   -   added in the tree display functionality.  Looks pretty OK!
'''

import sys
import fbTool
#import basicUI
import fpKicker
import fpPlayer
import fpDefense
import fbPlayerPoints
import PyQt4.QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#global variables (bad practice?  EHHHHHH)
a=QApplication(sys.argv)        #app window
w=QMainWindow()                 #base class for all UI objects in pyqt
w.setFixedSize(800,600)
w.setWindowTitle("FFB team tool v 0.1.0")   #title for the window
tree=QTreeWidget()
leagueItems=[]
teamItems=[]
playerItems=[]
dockWidget= PyQt4.QtGui.QDockWidget()
 
def initializeTree():
    leagueCt = 0
    tree.setHeaderLabels(['','League Name','Team Name','Player Name'])
    
    
def updateTree():
    tree.clear()
    for i in fbTool.leagueLists:
        ins = QTreeWidgetItem(tree)
        ins.setText(1,i.leagueName)
        for j in i.rosters:
            ins1 = QTreeWidgetItem(tree)
            ins1.setText(2,j.rosterName)
            teamItems.append(ins1)
            ins.addChild(teamItems[len(teamItems)-1])
            for k in j.players:
                ins2 = QTreeWidgetItem(tree)
                ins2.setText(3,(k.firstName + ' ' + k.lastName))
                playerItems.append(ins2)
                ins1.addChild(playerItems[len(playerItems)-1])
        leagueItems.append(ins)
        tree.addTopLevelItem(leagueItems[len(leagueItems)-1])

    dockWidget.update()

def bt1():          #add new league
    print 'add league goes here'
    i=0
def bt2():          #Add new roster
    print 'add roster goes here'
    i=0
def bt3():          #Update roster
    print 'update roster stuff here'
    i=0
def bt4():          #Remove league
    print 'remove league goes here'
    i=0
def bt5():          #Remove roster
    print 'remove roster goes here'
    i=0
def bt6():          #Trade between rosters 
    print 'trade UI will go here'
    i=0
def bt7():          #compare points
    print 'point comparison menu will go here'
    i=0
def bt8():          #save
    if fbTool.leagueLists:
        fileName = QFileDialog.getSaveFileName()
        fbTool.writeClassToFile(fileName)
    else:
        QMessageBox.critical(w,'lolgg','Nothing to save!')
    i=0
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
            updateTree()
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

def guiMenu():
#declare menubar, doesn't work?
    mBar = w.menuBar()
    fileMenu = mBar.addMenu('&File') 

#Tree view stuff
    initializeTree()
    updateTree()
    dockWidget.setWidget(tree)
    dockWidget.setMaximumWidth(540)
    w.addDockWidget(PyQt4.QtCore.Qt.LeftDockWidgetArea,dockWidget)

#menuBar, doesn't work?
    quitButton = QAction(QIcon('exit24.png'),'Quit',w)
    quitButton.setShortcut('Ctrl+Q')
    quitButton.setStatusTip('Exits program without saving')
    quitButton.triggered.connect(w.close)
    fileMenu.addAction(quitButton)

#BUTTONS!
    button1 = QPushButton('Add new league',w)
    button2 = QPushButton('Add roster to league',w)
    button3 = QPushButton('Update roster info',w)
    button4 = QPushButton('Remove League',w)
    button5 = QPushButton('Remove Team',w)
    button6 = QPushButton('Trade Between Teams',w)
    button7 = QPushButton('Compare Points Between Teams',w) #declared here cos it's long
    button8 = QPushButton('Save to File',w)
    button9 = QPushButton('Load from File(append)',w)
    button10 = QPushButton('Load from File (replace)',w)
    button11 = QPushButton('Save And Quit',w)
    button12 = QPushButton('Quit without saving',w)

#BUTTON HOVER OVER TEXT
    button1.setToolTip('')
    button2.setToolTip('This\' do stuff later!')
    button3.setToolTip('')
    button4.setToolTip('')
    button5.setToolTip('')
    button6.setToolTip('')
    button7.setToolTip('')
    button8.setToolTip('')
    button9.setToolTip('')
    button10.setToolTip('')
    button11.setToolTip('')
    button12.setToolTip('')

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
    button1.resize(button7.sizeHint())
    button2.resize(button7.sizeHint())
    button3.resize(button7.sizeHint())
    button4.resize(button7.sizeHint())
    button5.resize(button7.sizeHint())
    button6.resize(button7.sizeHint())
    button7.resize(button7.sizeHint())
    button8.resize(button7.sizeHint())
    button9.resize(button7.sizeHint())
    button10.resize(button7.sizeHint())
    button11.resize(button7.sizeHint())
    button12.resize(button7.sizeHint())

#BUTTON POSITIONS
    button1.move(550,10)
    button2.move(550,60)
    button3.move(550,110)
    button4.move(550,160)
    button5.move(550,210)
    button6.move(550,260)
    button7.move(550,310)
    button8.move(550,360)
    button9.move(550,410)
    button10.move(550,460)
    button11.move(550,510)
    button12.move(550,560)

    w.show()    #shows the window
    
    sys.exit(a.exec_()) 

guiMenu()
exit()
