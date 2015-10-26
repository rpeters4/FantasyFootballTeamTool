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

def findFL(firstName,lastName,team):        ##finds nflgame.player object
    n=firstName + ' ' + lastName            ##by first/last name and team
    return nflgame.find(n,team)

leagueLists = []

#
#   addLeague - adds a new league to the leagueList, and checks for dups
#
def addLeague(leagueName):                  ##adds new fantasyfootbal league
    if leagueLists:
        for i in leagueLists:
            if i.leagueName is leagueName:
                print 'ERROR: League already exists\n'
                raw_input('Press return to continue...')
                return 1
            if i.leagueName is not leagueName and i is leagueLists[-1]:
                l = league(leagueName, [])
                leagueLists.append(l)
                return 0
    else:
        l=league(leagueName,[])
        leagueLists.append(l)
        return 0

    return 1        #if the if statment doens't trigger, something's wrong.
#
#   addRoster - adds a new team to an existing league.  If league doesn't
#               exist, it adds that too.
#
def addRoster(leagueName, rosterName): 
    if leagueLists:
        for l in leagueLists:
            if l.leagueName == leagueName and not l.rosters:
                r = roster(leagueName, rosterName, [])
                l.rosters.append(r)
                return 0
            if l.leagueName == leagueName:
                for r in l.rosters:
                    if r.rosterName == rosterName:
                        print 'ERROR: Team already exists'
                        return 1
                    if r.rosterName != rosterName and r == l.rosters[-1]:
                        r = roster(leagueName, rosterName, [])
                        l.rosters.append(r)
                        return 0
                    
            elif l == leagueLists[-1] and l.leagueName != leagueName:
                print 'ERROR: League %s does not exist' % leagueName
                answer = raw_input('Would you like to add a league? (y/n) ')
                while True is True:
                    if answer.lower() in ['y', 'yes']:
                        addLeague(leagueName)
                        return addRoster(leagueName, rosterName)
                    elif answer.lower() in ['n', 'no']:
                        return 1
                    else:
                        answer = raw_input('Invalid response please try again (y/n)')
    else:
        print 'ERROR: League list is empty'
        answer = raw_input('Would you like to add a league? (y/n) ')
        while True is True:
            if answer.lower() in ['y', 'yes']:
                addLeague(leagueName)
                return addRoster(leagueName, rosterName)
            elif answer.lower() in ['n', 'no']:
                return 1
            else:
                answer = raw_input('Invalid response please try again (y/n)')

#   addPlayer - adds a player to a specified team in a specified league,
#               if said team or league don't exist, it adds those too
#               also checks for double rostering to prevent any boo boos
#

def addPlayer(leagueName, rosterName, playerName, playerTeam):
    if leagueLists:
        for l in leagueLists:
            if l.leagueName == leagueName:
                for r in l.rosters:
                    if r.rosterName == rosterName:
                        teamName = nflgame.standard_team(playerTeam)
                        playerFound = nflgame.find(playerName, team=teamName)
                        if playerFound:
                            p = playerFound[0]
                            plr2Ad = player(p.player_id, p.first_name, p.last_name, p.team, p.position)
                            for k in l.rosters:
                                if k.players:
                                    for j in k.players:
                                        if plr2Ad.firstName == j.firstName and plr2Ad.lastName == j.lastName and plr2Ad.team == j.team:
                                            print 'ERROR: Player already rostered\n'
                                            return 1
                            r.players.append(plr2Ad)
                            return 0
                        else:   
                            print 'ERROR: Player does not exist\n'
                            return 1
                    elif r == l.rosters[-1]:
                        print 'ERROR: Roster for team %s does not exist\n' % rosterName
                        answer = raw_input('Would you like to add a team? (y/n) ')
                        while True is True:
                            if answer.lower() in ['y', 'yes']:
                                addRoster(leagueName, rosterName)
                                return addPlayer(leagueName, rosterName, playerName, playerTeam)
                            elif answer.lower() in ['n', 'no']:
                                return 1
                            else:
                                answer = input('Invalid response please try again (y/n)')
            elif l is leagueLists[-1]:
                print 'ERROR: League %s does not exist\n' % leagueName
                answer = raw_input('Would you like to add league and team? (y/n) ')
                while True is True:
                    if answer.lower() in ['y', 'yes']:
                        addLeague(leagueName)
                        addRoster(leagueName, rosterName)
                        return addPlayer(leagueName, rosterName, playerName, playerTeam)
                    elif answer.lower() in ['n', 'no']:
                        return 1
                    else:
                        answer = raw_input('Invalid response please try again (y/n)')
    else:
        print 'ERROR: League does not exist\n'
        answer = raw_input('Would you like to add a league? (y/n) ')
        while True is True:
            if answer.lower() in ['y', 'yes']:
                addLeague(leagueName)
                addRoster(leagueName, rosterName)
                return addPlayer(leagueName, rosterName, playerName, playerTeam)
            elif answer.lower() in ['n', 'no']:
                return 1
            else:
                answer = raw_input('Invalid response please try again (y/n)')


