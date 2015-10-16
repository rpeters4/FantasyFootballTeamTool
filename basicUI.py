import fbTool
import os
from sys import platform as _platform

def printLeagues():
    if fbTool.leagueLists:
        it=1
        print 'League# |LeagueName'
        for i in fbTool.leagueLists:
            print '%d      | %s' %(it,i.leagueName)
            it=it+1
    raw_input('Press return to continue...')

def getLeagueName():
    return raw_input('Please enter league name: ')

def printTeams(leagueName):
    it=1
    print 'Teams in league %s:'%leagueName
    for i in fbTool.leagueLists:
        if i.leagueName==leagueName:
            print 'Team# | Team Name'
            for j in i.rosters:
                print '%d   |%s'%(it,j.rosterName)
                it=it+1
        else:
            print 'error: league not registered'
    raw_input('Press return to continue...')

def getTeamName():
    return raw_input('Please enter team name: ')

def printPlayers(leagueName,teamName):
    it=1
    print 'Players on team %s:'%teamName
    print 'PlayerID  |First Name    |Last Name    |NFLTeam    |Position'
    lfound=False
    tfound=True
    for i in fbTool.leagueLists:
        if i.leagueName == leagueName:
            lfound=True
            for j in i.rosters:
                if j.rosterName == teamName:
                    tfound=True
                    for k in j.players:
                        print '%s   %s   %s   %s   %s'%(str(k.player_id),k.firstName,k.lastName,k.team,k.position)
                elif j==i.rosters[-1] and not tfound:
                    print 'Team %s not found'%teamName

        elif i==fbTool.leagueLists[-1] and not lfound:
            print 'League %s not found' %leagueName
    raw_input('Press return to continue...')


def getFileName(isOut):
    if isOut:
        return raw_input('please input output filename: ')
    else:
        return raw_input('please input input filename: ')

def printPts(leagueName,teamName,weekNum):
    print 'this will do things(eventually...)!  wowie zowie!\n'

def main():
    choice = 0
    if _platform =="linux" or _platform=="linux2":
        os.system('clear')
    elif _platform == "win32":
        os.system('cls')
    print 'Fantasy Football Team Tool - CLI interface\n'
    print 'Please choose one of the following options:\n1 - Add league to be tracked\n2 - Add team to an existing league\n3 - Add player to existing team\'s roster\n4 - Print list of leagues\n5 - Print list of teams registered to a given league\n6 - Print a given team in a given league\'s current roster\n7 - Print fantasy points for given player in a given week\n8 - Write current league structures to a file\n9 - Read league structures from a file\n10 - Exit the program\n'
    choice=raw_input('Please enter an option: ')
    if choice != '\n':
        choice = int (choice)
    else:
        choice = 0
    
    while choice != 10:
        if choice in [1,2,3,4,5,6,7,8,9,10]:
            if choice==1:
                ln=getLeagueName()
                fbTool.addLeague(ln)
            if choice==2:
                ln=getLeagueName()
                tn=getTeamName()
                fbTool.addRoster(ln,tn)
            if choice==3:
                ln=getLeagueName()
                tn=getTeamName()
                plName=raw_input('Please input the desired player to add\'s name: ')
                plTeam=raw_input('Please input the desired player\'s NFL team: ')
                fbTool.addPlayer(ln,tn,plName,plTeam)
            if choice==4:
                printLeagues()
            if choice==5:
                ln=getLeagueName()
                printTeams(ln)
            if choice==6:
                ln=getLeagueName()
                tn=getTeamName()
                printPlayers(ln,tn)
            if choice==7:
                ln=getLeagueName()
                tn=getTeamName()
                wn=raw_input('Please enter a week number: ')
                printPts(ln,tn,wn)
            if choice==8:
                fn=getFileName(1)
                fbTool.writeClassToFile(fn)
            if choice==9:
                fn=getFileName(0)
                fbTool.readClassFromFile(fn)
            if choice==10:
                print 'exiting...\n'
 
            if _platform =="linux" or _platform=="linux2":
                os.system('clear')
            elif _platform == "win32":
                os.system('cls')               
            print 'Please choose one of the following options:\n1 - Add league to be tracked\n2 - Add team to an existing league\n3 - Add player to existing team\'s roster\n4 - Print list of leagues\n5 - Print list of teams registered to a given league\n6 - Print a given team in a given league\'s current roster\n7 - Print fantasy points for given player in a given week\n8 - Write current league structures to a file\n9 - Read league structures from a file\n10 - Exit the program\n'
            choice=raw_input('Please enter an option: ')
            if choice != '\n':
                choice = int (choice)
            else:
                choice = 0
        else:
            print 'ERROR: Invalid input\n'
main()
