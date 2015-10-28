import sys
import fbTool
from PyQt4.QtGui import *

a = QApplication(sys.argv) #app window

w=QWidget() #base class for all UI objects in pyqt

w.resize(800,600)   #window size so tiny!

w.setWindowTitle("FFB team tool v 0.0.1")   #title for the window

button1 = QPushButton('Add new league',w)
button1.setToolTip('')
button1.clicked.connect(exit)
button1.resize(button1.sizeHint())
button1.move(15,25)

button2 = QPushButton('Add roster to league',w)
button2.setToolTip('This\' do stuff later!')
button2.clicked.connect(exit)
button2.resize(button2.sizeHint())
button2.move(15,75)

button3 = QPushButton('Update roster info',w)
button3.setToolTip('')
button3.clicked.connect(exit)
button3.resize(button3.sizeHint())
button3.move(15,125)

button4 = QPushButton('Print current league info',w)
button4.setToolTip('')
button4.clicked.connect(exit)
button4.resize(button4.sizeHint())
button4.move(15,175)

button5 = QPushButton('Print current roster list',w)
button5.setToolTip('')
button5.clicked.connect(exit)
button5.resize(button5.sizeHint())
button5.move(15,225)

button6 = QPushButton('Print current roster list for team',w)
button6.setToolTip('')
button6.clicked.connect(exit)
button6.resize(button6.sizeHint())
button6.move(15,275)

button7 = QPushButton('I\'m pretty sure I need this...',w)
button7.setToolTip('')
button7.clicked.connect(exit)
button7.resize(button7.sizeHint())
button7.move(15,325)

button8 = QPushButton('Save data to file',w)
button8.setToolTip('')
button8.clicked.connect(exit)
button8.resize(button8.sizeHint())
button8.move(15,375)


button9 = QPushButton('Load data from file',w)
button9.setToolTip('')
button9.clicked.connect(exit)
button9.resize(button9.sizeHint())
button9.move(15,425)

button10 = QPushButton('Save and quit',w)
button10.setToolTip('')
button10.clicked.connect(exit)
button10.resize(button10.sizeHint())
button10.move(15,475)

button11 = QPushButton('Quit without saving',w)
button11.setToolTip('')
button11.clicked.connect(exit)
button11.resize(button11.sizeHint())
button11.move(15,525)


w.show()    #shows the window

sys.exit(a.exec_()) #exits the window?
