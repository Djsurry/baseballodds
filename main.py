import os, requests, json

API_KEY = os.environ['ODDS_KEY']

def get_games():
  return [x['id'] for x in json.loads(requests.get(f'https://api.the-odds-api.com/v4/sports/baseball_mlb/odds/?apiKey={API_KEY}&regions=us&markers=h2h&oddsFormat=decimal').text)]

def get_odds(event, markets):
  return [x for x in json.loads(requests.get(f'https://api.the-odds-api.com/v4/sports/baseball_mlb/events/{event}/odds?apiKey={API_KEY}&regions=us&markets={markets}&oddsFormat=decimal').text)['bookmakers'] if x['key'] == 'fanduel'][0]['markets']

# batter_home_runs
# batter_hits	
print(get_odds(get_games()[0], "batter_home_runs"))