import nflgame
#calculates stats of kicker but does not add bonus for kickers at distances 40+ or 50+
def kickerScore(playerName, year, week):
    lf = player
    statistics = lf.stats(year, week)
    #print statistics.stats
    if 'kicking_xpmissed' in statistics.stats:
        xpMissed = statistics.stats['kicking_xpmissed']
    #print statistics.stats['kicking_xpmissed']
    if 'kicking_xpmade' in statistics.stats:
    xpMade = statistics.stats['kicking_xpmade']
    #print statistics.stats['kicking_xpmade']
    if 'kicking_fgm' in statistics.stats:
        fgMade = statistics.stats['kicking_fgm']
    #print statistics.stats['kicking_fgm']
    if 'kicking_fgm' in statistics.stats and 'kicking_fga' in statistics.stats:
        fgMissed = statistics.stats['kicking_fga'] - statistics.stats['kicking_fgm']
    #print statistics.stats['kicking_fga'] - statistics.stats['kicking_fgm']
    points = xpMade*1 - xpMissed*1 + fgMade*3 - fgMissed*3
    print points
