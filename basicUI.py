import nflgame
import fbTool
import os
import fpPlayer
import fpKicker
import fpDefense
import fbPlayerPoints
from sys import platform as _platform

def getLeagueName():
    return raw_input('Please enter league name: ').strip()

def getTeamName():
    return raw_input('Please enter team name: ').strip()

def getFileName(isOut):
    if isOut:
        return raw_input('please input output filename: ').strip()
    else:
        return raw_input('please input input filename: ').strip()

def addLeagueUI():
    ln=getLeagueName()
    testVar=fbTool.addLeague(ln)
    if not testVar:
        print 'Successfully added league %s!' % ln
    else:
        print 'Failed to add league...'
        if testVar == 1:
            print 'League %s already exists.'%ln
        else:
            print 'something is horribly broken.'
    raw_input('Press return to continue...').strip()

def addRosterUI():
    ln=getLeagueName()
    tn=getTeamName()
    inp='y'
    defense = []
    while inp.lower() not in ['n' or 'no']:
        if inp.lower()=='y' or inp.lower()=='yes':
            defen=raw_input('Please enter team name for defense: ').strip()
            while nflgame.standard_team(defen) is None:
                defen=raw_input('Invalid team name, please try again: ').strip()
            defen=nflgame.standard_team(defen)
            defense.append(defen)
        else:
            print 'invalid input, try again.'
        inp = raw_input('Would you like to add another team for defense? (y/n): ' ).strip()
    testVar=fbTool.addRoster(ln,tn,defense)
    if not testVar:
        print 'Succesfully added roster %s!' % tn
    else:
        print 'Failed to add team...'
        if testVar == 1:
            print 'Team %s already exists in league %s' %(tn,ln)
        if testVar == 2:
            print 'League %s does not exist.'
            userInVar = ' '
            while userInVar.lower() not in ['y','yes','n''no']:
                userInVar = raw_input('Would you like to add it? (y/n): ').strip()
                if userInVar.lower() not in ['y','yes','n','no']:
                    print 'invalid input.  please try again.'
            if userInVar.lower() == 'y' or userInVar.lower()=='yes':
                if not fbTool.addLeague(ln):
                    testVar = fbTool.addRoster(ln,tn,roster)
                    if not testVar:
                        print 'Successfully added roster %s!' % tn
                    else:
                        print 'Failed to add roster...'
    raw_input('Press return to continue...').strip()
                    
def addPlayerUI():
    ln=getLeagueName()
    tn=getTeamName()
    plName=raw_input('Please input the desired player to add\'s name: ')
    plTeam=raw_input('Please input the desired player\'s NFL team: ')
    testVar=fbTool.addPlayer(ln,tn,plName,plTeam)
    if not testVar:
        print 'Succesfully added %s to %s from league %s' % (plName,tn,ln)
    else:
        print 'Failed to add player...'
    if testVar == 1:
        print 'Player already rostered in league %s'%ln
    if testVar == 2:
        print 'Player %s not found in database'%plName
    if testVar == 3:
        print 'Team does not exist.'
        userInVar = ' '
        while userInVar.lower() not in ['y','yes','n','no']:
            userInVar = raw_input('Would you like to add it? (y/n): ').strip()
            if userInVar.lower() not in ['y','yes','n','no']:
                print 'Invalid input.  Please try again.'
        if userInVar.lower()=='y' or userInVar.lower()=='yes':
            if not fbTool.addRoster(ln,tn):
                testVar = fbTool.addPlayer(ln,tn,plName,plTeam)
                if not testVar:
                    print 'Successfully added %s to %s from league %s' %(plName,tn,ln)
                else:
                    print 'Failed to add player.'
                if testVar == 1:
                  print 'Player already rostered in league %s'%ln
                if testVar == 2:
                    print 'Player %s not found in database'%plName
            else:
                print 'Failed to add roster.'
    if testVar == 4:
        print 'League does not exist.'
        userInVar=' '
        while userInVar.lower() not in ['y','yes','n','no']:
            userInVar = raw_input('Would you like to add the league and team? (y/n): ').strip()
            if userInVar.lower() not in ['y','yes','no','n']:
                print 'Invalid input.  Please try again.'
        if userInVar.lower()=='y' or userInVar.lower()=='yes':
            if not fbTool.addLeague(ln):
                if not fbTool.addRoster(ln,tn):
                    testVar =fbTool.addPlayer(ln,tn,plName,plTeam)
                    if not testVar:
                        print 'Successfully added %s to %s from league %s' %(plName,tn,ln)
                    else:
                        print 'Failed to add player.'
                    if testVar == 1:
                        print 'Player already rostered in league %s'%ln
                    if testVar == 2:
                        print 'Player %s not found in database'%plName
                else:
                    print 'failed to add team to league'
            else:
                print 'something went horribly wrong.'

    raw_input('Press return to continue...').strip()

