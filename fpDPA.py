import nflgame

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


print defensePA(2015,7,'NE')


