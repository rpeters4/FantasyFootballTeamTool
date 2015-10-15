# THIS file was made just to screw around with the the API.
# I've pulled through it and figured out where all the useful
# stats are held, just a matter of figuring out how to use them!
# (cue people who know things about fantasy football scoring...)
#
#
#
#

import nflgame

li=nflgame.find('tom brady',team=None)

l=li[0]

print l.first_name
print l.last_name
print l.team
print l.playerid
print l.name
print l.birthdate
print l.college
print l.height
print l.number
print l.position
print l.status
print l.uniform_number
print l.weight
print l.years_pro

k=l.plays(2015,1)

m=l.stats(2015,[1])

print m.guess_position
print m.home
print m.name
print m.player
print m.playerid
print m.stats
print m.tds
print m.team
print m.twopta
print m.twoptm
print m.twoptmissed

print m.stats['passing_att']


#
# This lists all of the players in the player dictionary:
# May be useful for adding players by a menu system? 
#

#def dump(team=None):
#	players=[]
#	for player in nflgame.players.itervalues():
#		if team is None or nflgameteam.lower()==nflgame.player.team.lower():
#			players.append(str(player.name))
#	return players


#print dump()


