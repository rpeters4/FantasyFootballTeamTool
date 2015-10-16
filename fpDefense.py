import nflgame

def defensePoints(s, w, t):
    games = nflgame.games_gen(s, w, t, t)
    plays = nflgame.combine_plays(games)
    dfrectd=0
    dffum=0
    dsk=0
    dint=0
    dinttd=0
    punttd=0
    kicktd=0
    dsafe=0
    for p in plays.filter(team__ne=t):
        if p.defense_sk > 0:  #checked
            dsk += 1
        if p.defense_ffum > 0: #checked
            dffum += 1
        if p.defense_int > 0:
            dint += 1
        if p.defense_int_tds > 0:
            dinttd += 1
        if p.defense_frec_tds > 0:
            dfrectd += 1
        if p.defense_safe > 0:
            dsafe += 1
        if p.puntret_tds > 0:
            punttd += 1
        if p.kickret_tds > 0:
            kicktd += 1
    #endfor

    return dsk + 2*dffum + 2*dint + 6*dinttd + 6*dfrectd + 2*dsafe + 6*punttd + 6*kicktd

#TESTING XDXD
print defensePoints(2015, None, "NE")             #Get all sacks earned by Baltimore defense in all of 2015
print defensePoints(2015, 1, "NE")                #Calc all the fantasy points for week 1
print defensePoints(2015, 2, "NE")                #Calc all the fantasy points for week 2
print defensePoints(2015, [1,2], "NE")            #calc total points for week 1 and week 2
