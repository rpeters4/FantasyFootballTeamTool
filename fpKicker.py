import nflgame
import fpPlayer
#calculates stats of kicker but does not add bonus for kickers at distances 40+ or 50+
def kickerScore(player, year, week):
    points = fpPlayer.fantasyPoints(player,year,week)
    lf = player
    statistics = lf.stats(year, week)
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
    points = points + xpMade*1 - xpMissed*1 + fgMade*3 - fgMissed*3
    games = nflgame.games(year, week)
    plays = nflgame.combine_plays(games)
    allMadeFGs = plays.filter(kicking_fgm = True)
    for p in allMadeFGs:
        if p.players.playerid(lf.playerid):
            yards = p.kicking_fgm_yds
            if yards >= 40:
                points = points + 1
            if yards >= 50:
                points = points + 1
    return points
