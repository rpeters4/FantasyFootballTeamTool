#
import nflgame

<<<<<<< HEAD
p=raw_input("Enter player: \n")
y=int(raw_input("Enter year: \n"))
print y
w=raw_input("Enter week(s): \n")
#w = raw_input()
weeks = map(int, w.split())
#weeks=[int(w)]
#print weeks

def fantasypoints(p1, y1, w1):
    ppy=0
    pp2=0
    pint=0
    pptd=0
    prutd=0
    pruy=0
    prey=0
    pretd=0
    pfl=0
    pr2=0
    if nflgame.find(p1,team=None):
        lf=nflgame.find(p1, team=None)[0]
        k=lf.plays(y,w1)
        m=lf.stats(y,w1)
        print m
        if 'passing_yds' in m.stats:  
            ppy = .04*m.stats['passing_yds']
        if 'passing_twoptm' in m.stats:
            pp2 = 2*m.stats['passing_twoptm']
        if 'passing_ints' in m.stats:
            pint = -2*m.stats['passing_ints']
        if 'passing_tds' in m.stats:
            pptd = 4*m.stats['passing_tds']
        if 'rushing_tds' in m.stats:
            prutd = 6*m.stats['rushing_tds']
        if 'rushing_yds' in m.stats:
            pruy = .1*m.stats['rushing_yds']
        if 'receiving_yds' in m.stats:
            prey = .1*m.stats['receiving_yds']
        if 'receiving_tds' in m.stats:
            pretd = 6*m.stats['receiving_tds']
        if 'fumbles_lost' in m.stats:
            pfl = -2*m.stats['fumbles_lost']
        if 'rushing_twoptm' in m.stats:
            pr2 = 2*m.stats['rushing_twoptm']
        points = ppy+pp2+pint+pptd+prutd+pruy+prey+pretd+pfl+pr2
        print points
        return points
=======
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
>>>>>>> 95c2b8d1c48c70a96dd632b2d393fd7d1a06db6a
    else:
        print "Player not found."

##p=raw_input("Enter player: \n")
###li=nflgame.find(p, team=None)
###li=nflgame.find('tom brady',team=None)
##y=int(raw_input("Enter year: \n"))
##print y
##w=raw_input("Enter week(s): \n")
###w = raw_input()
##weeks = map(int, w.split())
###weeks=[int(w)]
##print weeks
###l=li[0]
##
###print l.first_name
###print l.last_name
###print l.team
###print l.playerid
###print l.name
###print l.birthdate
###print l.college
###print l.height
###print l.number
###print l.position
###print l.status
###print l.uniform_number
###print l.weight
###print l.years_pro
###k=l.plays(y,weeks)		#just picked week 3 to test things out
##
###m=l.stats(y,weeks)		
##
###print m.stats['passing_att']
##def fantasypoints(p1, y1, w1):
##    ppy=0
##    pp2=0
##    pint=0
##    pptd=0
##    prutd=0
##    pruy=0
##    prey=0
##    pretd=0
##    pfl=0
##    pr2=0
##    if nflgame.find(p1,team=None):
##        lf=nflgame.find(p1, team=None)[0]
##        k=lf.plays(y,w1)
##        m=lf.stats(y,w1)
##        print m
##        if 'passing_yds' in m.stats:  
##            ppy = .04*m.stats['passing_yds']
##        if 'passing_twoptm' in m.stats:
##            pp2 = 2*m.stats['passing_twoptm']
##        if 'passing_ints' in m.stats:
##            pint = -2*m.stats['passing_ints']
##        if 'passing_tds' in m.stats:
##            pptd = 4*m.stats['passing_tds']
##        if 'rushing_tds' in m.stats:
##            prutd = 6*m.stats['rushing_tds']
##        if 'rushing_yds' in m.stats:
##            pruy = .1*m.stats['rushing_yds']
##        if 'receiving_yds' in m.stats:
##            prey = .1*m.stats['receiving_yds']
##        if 'receiving_tds' in m.stats:
##            pretd = 6*m.stats['receiving_tds']
##        if 'fumbles_lost' in m.stats:
##            pfl = -2*m.stats['fumbles_lost']
##        if 'rushing_twoptm' in m.stats:
##            pr2 = 2*m.stats['rushing_twoptm']
##        points = ppy+pp2+pint+pptd+prutd+pruy+prey+pretd+pfl+pr2
##        print points
##    else:
##        print 'wtf mate, player not found!'
##
##fantasypoints(p,y,weeks)
