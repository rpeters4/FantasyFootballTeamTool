import nflgame
         
class league:
    def __init__(self, leagueName, rosters):
        self.rosters = rosters
        self.leagueName = leagueName

class roster:
    def __init__(self, leagueName, rosterName, players):
            self.leagueName = leagueName
            self.rosterName = rosterName
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
    if leagueLists:
        for i in leagueLists:
            if i.leagueName is leagueName:
                print 'ERROR: League already exists\n'
                break
            if i.leagueName is not leagueName and i is leagueLists[-1]:
                l = league(leagueName, [])
                leagueLists.append(l)
                print 'league added\n'
                break
    else:
        l=league(leagueName,[])
        leagueLists.append(l)

def addRoster(leagueName, rosterName):
    if leagueLists:
        for l in leagueLists:
            if l.leagueName is leagueName and not l.rosters:
                r = roster(leagueName, rosterName, [])
                l.rosters.append(r)
                break
            if l.leagueName is leagueName:
                for r in l.rosters:
                    if r.rosterName is rosterName:
                        print 'ERROR: Team already exists\n'
                        break
                    if r.rosterName is not rosterName and r is l.rosters[-1]:
                        r = roster(leagueName, rosterName, [])
                        l.rosters.append(r)
                        print 'roster added\n'
                        break
            elif l is leagueLists[-1]:
                print 'ERROR: League does not exist\n'
                answer = input('Would you like to add a league? (y/n) ')
                while True is True:
                    if answer in ['y', 'Y', 'Yes', 'yes']:
                        addLeague(leagueName)
                        addRoster(leagueName, rosterName)
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
                break
            elif answer in ['n', 'N', 'No', 'no']:
                break
            else:
                answer = input('Invalid response please try again (y/n)')
            
def addPlayer(leagueName, rosterName, playerName, playerTeam):
    if leagueLists:
        for l in leagueLists:
            if l.leagueName is leagueName:
                print 'matched leagueName...\n'
                for r in l.rosters:
                    if r.rosterName is rosterName:
                        teamName = nflgame.standard_team(playerTeam)
                        playerFound = nflgame.find(playerName, team=teamName)
                        if playerFound:
                            p = playerFound[0]
                            plr2Ad = player(p.player_id, p.first_name, p.last_name, p.team, p.position)
                            playerFound = False
                            for k in l.rosters:
                                for j in k.players:
                                    if plr2Ad.firstName is j.firstName and plr2Ad.lastName is j.lastName and plr2Ad.team is j.team:
                                        print 'ERROR: Player already rostered\n'
                                        playerFound = True
                                        break
                            if not playerFound:
                                print 'adding player...'
                                r.players.append(playerToAdd)
                                break
                        else:   
                            print 'ERROR: Player does not exist\n'
                    elif r is l.rosters[-1] and not playerFound:
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
