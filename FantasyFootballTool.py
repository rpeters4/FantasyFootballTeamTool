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
    if leagueLists:
        for l in leagueLists:
            if l.leagueName is leagueName:
                r = roster(leagueName, teamName, [])
                l.rosters.append(r)
                break
            elif l is leagueLists[-1]:
                print 'ERROR: League does not exist\n'
                answer = input('Would you like to add a league? (y/n) ')
                while True is True:
                    if answer in ['y', 'Y', 'Yes', 'yes']:
                        addLeague(leagueName)
                        addRoster(leagueName, teamName)
                        break
                    elif answer in ['n', 'N', 'No', 'no']:
                        break
                    else:
                        answer = input('Invalid response please try again (y/n)')
    else:
        print 'ERROR: League does not exist\n'
        answer = input('Would you like to add a league? (y/n) ')
        while True is True:
            if answer in ['y', 'Y', 'Yes', 'yes']:
                addLeague(leagueName)
                addRoster(leagueName, teamName)
                break
            elif answer in ['n', 'N', 'No', 'no']:
                break
            else:
                answer = input('Invalid response please try again (y/n)')
            
def addPlayer(leagueName, rosterName, playerName, playerTeam):
    if leagueLists:
        for l in leagueLists:
            if l.leagueName is leagueName:
                for r in l.rosters:
                    if r.teamName is rosterName:
                        teamName = nflgame.standard_team(playerTeam)
                        playerFound = nflgame.find(playerName, team=teamName)
                        if playerFound:
                            p = playerFound[0]
                            playerToAdd = player(p.player_id, p.first_name, p.last_name, p.team, p.position)
                            r.players.append(playerToAdd)
                            break
                        else:   
                            print 'ERROR: Player does not exist\n'
                    elif r is l.rosters[-1]:
                        print 'ERROR: Roster does not exist\n'
                        answer = input('Would you like to add a team? (y/n) ')
                        while True is True:
                            if answer in ['y', 'Y', 'Yes', 'yes']:
                                addRoster(leagueName, rosterName)
                                addPlayer(leagueName, rosterName, playerName, playerTeam)
                                break
                            elif answer in ['n', 'N', 'No', 'no']:
                                break
                            else:
                                answer = input('Invalid response please try again (y/n)')
                    break                        
            elif l is leagueLists[-1]:
                print 'ERROR: League does not exist\n'
                answer = input('Would you like to add a league? (y/n) ')
                while True is True:
                    if answer in ['y', 'Y', 'Yes', 'yes']:
                        addLeague(leagueName)
                        addRoster(leagueName, rosterName)
                        addPlayer(leagueName, rosterName, playerName, playerTeam)
                        break
                    elif answer in ['n', 'N', 'No', 'no']:
                        break
                    else:
                        answer = input('Invalid response please try again (y/n)')
    else:
        print 'ERROR: League does not exist\n'
        answer = input('Would you like to add a league? (y/n) ')
        while True is True:
            if answer in ['y', 'Y', 'Yes', 'yes']:
                addLeague(leagueName)
                addRoster(leagueName, rosterName)
                addPlayer(leagueName, rosterName, playerName, playerTeam)
                break
            elif answer in ['n', 'N', 'No', 'no']:
                break
            else:
                answer = input('Invalid response please try again (y/n)')
