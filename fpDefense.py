import nflgame

def defensePlays(team, year, week, games):
    plays = nflgame.combine_plays(games)
    dfrectd=0
    dffum=0
    dsk=0
    dint=0
    dinttd=0
    punttd=0
    kicktd=0
    dsafe=0
    sack=0
    for p in plays.filter(team__ne=team):
        if p.defense_ffum > 0: 
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
        if p.defense_sk > 0:
            sack += 1
    return 2*dffum + 2*dint + 6*dinttd + 6*dfrectd + 2*dsafe + 6*punttd + 6*kicktd + 1*sack

def defensePA(team, year, week, games):
    pa = 0
    for g in games:  
        if g.home == team:
            if g.score_away == 0:
                pa = 5
            if g.score_away > 0 and g.score_away <=6:
                pa = 4
            if g.score_away > 6 and g.score_away <=13:
                pa = 3
            if g.score_away > 13 and g.score_away <=17:
                pa = 1
            if g.score_away > 17 and g.score_away <=27:
                pa = 0
            if g.score_away > 27 and g.score_away <=34:
                pa = -1
            if g.score_away > 34 and g.score_away <=45:
                pa = -3
            if g.score_away > 45:
                pa = -5
        else:
            if g.score_home == 0:
                pa = 5
            if g.score_home > 0 and g.score_home <=6:
                pa = 4
            if g.score_home > 6 and g.score_home <=13:
                pa = 3
            if g.score_home > 13 and g.score_home <=17:
                pa = 1
            if g.score_home > 17 and g.score_home <=27:
                pa = 0
            if g.score_home > 27 and g.score_home <=34:
                pa = -1
            if g.score_home > 34 and g.score_home <=45:
                pa = -3
            if g.score_home >45.0:
                pa = -5
    return pa

def defenseYA(team, year, week, games):
    ya = 0
    for g in games:
        if g.home == team:
            if g.stats_away[1] < 100:
                ya = 5
            if g.stats_away[1] >= 100 and g.stats_away[1] <= 199:
                ya = 3
            if g.stats_away[1] >= 200 and g.stats_away[1] <= 299:
                ya = 2
            if g.stats_away[1] >= 300 and g.stats_away[1] <= 349:
                ya = 0
            if g.stats_away[1] >= 350 and g.stats_away[1] <= 399:
                ya = -1
            if g.stats_away[1] >= 400 and g.stats_away[1] <= 449:
                ya = -3
            if g.stats_away[1] >= 450 and g.stats_away[1] <= 499:
                ya = -5
            if g.stats_away[1] >= 500 and g.stats_away[1] <= 549:
                ya = -6
            if g.stats_away[1] >= 550:
                ya = -7
        else:
            if g.stats_home[1] < 100:
                ya = 5
            if g.stats_home[1] >= 100 and g.stats_home[1] <= 199:
                ya = 3
            if g.stats_home[1] >= 200 and g.stats_home[1] <= 299:
                ya = 2
            if g.stats_home[1] >= 300 and g.stats_home[1] <= 349:
                ya = 0
            if g.stats_home[1] >= 350 and g.stats_home[1] <= 399:
                ya = -1
            if g.stats_home[1] >= 400 and g.stats_home[1] <= 449:
                ya = -3
            if g.stats_home[1] >= 450 and g.stats_home[1] <= 499:
                ya = -5
            if g.stats_home[1] >= 500 and g.stats_home[1] <= 549:
                ya = -6
            if g.stats_home[1] >= 550:
                ya = -7
    return ya

def fpDefense(team, year, week):
    games = nflgame.games_gen(year, week, team, team)
    points = 0
    points = points + defensePlays(team, year, week, games)
    points = points + defensePA(team, year, week, games)
    points = points + defenseYA(team, year, week, games)
    return points
