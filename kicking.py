import nflgame

def kick(playerName, year, week):
	if nflgame.find(playerName, team=None):
		playa = nflgame.find(playerName, team=None) [0]
		games = nflgame.games(year, week)
		plays = nflgame.combine_plays(games)
		all_made_fgs = plays.filter(kicking_fgm=True)
		myList = []
		i = 1
		for p in all_made_fgs:
			if p.players.playerid(playa.playerid):
                                myList.append(p.kicking_fgm_yds)
                return myList
                                