def playerPointsUI():
    playerInfo = []
    points = 0
    playerInfo.append(raw_input("Enter player: ").strip())
    playerInfo.append(int(raw_input("Enter year: ")))
    w1 = raw_input("Enter week(s): ").strip()
    playerInfo.append(map(int, w1.split()))
    points = fbPlayerPoints.playerPoints(playerInfo)
    if points == float('inf'):
        print 'Player does not exist'
    print points
    raw_input('Press return to continue...').strip()
    return points

def printLeagues():
    if fbTool.leagueLists:
        it=1
        print 'League# LeagueName'
        for i in fbTool.leagueLists:
            print '%d       %s' %(it,i.leagueName)
            it=it+1
    raw_input('Press return to continue...').strip()

def printTeams():
    leagueName=getLeagueName()
    it=1
    for i in fbTool.leagueLists:
        if i.leagueName==leagueName:
            print 'Teams in league %s:'%leagueName
            print '{:4s} {:11s} '.format('Team#','Team Name')
            for j in i.rosters:
                print '{:2d}    {:15s}'.format(it,j.rosterName)
                it=it+1
        elif i==fbTool.leagueLists[-1]:
            print 'error: league not registered'
    raw_input('Press return to continue...')

def printPlayers():
    leagueName=getLeagueName()
    teamName=getTeamName()
    lfound=False
    tfound=True
    for i in fbTool.leagueLists:
        if i.leagueName == leagueName:
            lfound=True
            for j in i.rosters:
                if j.rosterName == teamName:
                    tfound=True
                    print 'Players on team %s:'%teamName
                    if j.players:
                        print 'PlayerID       First Name       Last Name           NFLTeam    Position'
                    else:
                        print 'Team is empty'
                    for k in j.players:
                        print '{:14s} {:16s} {:19s} {:10s} {:9s} '.format(str(k.player_id),k.firstName,k.lastName,k.team,k.position)
                    print '%s uses %s\'s defense' %(teamName,j.defense)
                elif j==i.rosters[-1] and not tfound: 
                    print 'Team %s not found'%teamName

        elif i==fbTool.leagueLists[-1] and not lfound:
            print 'League %s not found' %leagueName
    raw_input('Press return to continue...').strip()


def printPts():
    leagueName=getLeagueName()
    teamName=getTeamName()
    weekNum=int(raw_input('Please enter a week number: '))
    points=[]
    it=0
    plfound=False
    tfound=False
    year=int(raw_input('Enter a year (2009-2015):').rstrip())
    for i in fbTool.leagueLists:
        if i.leagueName == leagueName:
            lfound=True
            for j in i.rosters:
                if j.rosterName == teamName:
                    tfound=True
                    if j.players:
                        print 'Calculating points for %s on week %d...'%(teamName,weekNum)
                        for k in j.players:
                            if k.position != 'LE' and k.position != 'RE' and k.position != 'OLB' and k.position != 'CB' and k.position != 'MLB' and k.position != 'DT' and k.position != 'DB' and k.position != 'DE' and k.position != 'FS' and k.position != 'SS':
                                playersName=k.firstName+' '+k.lastName
                                plyToApp = nflgame.find(playersName,k.team)[0]
                                if k.position == 'K':
                                    points.append(fpKicker.kickerScore(plyToApp,year,weekNum))
                                else:
                                    points.append(fpPlayer.fantasyPoints(plyToApp,year,weekNum))
                        print 'PlayerID       First Name       Last Name           NFLTeam    Points'
                        for k in j.players:
                            if k.position != 'LE' and k.position != 'RE' and k.position != 'OLB' and k.position != 'CB' and k.position != 'MLB' and k.position != 'DT' and k.position != 'DB' and k.position != 'DE' and k.position != 'FS' and k.position != 'SS':
                                print '{:14s} {:16s} {:19s} {:10s} {:9f} '.format(str(k.player_id),k.firstName,k.lastName,k.team,points[it])
                                it = it+1
                        dpoints=0
                        for l in j.defense:
                            dpoints = dpoints+fpDefense.fpDefense(l,year,weekNum)
                        p=sum(points)
                        print 'total offensive points: %f'%p
                        print 'total defensive points: %f'%dpoints
                        print 'total points: %f'%(p+dpoints)
                    else:
                        print 'Team is empty'
                elif j==i.rosters[-1] and not tfound: 
                    print 'Team %s not found'%teamName
        elif i==fbTool.leagueLists[-1] and not lfound:
            print 'League %s not found' %leagueName
    raw_input('Press return to continue...').strip()

