


import requests
import re

def call_api(uri, result_key):
    json = {}
    try:
        json = requests.get(uri, headers = { 'X-Auth-Token': 'c52b7825851b4357af3e06c1888152f0' }).json()
        return json[result_key]
    except:
        print(json)
        return None


teams = call_api('http://api.football-data.org/v1/soccerseasons/439/teams', 'teams')


for team in teams:
    players = call_api(team['_links']['players']['href'], 'players')
    fixtures = call_api(team['_links']['fixtures']['href'], 'fixtures')
    wins = 0
    losts = 0
    for f in fixtures:
        if team['name'] == f['homeTeamName']:
            wins += f['result']['goalsHomeTeam'] if f['result']['goalsHomeTeam'] else 0
        else:
            wins += f['result']['goalsAwayTeam'] if f['result']['goalsAwayTeam'] else 0
    for f in fixtures:
        if team['name'] != f['homeTeamName']:
            losts += f['result']['goalsHomeTeam'] if f['result']['goalsHomeTeam'] else 0
        else:
            losts += f['result']['goalsAwayTeam'] if f['result']['goalsAwayTeam'] else 0
    cost = 0.0
    if team['squadMarketValue']:
        cost = float(re.sub("\D", "", team['squadMarketValue']))
    print('Team "{}", {} players, {} wins, {} losts, {} cost'.format(team['name'], len(players), wins, losts, cost))
    team['players'] = players
    team['wins'] = wins

