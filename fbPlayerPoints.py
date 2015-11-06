import nflgame
import fpPlayer
import fpKicker
import fpDefense
import byeWeekLists

def playerPoints(playerInfo):
    weeksPlayed = 0
    playerFound = nflgame.find(playerInfo[0], team = None)
    if playerFound != []:
        if playerFound[0].position == "K":
            points = fpKicker.kickerScore(playerFound[0], playerInfo[1], playerInfo[2])
        else:
            points = fpPlayer.fantasyPoints(playerFound[0], playerInfo[1], playerInfo[2])
        for i in playerInfo[2]:
            if str(i).isdigit():
                weeksPlayed = weeksPlayed + 1
        curWeek = nflgame.live.current_year_and_week()[1]
        if len(playerInfo[2]) == 1 and playerInfo[2][0] == byeWeekLists.byeCheckPlayer(playerFound[0]):
            return float(18742)
        if byeWeekLists.byeCheckPlayer(playerFound[0]) <= curWeek and byeWeekLists.byeCheckPlayer(playerFound[0]) in playerInfo[2]:
            weeksPlayed = weeksPlayed - 1
        average = points / weeksPlayed
        return average
    elif playerInfo[0] != None:
        team = nflgame.standard_team(playerInfo[0])
        if team == None:
            return float('inf')
        playerInfo[0] = team
        points = fpDefense.fpDefense(playerInfo[0], playerInfo[1], playerInfo[2])
        for i in playerInfo[2]:
            if str(i).isdigit():
                weeksPlayed = weeksPlayed + 1
        curWeek = nflgame.live.current_year_and_week()[1]
        if len(playerInfo[2]) == 1 and playerInfo[2][0] == byeWeekLists.byeCheckTeam(playerInfo[0]):
            return float(18742)
        if byeWeekLists.byeCheckTeam(playerInfo[0]) <= curWeek and byeWeekLists.byeCheckTeam(playerInfo[0]) in playerInfo[2]:
            weeksPlayed = weeksPlayed - 1
        return points / weeksPlayed
    else:
        return float('inf')
    
