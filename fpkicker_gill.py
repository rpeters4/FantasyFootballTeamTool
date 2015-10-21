import nflgame

def kickerScore(playerName, year, week):
    for player in nflgame.find(playerName, team = None):
        if player is not None:
            print player.plays(year, week)
        else:
            print "Player does not exist"