#   FILE I/O: push in attributes of leagues, rosters, and players
#             and read them back to save hastle of having to enter
#             everything in manually all the time...
#
#   writeClassToFile and readClassToFile should be self explanitory
#   in their functions...
#   returns: 0= success, 1=trying to write/read nothing to/from file 2 = failed to open file

def writeClassToFile(fileName):
    if not leagueLists:
        print 'nothing to output to file %s\n' %fileName
        return 1
    else:
        wFile = open(fileName,'w')	
        if wFile.closed:
            print 'ERROR: Could not open file %s\n' % fileName
            return 2
        else:
            for i in leagueLists:
                wFile.write('NEWLEAGUE\n')
                wFile.write(i.leagueName+'\n')
                for j in i.rosters:
                    wFile.write('NEWROSTER\n')
                    wFile.write(j.rosterName+'\n')
                    for k in j.players:
                        wFile.write('NEWPLAYER\n')
                        wFile.write(k.firstName+' '+k.lastName+' '+k.team+'\n')
            wFile.close()

def readClassFromFile(fileName):
    try:
        rFile = open(fileName,'r')
    except IOError:
        print 'ERROR: Could not open file %s' % fileName
        return 2
    if rFile.closed:
        print 'ERROR: Could not open file %s' % fileName
        return 2
    else:
        fileText=rFile.read()
        splitText=fileText.splitlines()
        for i in range(0,len(splitText)):
            if splitText[i] == 'NEWLEAGUE':
                i=i+1
                leagueName = splitText[i]
                addLeague(leagueName)
                for j in range(i,len(splitText)):
                    if splitText[j] == 'NEWLEAGUE':
                        break
                    if splitText[j] == 'NEWROSTER':
                        j=j+1
                        rosterName=splitText[j]
                        addRoster(leagueName,rosterName)
                        for k in range(j,len(splitText)):
                            if splitText[k] == 'NEWROSTER' or splitText[k] == 'NEWLEAGUE':
                                break
                            if splitText[k] == 'NEWPLAYER':
                                k=k+1
                                p=splitText[k].split()
                                pname=p[0]+' '+p[1]
                                pteam=p[2]
                                addPlayer(leagueName,rosterName,pname,pteam)

        rFile.close()
        return 0
    
def tradePlayers(players1, players2, leagueNameToTrade, roster1, roster2):
    for l in leagueLists:
        if l.leagueName == leagueNameToTrade:
            leagueOfTrade = l
    if l == None:
        print "Player not on roster"
        return 1
    for r1 in leagueOfTrade.rosters:
        if r1.rosterName == roster1:
            roster1Trade = r1
        if r1.rosterName == roster2:
            roster2Trade = r1
    if roster1Trade == None or roster2Trade == None:
        print "Roster does not exist"
        return 1
    for p1 in players1:
        playerOnRoster = False
        for pl1 in roster1Trade.players:
            if pl1.player_id == p1.playerid:
                playerOnRoster = True
                break
    if playerOnRoster == False:
        print "Player not on roster"
        return 1
    for p2 in players2:
        playerOnRoster = False
        for pl2 in roster2Trade.players:
            if pl2.player_id == p2.playerid:
                playerOnRoster = True
                break
    if playerOnRoster == False:
        print "Player not on roster"
        return 1
    for p1 in players1:
        for pl1 in roster1Trade.players:
            if p1.playerid == pl1.player_id:
                roster1Trade.players.remove(pl1)
        addPlayer(leagueNameToTrade, roster2, p1.full_name, p1.team)
    for p2 in players2:
        for pl2 in roster2Trade.players:
            if p2.playerid == pl2.player_id:
                roster2Trade.players.remove(pl2)
        addPlayer(leagueNameToTrade, roster1, p2.full_name, p2.team)
    print "Trade succesful"
    return 0

def removePlayer(playersToRemove, leagueToRemoveFrom, rosterToRemoveFrom):
    for l in leagueLists:
        if l.leagueName == leagueToRemoveFrom:
            leagueOfRemoval = l
    if l == None:
        print "League does not exist"
        return 1
    for r in leagueOfRemoval.rosters:
        if r.rosterName == rosterToRemoveFrom:
            rosterOfRemoval = r
    if rosterOfRemoval == None:
        print "Roster does not exist"
        return 1
    for p in playersToRemove:
        for player in rosterOfRemoval.players:
            if p.playerid == player.player_id:
                rosterOfRemoval.players.remove(player)
