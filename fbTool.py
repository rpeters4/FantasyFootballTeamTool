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
                break
            if i.leagueName is not leagueName and i is leagueLists[-1]:
                l = league(leagueName, [])
                leagueLists.append(l)
                print 'added league %s\n' % leagueName
                break
    else:
        l=league(leagueName,[])
        leagueLists.append(l)
        print 'added league %s\n'%leagueName
#
#   addRoster - adds a new team to an existing league.  If league doesn't
#               exist, it adds that too.
#
def addRoster(leagueName, rosterName):     ##
    if leagueLists:
        for l in leagueLists:
            if l.leagueName is leagueName and not l.rosters:
                r = roster(leagueName, rosterName, [])
                l.rosters.append(r)
                print 'added team %s to league %s\n' %(rosterName,leagueName)
                break
            if l.leagueName is leagueName:
                for r in l.rosters:
                    if r.rosterName is rosterName:
                        print 'ERROR: Team already exists\n'
                        break
                    if r.rosterName is not rosterName and r is l.rosters[-1]:
                        r = roster(leagueName, rosterName, [])
                        l.rosters.append(r)
                        print 'added team %s to league %s\n'%(rosterName,leagueName)
                        break
            elif l is leagueLists[-1]:
                print 'ERROR: League %s does not exist\n' % leagueName
                answer = raw_input('Would you like to add a league? (y/n) ')
                while True is True:
                    if answer.lower() in ['y', 'yes']:
                        addLeague(leagueName)
                        addRoster(leagueName, rosterName)
                        break
                    elif answer.lower() in ['n', 'no']:
                        break
                    else:
                        answer = raw_input('Invalid response please try again (y/n)')
    else:
        print 'ERROR: League %s does not exist\n' % leagueName
        answer = raw_input('Would you like to add a league? (y/n) ')
        while True is True:
            if answer.lower() in ['y', 'yes']:
                addLeague(leagueName)
                addRoster(leagueName, rosterName)
                break
            elif answer.lower() in ['n', 'no']:
                break
            else:
                answer = raw_input('Invalid response please try again (y/n)')
#
#   addPlayer - adds a player to a specified team in a specified league,
#               if said team or league don't exist, it adds those too
#               also checks for double rostering to prevent any boo boos
#

def addPlayer(leagueName, rosterName, playerName, playerTeam):
    playerFoundFlag = False
    if leagueLists:
        for l in leagueLists:
            if l.leagueName is leagueName:
                for r in l.rosters:
                    if r.rosterName is rosterName:
                        teamName = nflgame.standard_team(playerTeam)
                        playerFound = nflgame.find(playerName, team=teamName)
                        if playerFound:
                            p = playerFound[0]
                            plr2Ad = player(p.player_id, p.first_name, p.last_name, p.team, p.position)
                            playerFoundFlag = False
                            for k in l.rosters:
                                for j in k.players:
                                    if plr2Ad.firstName is j.firstName and plr2Ad.lastName is j.lastName and plr2Ad.team is j.team:
                                        print 'ERROR: Player already rostered\n'
                                        playerFoundFlag = True
                                        break
                            if not playerFoundFlag:
                                print 'adding player %s to %s in %s' %(playerName,rosterName,leagueName)
                                r.players.append(plr2Ad)
                                break
                        else:   
                            print 'ERROR: Player does not exist\n'
                    elif r is l.rosters[-1] and not playerFoundFlag:
                        print 'ERROR: Roster for team %s does not exist\n' % rosterName
                        answer = raw_input('Would you like to add a team? (y/n) ')
                        while True is True:
                            if answer.lower() in ['y', 'yes']:
                                addRoster(leagueName, rosterName)
                                addPlayer(leagueName, rosterName, playerName, playerTeam)
                                break
                            elif answer.lower() in ['n', 'no']:
                                break
                            else:
                                answer = input('Invalid response please try again (y/n)')
            elif l is leagueLists[-1]:
                print 'ERROR: League %s does not exist\n' % leagueName
                answer = raw_input('Would you like to add league and team? (y/n) ')
                while True is True:
                    if answer.lower() in ['y', 'yes']:
                        addLeague(leagueName)
                        addRoster(leagueName, rosterName)
                        addPlayer(leagueName, rosterName, playerName, playerTeam)
                        break
                    elif answer.lower() in ['n', 'no']:
                        break
                    else:
                        answer = raw_input('Invalid response please try again (y/n)')
    else:
        print 'ERROR: League does not exist\n'
        answer = raw_input('Would you like to add a league? (y/n) ')
        while True is True:
            if answer.lower() in ['y', 'yes']:
                addLeague(leagueName)
                addRoster(leagueName, rosterName)
                addPlayer(leagueName, rosterName, playerName, playerTeam)
                break
            elif answer.lower() in ['n', 'no']:
                break
            else:
                answer = raw_input('Invalid response please try again (y/n)')


#   FILE I/O: push in attributes of leagues, rosters, and players
#             and read them back to save hastle of having to enter
#             everything in manually all the time...
#
#   writeClassToFile and readClassToFile should be self explanitory
#   in their functions...

def writeClassToFile(fileName):
    if not leagueLists:
        print 'nothing to output to file %s\n' %fileName
    else:
        wFile = open(fileName,'w')	
        if wFile.closed:
            print 'ERROR: Could not open file %s\n' % fileName
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
            print 'successfully output to file %s\n' % fileName
            wFile.close()

def readClassFromFile(fileName):
    rFile = open(fileName,'r')
    if rFile.closed:
        print 'ERROR: Could not open file %s\n' %fileName
    else:
        fileText=rFile.read()
        splitText=fileText.splitlines()
        #splitText=fileText.split()
        print splitText
        for i in range(0,len(splitText)):
            if splitText[i] == 'NEWLEAGUE':
                print 'in if statment 1\n'
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

        print 'successfully imported data from %s'%fileName
        rFile.close()