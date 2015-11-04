import sys
import fbTool
import basicUI
import fpKicker
import fpPlayer
import fpDefense
import fbPlayerPoints
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot


a=QApplication(sys.argv)        #app window
w=QMainWindow()                 #base class for all UI objects in pyqt
leagues=[]
teams=[]
players=[]

#def quitiNoSave:
#    result = QMessageBox.question()
def bt1():          #add new league
    basicUI.printLeagues()
    basicUI.printTeams('nfl')
    basicUI.printTeams('t')
    basicUI.printPlayers('nfl','bills')
    i=0
def bt2():          #Add new roster

    i=0
def bt3():          #Update roster

    i=0
def bt4():          #Remove league

    i=0
def bt5():          #Remove roster

    i=0
def bt6():          #Trade between rosters 

    i=0
def bt7():          #compare points

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

def bt10():         #loads data in destroy mode
    if fbTool.leagueLists:
        te=QMessageBox.question(w,'???','Replace current league data?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if te == QMessageBox.Yes:
            te2=QMessageBox.question(w,'???','Save before doing so?',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if te2 == QMessageBox.Yes:
                bt8
            fbTool.leagueLists = []
            fileName = QFileDialog.getOpenFileName()
            fbTool.readClassFromFile(fileName)
    else:
        fileName = QFileDialog.OpenFileName()
        fbTool.readClassFromFile(fileName)

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

def bt11():         #quit without saving
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
    
#    a=QApplication(sys.argv)        #app window
#    w=QMainWindow()                 #base class for all UI objects in pyqt
    w.setFixedSize(800,600)
    w.setWindowTitle("FFB team tool v 0.0.1")   #title for the window

    mBar = w.menuBar()
    fileMenu = mBar.addMenu('&File') 

    quitButton = QAction(QIcon('exit24.png'),'Quit',w)
    quitButton.setShortcut('Ctrl+Q')
    quitButton.setStatusTip('Exits program without saving')
    quitButton.triggered.connect(w.close)
    fileMenu.addAction(quitButton)

    button7 = QPushButton('Compare Points Between Teams',w) #declared here cos it's long
 
    button1 = QPushButton('Add new league',w)
    button1.setToolTip('')
    button1.clicked.connect(bt1)
    button1.resize(button7.sizeHint())
    button1.move(15,10)

    button2 = QPushButton('Add roster to league',w)
    button2.setToolTip('This\' do stuff later!')
    button2.clicked.connect(bt2)
    button2.resize(button7.sizeHint())
    button2.move(15,60)

    button3 = QPushButton('Update roster info',w)
    button3.setToolTip('')
    button3.clicked.connect(bt3)
    button3.resize(button7.sizeHint())
    button3.move(15,110)

    button4 = QPushButton('Remove League',w)
    button4.setToolTip('')
    button4.clicked.connect(bt4)
    button4.resize(button7.sizeHint())
    button4.move(15,160)

    button5 = QPushButton('Remove Team',w)
    button5.setToolTip('')
    button5.clicked.connect(bt5)
    button5.resize(button7.sizeHint())
    button5.move(15,210)

    button6 = QPushButton('Trade Between Teams',w)
    button6.setToolTip('')
    button6.clicked.connect(bt6)
    button6.resize(button7.sizeHint())
    button6.move(15,260)

    button7.setToolTip('')
    button7.clicked.connect(bt7)
    button7.resize(button7.sizeHint())
    button7.move(15,310)

    button8 = QPushButton('Save to File',w)
    button8.setToolTip('')
    button8.clicked.connect(bt8)
    button8.resize(button7.sizeHint())
    button8.move(15,360)

    button9 = QPushButton('Load from File(append)',w)
    button9.setToolTip('')
    button9.clicked.connect(bt9)
    button9.resize(button7.sizeHint())
    button9.move(15,410)

    button10 = QPushButton('Load from File(replace)',w)
    button10.setToolTip('')
    button10.clicked.connect(bt10)
    button10.resize(button7.sizeHint())
    button10.move(15,460)

    button11 = QPushButton('Save And Quit',w)
    button11.setToolTip('')
    button11.clicked.connect(bt11)
    button11.resize(button7.sizeHint())
    button11.move(15,510)

    button12 = QPushButton('Quit without saving',w)
    button12.setToolTip('')
    button12.clicked.connect(bt11)
    button12.resize(button7.sizeHint())
    button12.move(15,560)

    

    w.show()    #shows the window

    sys.exit(a.exec_()) #exits the window?


guiMenu()
exit
