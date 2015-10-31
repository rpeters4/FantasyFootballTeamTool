week4 = ['TEN', 'NE', 4]
week5 = ['CAR', 'MIA', 'MIN', 'NYJ', 5]
week6 = ['DAL', 'OAK', 'STL', 'TN', 6]
week7 = ['CHI', 'CIN', 'DEN', 'GB', 7]
week8 = ['BUF', 'JAC', 'PHI', 'WAS', 8]
week9 = ['ARI', 'BAL', 'DET', 'HOU', 'KC', 'SEA', 9]
week10 = ['ATL', 'IND', 'SD', 'SF', 10]
week11 = ['CLE', 'NO', 'NYG', 'PIT', 11]
byeWeeks = [week4, week5, week6, week7, week8, week9, week10, week11]

def byeCheck(chkPlayer):
    if nfl.standard_team(chkPlayer.team) in week4: 
        return 4
    if nfl.standard_team(chkPlayer.team) in week5: 
        return 5
    if nfl.standard_team(chkPlayer.team) in week6: 
        return 6
    if nfl.standard_team(chkPlayer.team) in week7: 
        return 7
    if nfl.standard_team(chkPlayer.team) in week8: 
        return 8
    if nfl.standard_team(chkPlayer.team) in week9: 
        return 9
    if nfl.standard_team(chkPlayer.team) in week10: 
        return 10
    if nfl.standard_team(chkPlayer.team) in week11: 
        return 11

