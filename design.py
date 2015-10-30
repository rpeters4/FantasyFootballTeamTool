# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(523, 543)
        self.window2 = None
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addLeague = QtGui.QPushButton(self.centralwidget)
        self.addLeague.setObjectName(_fromUtf8("addLeague"))
        self.verticalLayout.addWidget(self.addLeague)
        self.addTeam = QtGui.QPushButton(self.centralwidget)
        self.addTeam.setObjectName(_fromUtf8("addTeam"))
        self.verticalLayout.addWidget(self.addTeam)
        self.addPlayer = QtGui.QPushButton(self.centralwidget)
        self.addPlayer.setObjectName(_fromUtf8("addPlayer"))
        self.verticalLayout.addWidget(self.addPlayer)
        self.leagueList = QtGui.QPushButton(self.centralwidget)
        self.leagueList.setObjectName(_fromUtf8("leagueList"))
        self.verticalLayout.addWidget(self.leagueList)
        self.teamList = QtGui.QPushButton(self.centralwidget)
        self.teamList.setObjectName(_fromUtf8("teamList"))
        self.verticalLayout.addWidget(self.teamList)
        self.teamRoster = QtGui.QPushButton(self.centralwidget)
        self.teamRoster.setObjectName(_fromUtf8("teamRoster"))
        self.verticalLayout.addWidget(self.teamRoster)
        self.teamPoints = QtGui.QPushButton(self.centralwidget)
        self.teamPoints.setObjectName(_fromUtf8("teamPoints"))
        self.verticalLayout.addWidget(self.teamPoints)
        self.readFile = QtGui.QPushButton(self.centralwidget)
        self.readFile.setObjectName(_fromUtf8("readFile"))
        self.verticalLayout.addWidget(self.readFile)
        self.writeFile = QtGui.QPushButton(self.centralwidget)
        self.writeFile.setObjectName(_fromUtf8("writeFile"))
        self.verticalLayout.addWidget(self.writeFile)
        self.exit = QtGui.QPushButton(self.centralwidget)
        self.exit.setObjectName(_fromUtf8("exit"))
        self.verticalLayout.addWidget(self.exit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.addLeague.setText(_translate("MainWindow", "Add a league to be tracked", None))
        self.addTeam.setText(_translate("MainWindow", "Add team to an existing league", None))
        self.addPlayer.setText(_translate("MainWindow", "Add a player to an existing team\'s roster", None))
        self.leagueList.setText(_translate("MainWindow", "Print a list of registered leagues", None))
        self.teamList.setText(_translate("MainWindow", "Print a list of teams registered to a given league", None))
        self.teamRoster.setText(_translate("MainWindow", "Print a list of a team\'s current roster", None))
        self.teamPoints.setText(_translate("MainWindow", "Print fantasy points for teams in a league for given week", None))
        self.readFile.setText(_translate("MainWindow", "Read league structures from a file", None))
        self.writeFile.setText(_translate("MainWindow", "Write current league structures to a file", None))
        self.exit.setText(_translate("MainWindow", "Exit the program", None))

