import nflgame

class league:
    def __init__(self, leagueName, rosters):
        self.rosters = rosters
        self.leagueName = leagueName

class roster:
    def __init__(self, leagueName, rosterName, players, defense):
            self.leagueName = leagueName
            self.rosterName = rosterName
            self.players = players
            self.defense = defense


class player:
    def __init__(self, player_id, firstName, lastName, team, position):
        self.player_id = player_id
        self.firstName = firstName
        self.lastName = lastName
        self.team = team
        self.position = position
        self.active = True

def findFL(firstName,lastName,team):        ##finds nflgame.player object
    n=firstName + ' ' + lastName            ##by first/last name and team
    return nflgame.find(n,team)

leagueLists = []
#
#   addLeague - adds a new league to the leagueList, and checks for dups
#   returns: 0 = success, 1 = league already exists,2=invalid name
def addLeague(leagueName):                  ##adds new fantasyfootbal league
    if leagueName in ['\n','',' ','  ','   ','    ']:
        return 2
    if not leagueLists:
        l=league(leagueName,[])
        leagueLists.append(l)
        return 0

    for i in leagueLists:
        if i.leagueName == leagueName:
            return 1

    l = league(leagueName, [])
    leagueLists.append(l)
    return 0
#
#   addRoster - adds a new team to an existing league.  If league doesn't
#               exist, it adds that too.  Note, defTeam is a list of standard
#		team names that will be used for defense.
#   returns: 0 = success, 1 = team already exists, 2 = league doesn't exist
#   3+n = defense team #{0,1,2,....n} already taken by other team in league
def addRoster(leagueName, rosterName, defTeam): 
    if not leagueLists:
        return 2
    for l in leagueLists:
        if l.leagueName == leagueName and not l.rosters:
            r = roster(leagueName, rosterName, [], [])
            for de in defTeam:
                r.defense.append(de)
            l.rosters.append(r)
            return 0
        if l.leagueName == leagueName:
            for r in l.rosters:
                if r.rosterName == rosterName:
                    return 1
                count =0
                for x in defTeam:
                    if x in r.defense:
                        return 3+count
                    count = count + 1
            r = roster(leagueName, rosterName, [], [])
            for de in defTeam:
                r.defense.append(de)
            l.rosters.append(r)
            return 0
                
        elif l == leagueLists[-1] and l.leagueName != leagueName:
                return 2
    else:
        return 2

#   addPlayer - adds a player to a specified team in a specified league,
#               if said team or league don't exist, it adds those too
#               also checks for double rostering to prevent any boo boos
#   returns: 0 = success, 1 = player already rostered, 2 = player doesn't exist
#   3 = team doesn't exist, 4 = league doesn't exist

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
                                            return 1
                            r.players.append(plr2Ad)
                            return 0
                        else:   
                            return 2
                    elif r == l.rosters[-1]:
                        return 3
            elif l is leagueLists[-1]:
                return 4
    else:
        return 4

def addBenchedPlayer(leagueName, rosterName, playerName, playerTeam):
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
                            plr2Ad.active=False
                            for k in l.rosters:
                                if k.players:
                                    for j in k.players:
                                        if plr2Ad.firstName == j.firstName and plr2Ad.lastName == j.lastName and plr2Ad.team == j.team:
                                            return 1
                            r.players.append(plr2Ad)
                            return 0
                        else:   
                            return 2
                    elif r == l.rosters[-1]:
                        return 3
            elif l is leagueLists[-1]:
                return 4
    else:
        return 4
#   FILE I/O: push in attributes of leagues, rosters, and players
#             and read them back to save hastle of having to enter
#             everything in manually all the time...
#
#   writeClassToFile and readClassToFile should be self explanitory
#   in their functions...
#   returns: 0 = success, 1=trying to write/read nothing to/from file 2 = failed to open file
#   3 = invalid file format (read)

def writeClassToFile(fileName):
    if not leagueLists:
        return 1
    else:
        wFile = open(fileName,'w')	
        if wFile.closed:
            return 2
        else:
            for i in leagueLists:
                wFile.write('NEWLEAGUE\n')
                wFile.write(i.leagueName+'\n')
                for j in i.rosters:
                    wFile.write('NEWROSTER\n')
                    wFile.write(j.rosterName+'\n')
                    for l in j.defense:
                        wFile.write(l+'\n')
                    wFile.write('ENDDEF\n')
                    for k in j.players:
                        wFile.write('NEWPLAYER\n')
                        wFile.write(k.firstName+' '+k.lastName+' '+k.team+'\n')
                        if not k.active:
                            wFile.write('BENCHED\n')
            wFile.close()

