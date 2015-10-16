#
import nflgame

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
    else:
        print 'wtf mate, player not found!'

fantasypoints(p,y,weeks)
