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
                    if answer is in ['y', 'Y', 'Yes', 'yes']:
                        addLeague(leagueName)
                        addRoster(leagueName, teamName)
                        break
                    elif answer is in['n', 'N', 'No', 'no']:
                        break
                    else:
                        answer = input('Invalid response please try again (y/n)')
    else:
        print 'ERROR: League does not exist\n'
        answer = input('Would you like to add a league? (y/n) ')
        while True is True:
            if answer is in ['y', 'Y', 'Yes', 'yes']:
                addLeague(leagueName)
                addRoster(leagueName, teamName)
                break
            elif answer is in['n', 'N', 'No', 'no']:
                break
            else:
                answer = input('Invalid response please try again (y/n)')
            
def addPlayer(leagueName, rosterName, playerName, playerTeam):
    foundLeague = False
    foundRoster = False
    for l in leagueLists:
        if l.leagueName is leagueName and foundLeague is False:
            foundLeague = True
            for r in l.rosters:
                if r.teamName is rosterName and foundRoster is False:
                    foundRoster = True
                    teamName = nflgame.standard_team(playerTeam)
                    playerFound = nflgame.find(playerName, team=teamName)
                    if playerFound:
                        p = playerFound[0]
                        playerToAdd = player(p.player_id, p.first_name, p.last_name, p.team, p.position)
                        r.players.append(playerToAdd)
                    else:
                        'ERROR: Player %s not found\n' % playerName
                elif r.teamName is not rosterName and foundRoster is False:
                    print 'ERROR: Team does not exist\n'
                    print 'Would you like to add a team? '
                    answer = input('(y/n)')
                    while True:
                        if answer is 'y' or 'Y' or 'Yes' or 'yes':
                            addRoster(leagueName, RosterName)
                            break
                        elif answer is not 'n' or 'N' or 'No' or 'no':
                            print 'Invalid response please try again'
                            answer = input('(y/n)')
                        else:
                            break
                        
        elif l.leagueName is not leagueName and foundLeague is False:
            print 'ERROR: League does not exist\n'
            print 'Would you like to add a league? '
            answer = input('(y/n)')
            while True:
                if answer is 'y' or 'Y' or 'Yes' or 'yes':
                    addLeague(leagueName)
                    break
                elif answer is not 'n' or 'N' or 'No' or 'no':
                    print 'Invalid response please try again'
                    answer = input('(y/n)')
                else:
                    break
