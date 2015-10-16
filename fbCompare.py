
import nflgame
import fptest
import byeWeekLists

def playerCompare():
    player1 = raw_input("Enter player: \n")
    year1 = int(raw_input("Enter year: \n"))
    w1 = raw_input("Enter week(s): \n")
    weeks1 = map(int, w1.split())
    points1 = fptest.fantasypoints(player1, year1, weeks1)
    weeksPlayed1 = 0
    for i in weeks1:
        if str(i).isdigit():
            weeksPlayed1 = weeksPlayed1 + 1
    for w in byeWeekLists.byeWeeks:
        for t in w:
            curWeek = nflgame.live.current_year_and_week()[1]
            if w[-1] < curWeek and nflgame.find(player1, team=None)[0].team == t:
                weeksPlayed1 = weeksPlayed1 - 1
                break
    average1 = points1 / weeksPlayed1
    print average1
    player2 = raw_input("Enter player: \n")
    year2 = int(raw_input("Enter year: \n"))
    w2 = raw_input("Enter week(s): \n")
    weeks2 = map(int, w2.split())
    points2 = fptest.fantasypoints(player2, year2, weeks2)
    weeksPlayed2 = 0
    for i in weeks2:
        if str(i).isdigit():
            weeksPlayed2 = weeksPlayed2 + 1
    for w in byeWeekLists.byeWeeks:
        for t in w:
            curWeek = nflgame.live.current_year_and_week()[1]
            if w[-1] < curWeek and nflgame.find(player2, team=None)[0].team == t:
                weeksPlayed2 = weeksPlayed2 - 1
                break
    average2 = points2 / weeksPlayed2
    print average2
    
