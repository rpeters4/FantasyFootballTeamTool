import fpPlayer
import fpDefense
import fpKicker
import fbTool
import nflgame
import time

def fpTeamPoints(roster):
    return fpDefense.fpDefense(roster.defense[0],2015,1)

fbTool.addLeague('t')
fbTool.addRoster('t','t0',['TEN'])
fbTool.addRoster('t','t1',['NE'])
fbTool.addRoster('t','t2',['CAR'])
fbTool.addRoster('t','t3',['MIA'])
fbTool.addRoster('t','t4',['MIN'])
fbTool.addRoster('t','t5',['NYJ'])
fbTool.addRoster('t','t6',['DAL'])
fbTool.addRoster('t','t7',['OAK'])
fbTool.addRoster('t','t8',['STL'])
fbTool.addRoster('t','t9',['TB'])  #doesn't exist?  it's on the byeweeklist tho...
fbTool.addRoster('t','t10',['CHI'])
fbTool.addRoster('t','t11',['CIN'])
fbTool.addRoster('t','t12',['DEN'])
fbTool.addRoster('t','t13',['GB'])
fbTool.addRoster('t','t14',['BUF'])
fbTool.addRoster('t','t15',['JAC'])
fbTool.addRoster('t','t16',['PHI'])
fbTool.addRoster('t','t17',['WAS'])
fbTool.addRoster('t','t18',['ARI'])
fbTool.addRoster('t','t19',['BAL'])
fbTool.addRoster('t','t20',['DET'])
fbTool.addRoster('t','t21',['HOU'])
fbTool.addRoster('t','t22',['KC'])
fbTool.addRoster('t','t23',['SEA'])
fbTool.addRoster('t','t24',['ATL'])
fbTool.addRoster('t','t25',['IND'])
fbTool.addRoster('t','t26',['SD'])
fbTool.addRoster('t','t27',['SF'])
fbTool.addRoster('t','t28',['CLE'])
fbTool.addRoster('t','t29',['NO'])
fbTool.addRoster('t','t30',['NYG'])
fbTool.addRoster('t','t31',['PIT'])
raw_input ('Press return to continue...')

start = time.time()
for i in fbTool.leagueLists[0].rosters:
    print 'defense = %s'% i.defense[0]
    print fpTeamPoints(i)
stop = time.time()

print 'Time to compute the defense scores for 32 teams: %s' %(stop-start)
