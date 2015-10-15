import nflgame
      
class league:
    def __init__(self, leagueName, rosters):
        self.rosters = rosters
        self.leagueName = leagueName

class roster:
    def __init__(self, leagueName, teamName, players):
            self.leagueName = leagueName
            self.teamName = teamName
            self.players = players

class player:
    def __init__(self, player_id, firstName, lastName, team, position):
        self.player_id = player_id
        self.firstName = firstName
        self.lastName = lastName
        self.team = team
        self.position = position

leagueLists = []

def addLeague(leagueName):
    l = league(leagueName, [])
    leagueLists.append(l)

def addRoster(leagueName, teamName):
    for l in leagueLists:
        if l.leagueName is leagueName:
            r = roster(leagueName, teamName, [])
            l.rosters.append(r)
        else:
            print "League does not exist"
            #want to add league?  
            
def addPlayer(leagueName,rosterName, playerName):
    for l in leagueLists:
        if l.leagueName is leagueName:
            for r in l.rosters:
                if r.teamName is rosterName:
                    plIDs=find(playerName,team=None)
					if not plIDs
						print "couldn't find player"
					else
						player.player_id = plID[0]
						
