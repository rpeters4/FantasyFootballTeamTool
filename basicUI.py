import fbTool
import os
from sys import platform as _platform

def printLeagues():
    if fbTool.leagueLists:
        it=1
        print 'League# LeagueName'
        for i in fbTool.leagueLists:
            print '%d       %s' %(it,i.leagueName)
            it=it+1
    raw_input('Press return to continue...').rstrip()

def getLeagueName():
    return raw_input('Please enter league name: ').rstrip()

def printTeams(leagueName):
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

def getTeamName():
    return raw_input('Please enter team name: ').rstrip()

def printPlayers(leagueName,teamName):
    it=1
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
                elif j==i.rosters[-1] and not tfound: 
                    print 'Team %s not found'%teamName

        elif i==fbTool.leagueLists[-1] and not lfound:
            print 'League %s not found' %leagueName
    raw_input('Press return to continue...').rstrip()


def getFileName(isOut):
    if isOut:
        return raw_input('please input output filename: ').rstrip()
    else:
        return raw_input('please input input filename: ').rstrip()

def printPts(leagueName,teamName,weekNum):
    print 'this will do things(eventually...)!  wowie zowie!\n'

def main():
    choice = 0
    if _platform =="linux" or _platform=="linux2":
        os.system('clear')
    elif _platform == "win32":
        os.system('cls')
    print 'Fantasy Football Team Tool - CLI interface\n'
    print 'Please choose one of the following options:\n1 - Add league to be tracked\n2 - Add team to an existing league\n3 - Add a player to an existing team\'s roster\n4 - Print a list of registered leagues\n5 - Print a list of teams registered to a given league\n6 - Print a list of a team\'s current roster\n7 - Print fantasy points for teams in a league for given week\n8 - Write current league structures to a file\n9 - Read league structures from a file\n10 - Exit the program\n'
    choice=raw_input('Please enter an option: ').rstrip()
    if choice == '\n':
        choice = '0'
    
    while choice != '10':
        if choice in ['1','2','3','4','5','6','7','8','9','10']:
            if choice=='1':
                ln=getLeagueName()
                if not fbTool.addLeague(ln):
                    print 'Successfully added league %s!' % ln
                    raw_input('Press return to continue...').rstrip()
                else:
                    print 'Failed to add league...'
            if choice=='2':
                ln=getLeagueName()
                tn=getTeamName()
                if not fbTool.addRoster(ln,tn):
                    print 'Succesfully added roster %s!' % tn
                    raw_input('Press return to continue...').rstrip()
                else:
                    print 'Failed to add team...'
            if choice=='3':
                ln=getLeagueName()
                tn=getTeamName()
                plName=raw_input('Please input the desired player to add\'s name: ')
                plTeam=raw_input('Please input the desired player\'s NFL team: ')
                if not fbTool.addPlayer(ln,tn,plName,plTeam):
                    print 'Succesfully added %s to %s from league %s' % (plName,tn,ln)
                    raw_input('Press return to continue...').rstrip()
                else:
                    print 'Failed to add player...'
                    raw_input('Press return to continue...').rstrip()
            if choice=='4':
                printLeagues()
            if choice=='5':
                ln=getLeagueName()
                printTeams(ln)
            if choice=='6':
                ln=getLeagueName()
                tn=getTeamName()
                printPlayers(ln,tn)
            if choice=='7':
                ln=getLeagueName()
                tn=getTeamName()
                wn=raw_input('Please enter a week number: ')
                printPts(ln,tn,wn)
            if choice=='8':
                fn=getFileName(1)
                if not fbTool.writeClassToFile(fn):
                    print 'Successfully output to file %s' % fn
                    raw_input('Press return to continue...').rstrip()
                else:
                    raw_input('Press return to continue...').rstrip()
            if choice=='9':
                fn=getFileName(0)
                if not fbTool.readClassFromFile(fn):
                    print 'Successfully read from file %s' % fn
                    raw_input('Press return to continue...').rstrip()
                else:
                    raw_input('Press return to continue...').rstrip()
            if choice=='10':
                print 'exiting...\n'
 
        else:
            print 'ERROR: Invalid input\n'
            raw_input('Press return to continue...').rstrip()

        if _platform =="linux" or _platform=="linux2":
            os.system('clear')
        elif _platform == "win32":
            os.system('cls')               
        print 'Please choose one of the following options:\n1 - Add league to be tracked\n2 - Add team to an existing league\n3 - Add a player to an existing team\'s roster\n4 - Print a list of registered leagues\n5 - Print a list of teams registered to a given league\n6 - Print a list of a team\'s current roster\n7 - Print fantasy points for teams in a league for given week\n8 - Write current league structures to a file\n9 - Read league structures from a file\n10 - Exit the program\n'
        choice=raw_input('Please enter an option: ')
        if choice == '\n':
            choice = '0'
 
main()
