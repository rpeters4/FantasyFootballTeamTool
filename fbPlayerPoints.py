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
    else:
        return float('inf')
    for i in playerInfo[2]:
        if str(i).isdigit():
            weeksPlayed = weeksPlayed + 1
    for w in byeWeekLists.byeWeeks:
        for t in w:
            curWeek = nflgame.live.current_year_and_week()[1]
            if w[-1] < curWeek and nflgame.find(playerInfo[0], team=None)[0].team == t and w[-1] in playerInfo[2]:
                weeksPlayed1 = weeksPlayed1 - 1
                break
    average = points / weeksPlayed
    return average
    
