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

def defensePA(s,w,t):
# We want the games Buffalo played in 2013
# Get the games Buffalo played in the 2013 Regular Season
    games = nflgame.games_gen(s, w , home=t, away=t, kind= 'REG')
    pa = 0.0;

    # Iterate through the games
    for g in games:
        # If Buffalo was home, add the score_home to the points for list and the score_away to the points against list
        if g.home == t:
            print g.score_home
            print g.stats_home[1]
            print g.score_away
            if g.score_away == 0.0:
                pa = 5.0
            if g.score_away > 0.0 and g.score_away <=6.0:
                pa = 4.0
            if g.score_away > 6.0 and g.score_away <=13.0:
                pa = 3.0
            if g.score_away > 13.0 and g.score_away <=17.0:
                pa = 1.0
            if g.score_away > 17.0 and g.score_away <=27.0:
                pa = 0.0
            if g.score_away > 27.0 and g.score_away <=34.0:
                pa = -1.0
            if g.score_away > 34.0 and g.score_away <=45.0:
                pa = -3.0
            if g.score_away > 45.0:
                pa = -5.0
            # If Buffalo was away, add the score_away to the points for list and the score_home to the points against list
        else:
            print g.score_away
            print g.stats_away[1]
            print g.score_home
            if g.score_home == 0.0:
                pa = 5.0
            if g.score_home > 0.0 and g.score_home <=6.0:
                pa = 4.0
            if g.score_home > 6.0 and g.score_home <=13.0:
                pa = 3.0
            if g.score_home > 13.0 and g.score_home <=17.0:
                pa = 1.0
            if g.score_home > 17.0 and g.score_home <=27.0:
                pa = 0.0
            if g.score_home > 27.0 and g.score_home <=34.0:
                pa = -1.0
            if g.score_home > 34.0 and g.score_home <=45.0:
                pa = -3.0
            if g.score_home >45.0:
                pa = -5.0
            #endif
        return pa
        #endif
    #endfor  
#endDef


#TESTING XDXD
print defensePoints(2015, None, "NE")             #Get all sacks earned by Baltimore defense in all of 2015
print defensePoints(2015, 1, "NE")                #Calc all the fantasy points for week 1
print defensePoints(2015, 2, "NE")                #Calc all the fantasy points for week 2
print defensePoints(2015, [1,2], "NE")            #calc total points for week 1 and week 2


print defensePA(2015,7,'NE')
