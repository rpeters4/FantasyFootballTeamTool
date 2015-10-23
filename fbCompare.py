import nflgame
import fpPlayer
import fpKicker
import byeWeekLists

def playerCompare():
    player1 = raw_input("Enter player: \n").strip()
    year1 = int(raw_input("Enter year: \n"))
    w1 = raw_input("Enter week(s): \n").strip()
    weeks1 = map(int, w1.split())
    weeksPlayed1 = 0
    player2 = raw_input("Enter player: \n").strip()
    year2 = int(raw_input("Enter year: \n"))
    w2 = raw_input("Enter week(s): \n").strip()
    weeks2 = map(int, w2.split())
    weeksPlayed2 = 0
    player1Found = nflgame.find(player1, team = None)
    player2Found = nflgame.find(player2, team = None)
    if player1Found != []:
        if player1Found[0].position == "K":
            points1 = fpKicker.kickerScore(player1Found[0], year1, weeks1)
        else:
            points1 = fpPlayer.fantasypoints(player1Found[0], year1, weeks1)
    else:
        print "First player entered was not found\n"
        return 0
    if player2Found != []:
        if player2Found[0].position == "K":
            points2 = fpKicker.kickerScore(player2Found[0], year1, weeks1)
        else:
            points2 = fpPlayer.fantasypoints(player2Found[0], year2, weeks2)
    else:
        print "Second player entered was not found\n"
        return 0
    for i in weeks1:
        if str(i).isdigit():
            weeksPlayed1 = weeksPlayed1 + 1
    for w in byeWeekLists.byeWeeks:
        for t in w:
            curWeek = nflgame.live.current_year_and_week()[1]
            if w[-1] < curWeek and nflgame.find(player1, team=None)[0].team == t and w[-1] in weeks1:
                weeksPlayed1 = weeksPlayed1 - 1
                break
    for i in weeks2:
        if str(i).isdigit():
            weeksPlayed2 = weeksPlayed2 + 1
    for w in byeWeekLists.byeWeeks:
        for t in w:
            curWeek = nflgame.live.current_year_and_week()[1]
            if w[-1] < curWeek and nflgame.find(player2, team=None)[0].team == t and w[-1] in weeks2:
                weeksPlayed2 = weeksPlayed2 - 1
                break
    average1 = points1 / weeksPlayed1
    average2 = points2 / weeksPlayed2
    print '%s\'s average is %.2f' % (player1, average1)
    print '%s\'s average is %.2f' % (player2, average2)
    return 0
    
