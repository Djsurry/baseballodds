import os, requests, json

API_KEY = os.environ['ODDS_KEY']

def get_games():
  return [{'home_team': x['home_team'], 'away_team': x['away_team'], 'id': x['id']} for x in json.loads(requests.get(f'https://api.the-odds-api.com/v4/sports/baseball_mlb/odds/?apiKey={API_KEY}&regions=us&markers=h2h&oddsFormat=decimal').text)]

def get_odds(event, markets):
  return [x for x in json.loads(requests.get(f'https://api.the-odds-api.com/v4/sports/baseball_mlb/events/{event}/odds?apiKey={API_KEY}&regions=us&markets={markets}&oddsFormat=decimal').text)['bookmakers'] if x['key'] == 'fanduel'][0]['markets']

# batter_home_runs
# batter_hits	
print(get_odds(get_games()[0]['id'], "batter_home_runs"))