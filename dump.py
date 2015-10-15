import nflgame

def dump(team=None):
	players=[]
	for player in nflgame.players.itervalues():
		if team is None or nflgameteam.lower()==nflgame.player.team.lower():
			players.append(str(player.name))
	return players


print dump()