def readClassFromFile(fileName):
    try:
        rFile = open(fileName,'r')
    except IOError:
        return 2
    if rFile.closed:
        return 2
    else:
        fileText=rFile.read()
        splitText=fileText.splitlines()
        if splitText[0] != 'NEWLEAGUE':
            return 3
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
                        defen = []
                        j=j+1
                        while splitText[j]!='ENDDEF':
                            defName = splitText[j]
                            defen.append(defName)
                            j=j+1
                        j=j+1
                        addRoster(leagueName,rosterName,defen)
                        for k in range(j,len(splitText)):
                            if splitText[k] == 'NEWROSTER' or splitText[k] == 'NEWLEAGUE':
                                break
                            if splitText[k] == 'NEWPLAYER':
                                k=k+1
                                p=splitText[k].split()
                                if k<len(splitText)-1:
                                    k=k+1
                                pname=p[0]+' '+p[1]
                                pteam=p[2]
                                if splitText[k]=='BENCHED':
                                        addBenchedPlayer(leagueName,rosterName,pname,pteam)
                                        k=k+1
                                else:
                                    addPlayer(leagueName,rosterName,pname,pteam)

        rFile.close()
        return 0
   
#returns: 0 = success, 1 = league doesn't exist, 2 = roster doesn't exist
#   3 = player not on roster 
def tradePlayers(players1, players2, leagueNameToTrade, roster1, roster2):
    for l in leagueLists:
        if l.leagueName == leagueNameToTrade:
            leagueOfTrade = l
    if l == None:
        return 1
    for r1 in leagueOfTrade.rosters:
        if r1.rosterName == roster1:
            roster1Trade = r1
        if r1.rosterName == roster2:
            roster2Trade = r1
    if roster1Trade == None or roster2Trade == None:
        return 1
    for p1 in players1:
        print p1.player_id
        playerOnRoster = False
        for pl1 in roster1Trade.players:
            print pl1.player_id
            if pl1.firstName == p1.first_name and pl1.lastName == pl1.lastName:
                playerOnRoster = True
                break
            if not playerOnRoster and pl1 == roster1Trade.players[-1]:
                return 3
    for p2 in players2:
        print 'p2 is %s %s'%(p2.first_name,p2.last_name)
        print 'p2.player_id=%s'%p2.player_id
        print 'p2.team = %s'% p2.team
        playerOnRoster = False
        for pl2 in roster2Trade.players:
            print 'pl2 is %s %s' %(pl2.firstName,pl2.lastName)
            print 'pl2.player_id = %s'%pl2.player_id
            print 'pl2.team = %s' % pl2.team
            if pl2.firstName == p2.first_name and pl2.lastName == p2.last_name:
                playerOnRoster = True
                break
            if not playerOnRoster and pl2 == roster2Trade.players[-1]:
                return 3
    for p1 in players1:
        for pl1 in roster1Trade.players:
            if p1.first_name == pl1.firstName and p1.last_name == pl1.lastName:
                roster1Trade.players.remove(pl1)
        addPlayer(leagueNameToTrade, roster2, p1.full_name, p1.team)
    for p2 in players2:
        for pl2 in roster2Trade.players:
            if p2.first_name == pl2.firstName and p2.last_name == pl2.lastName:
                roster2Trade.players.remove(pl2)
        addPlayer(leagueNameToTrade, roster1, p2.full_name, p2.team)
    return 0

#returns: 0 = success, 1 = league doesn't exist, 2 = roster doesn't exist
#   3 = player not on roster 
def removePlayer(playersToRemove, leagueToRemoveFrom, rosterToRemoveFrom):
    for l in leagueLists:
        if l.leagueName == leagueToRemoveFrom:
            leagueOfRemoval = l
    if l == None:
        return 1
    for r in leagueOfRemoval.rosters:
        if r.rosterName == rosterToRemoveFrom:
            rosterOfRemoval = r
    if rosterOfRemoval == None:
        return 2
    for p in playersToRemove:
        for player in rosterOfRemoval.players:
            if p.playerid == player.player_id:
                rosterOfRemoval.players.remove(player)
                return 0
    return 3

#returns: 0 = success, 1 = league doesn't exist, 2 = roster doesn't exist
def removeRoster(leagueFrom,rosterName):
    for i in leagueLists:
        if i.leagueName == leagueFrom:
            for j in i.rosters:
                if j.rosterName == rosterName:
                    i.rosters.remove(j)
                    return 0
            return 2
    return 1

#returns: 0 = success, 1 = league doesn't exist
def removeLeague(leagueName):
    for i in leagueLists:
        if i.leagueName == leagueName:
            leagueLists.remove(i)
            return 0
    return 1

def setPlayerActiveFlag(player):
    if player.active:
        player.active = False
    else:
        player.active = True
