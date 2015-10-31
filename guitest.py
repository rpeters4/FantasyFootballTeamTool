import sys
import fbTool
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot


a=QApplication(sys.argv)        #app window
w=QMainWindow()                 #base class for all UI objects in pyqt
 

#def quitiNoSave:
#    result = QMessageBox.question()
def bt1():
    
    i=0
def bt2():

    i=0
def bt3():

    i=0
def bt4():

    i=0
def bt5():

    i=0
def bt6():

    i=0
def bt7():

    i=0
def bt8():
    if fbTool.leagueLists:
        fileName = QFileDialog.getSaveFileName()
        fbTool.writeClassToFile(fileName)
    else:
        QMessageBox.critical(w,'lolgg','Nothing to save!')
    i=0
def bt9():
    fileName = QFileDialog.getOpenFileName()
    fbTool.readClassFromFile(fileName)
def bt10():
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
def bt11():
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
    
#    a=QApplication(sys.argv)        #app window
#    w=QMainWindow()                 #base class for all UI objects in pyqt
    w.resize(800,600)
    w.setWindowTitle("FFB team tool v 0.0.1")   #title for the window

    mBar = w.menuBar()
    fileMenu = mBar.addMenu('&File') 

    quitButton = QAction(QIcon('exit24.png'),'Quit',w)
    quitButton.setShortcut('Ctrl+Q')
    quitButton.setStatusTip('Exits program without saving')
    quitButton.triggered.connect(w.close)
    fileMenu.addAction(quitButton)

    button1 = QPushButton('Add new league',w)
    button1.setToolTip('')
    button1.clicked.connect(bt1)
    button1.resize(button1.sizeHint())
    button1.move(15,25)

    button2 = QPushButton('Add roster to league',w)
    button2.setToolTip('This\' do stuff later!')
    button2.clicked.connect(bt2)
    button2.resize(button2.sizeHint())
    button2.move(15,75)

    button3 = QPushButton('Update roster info',w)
    button3.setToolTip('')
    button3.clicked.connect(bt3)
    button3.resize(button3.sizeHint())
    button3.move(15,125)

    button4 = QPushButton('Print current league info',w)
    button4.setToolTip('')
    button4.clicked.connect(bt4)
    button4.resize(button4.sizeHint())
    button4.move(15,175)

    button5 = QPushButton('Print current roster list',w)
    button5.setToolTip('')
    button5.clicked.connect(bt5)
    button5.resize(button5.sizeHint())
    button5.move(15,225)

    button6 = QPushButton('Print current roster list for team',w)
    button6.setToolTip('')
    button6.clicked.connect(bt6)
    button6.resize(button6.sizeHint())
    button6.move(15,275)

    button7 = QPushButton('I\'m pretty sure I need this...',w)
    button7.setToolTip('')
    button7.clicked.connect(bt7)
    button7.resize(button7.sizeHint())
    button7.move(15,325)

    button8 = QPushButton('Save data to file',w)
    button8.setToolTip('')
    button8.clicked.connect(bt8)
    button8.resize(button8.sizeHint())
    button8.move(15,375)

    button9 = QPushButton('Load data from file',w)
    button9.setToolTip('')
    button9.clicked.connect(bt9)
    button9.resize(button9.sizeHint())
    button9.move(15,425)

    button10 = QPushButton('Save and quit',w)
    button10.setToolTip('')
    button10.clicked.connect(bt10)
    button10.resize(button10.sizeHint())
    button10.move(15,475)

    button11 = QPushButton('Quit without saving',w)
    button11.setToolTip('')
    button11.clicked.connect(bt11)
    button11.resize(button11.sizeHint())
    button11.move(15,525)


    w.show()    #shows the window

    sys.exit(a.exec_()) #exits the window?


mainMenu()
exit