def saveFileUI():
    fn=getFileName(1)
    if not fbTool.writeClassToFile(fn):
        print 'Successfully output to file %s' % fn
        raw_input('Press return to continue...').strip()
    else:
        print 'File output failed.'
        raw_input('Press return to continue...').strip()

def loadFileUI():
    fn=getFileName(0)
    if not fbTool.readClassFromFile(fn):
        print 'Successfully read from file %s' % fn
        raw_input('Press return to continue...').strip()
    else:
        print 'File input failed.'
        raw_input('Press return to continue...').strip()

def main():
    choice = 0
    if _platform =="linux" or _platform=="linux2":
        os.system('clear')
    elif _platform == "win32":
        os.system('cls')
    else:
        print 'This program doesn\'t run on mac...'
        exit()
    print '==================================================================='
    print 'Fantasy Football Team Tool - CLI interface'
    print '==================================================================='
    print 'Please choose one of the following options:'
    print '1 - Add league to be tracked'
    print '2 - Add team to an existing league'
    print '3 - Add a player to an existing team\'s roster'
    print '4 - Print a list of registered leagues'
    print '5 - Print a list of teams registered to a given league'
    print '6 - Print a list of a team\'s current roster'
    print '7 - Print fantasy points for teams in a league for given week'
    print '8 - Write current league structures to a file'
    print '9 - Read league structures from a file'
    print '10 - Print a specific player\'s points'
    print '11 - Exit the program'
    choice=raw_input('Please enter an option: ').strip()
    if choice == '\n':
        choice = '0'
    
    while choice != '11':
        if choice in ['1','2','3','4','5','6','7','8','9','10','11']:
            if choice=='1':
                addLeagueUI()
            if choice=='2':
                addRosterUI()
            if choice=='3':
                addPlayerUI()
            if choice=='4':
                printLeagues()
            if choice=='5':
                printTeams()
            if choice=='6':
                printPlayers()
            if choice=='7':
                printPts()
            if choice=='8':
                saveFileUI()
            if choice=='9':
                loadFileUI()
            if choice=='10':
                playerPointsUI()
            if choice=='11':
                print 'exiting...\n'
 
        else:
            print 'ERROR: Invalid input\n'
            raw_input('Press return to continue...').strip()

        if _platform =="linux" or _platform=="linux2":
            os.system('clear')
        elif _platform == "win32":
            os.system('cls')

        print '==================================================================='
        print 'Fantasy Football Team Tool - CLI interface'
        print '==================================================================='
        print 'Please choose one of the following options:'
        print '1 - Add league to be tracked'
        print '2 - Add team to an existing league'
        print '3 - Add a player to an existing team\'s roster'
        print '4 - Print a list of registered leagues'
        print '5 - Print a list of teams registered to a given league'
        print '6 - Print a list of a team\'s current roster'
        print '7 - Print fantasy points for teams in a league for given week'
        print '8 - Write current league structures to a file'
        print '9 - Read league structures from a file'
        print '10 - Print a specific player\'s points'
        print '11 - Exit the program'
        choice = raw_input('Please enter an option: ').strip()
    
        if choice == '\n':
            choice = '0'
 
main()
