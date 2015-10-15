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
            
def addPlayer(leagueName, rosterName, playerName, playerTeam):
    leagueFound = False
    teamFound = False
    for l in leagueLists:
        if l.leagueName is leagueName:
            leagueFound = True
            for r in l.rosters:
                if r.teamName is rosterName:
                    teamFound
                    teamName = nflgame.standard_team(playerTeam)
                    playerFound = nflgame.find(playerName, team=teamName)
                    if playerFound:
                        p = playerFound[0]
                        playerToAdd = player(p.player_id, p.first_name, p.last_name, p.team, p.position)
                        r.players.append(playerToAdd)
                    else:
                        'ERROR: Player %s not found\n' % playerName
    if not leagueFound:
        print 'ERROR: League %s not found\n' % leagueName
    if not teamFound:
        print 'ERROR: Team %s not found\n' % rosterName

          
addLeague('t')
addRoster('t', 'test')
addPlayer('t', 'test', 'tom brady', 'NE')
addPlayer('NOTREAL','test','tom brady', 'NE')
addPlayer('t','tiffingtonbanderbotter','tom brady','NE')
addPlayer('t','test','Fakel McFakington','NE')

