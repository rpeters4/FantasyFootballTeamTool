#
import nflgame

def kickerScore(playerName, year, week):
    if nflgame.find(playerName, team=None):
        playa = nflgame.find(playerName, team=None)[0]
        games = nflgame.games(year, week)
        #games = playa.plays(year, week).players().playerid(playa.playerid)
        plays = nflgame.combine_plays(games)
        all_made_fgs = plays.filter(kicking_fgm=True)
        for p in all_made_fgs:
                if p.players.playerid(playa.playerid):
                    print p.kicking_fgm_yds
##        points = 0
##        m = playa.stats(year, week)
##        z = playa.plays(year, week)
##        print m
##        if 'kicking_fgm' in m.stats:
##            print "hi"
##            points = 1*m.stats['kicking_fgm_yds']
##            print points
    else:
        print "Player not found."
