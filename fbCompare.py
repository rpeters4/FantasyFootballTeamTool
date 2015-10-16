import nflgame
import fptest

def playerCompare():
    player1 = raw_input("Enter player: \n")
    year1 = int(raw_input("Enter year: \n"))
    w1 = raw_input("Enter week(s): \n")
    weeks1 = map(int, w1.split())
    points1 = fptest.fantasypoints(player1, year1, weeks1)
    averageWeeks = 0
    for i in weeks1:
        if str(i).isdigit():
            averageWeeks = averageWeeks + 1
    average1 = points1 / averageWeeks
    player2 = raw_input("Enter player: \n")
    year2 = int(raw_input("Enter year: \n"))
    w2 = raw_input("Enter week(s): \n")
    weeks2 = map(int, w2.split())
    points2 = fptest.fantasypoints(player2, year2, weeks2)
    averageWeeks = 0
    for i in weeks2:
        if str(i).isdigit():
            averageWeeks = averageWeeks + 1
    average2 = points2 / averageWeeks
    
