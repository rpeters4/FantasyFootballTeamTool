from PyQt4 import QtGui
import sys
import design
#import basicUI
import os
import nflgame
import kicking

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.kicka)

    #def kick(playerName, year, week):
      #  if nflgame.find(playerName, team=None):
      #      playa = nflgame.find(playerName, team=None) [0]
            #games = nflgame.games(year, week)
            #plays = nflgame.combine_plays(games)
            #all_made_fgs = plays.filter(kicking_fgm=True)
            #for p in all_made_fgs:
             #   if p.players.playerid(playa.playerid):
              #      return p.kicking_fgm_yds
    
		
    def kicka(self):
        self.listWidget.clear()
        self.listWidget.addItem(str(basicUI.addLeagueUI()))
        #self.listWidget.addItem("Justin Tucker has made field goals of: ")
        #self.listWidget.addItem(str(kicking.kick("Justin Tucker", 2015, 1)))
        print "yess"

		
def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()
	
	
if __name__ == '__main__':
    main()
	
