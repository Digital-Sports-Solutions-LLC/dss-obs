import requests
from vars import server

def fetch(url):
    url = f"http://{server}/{url}"
    response = requests.get(url)
    data = response.json()
    return data


def fetch_events():
    events = fetch("event/api/")

    event_choices = []
    for event in events:
        event_name = event['name']
        event_id = event['event_ID']
        event_choices.append(f"{event_name} (ID: {event_id})")
    
    return event_choices   
    
def fetch_courts_at_event(event_id):
    courts = fetch("court/api/")
    
    court_choices = []
    for court in courts:
        if str(event_id) == str(court['event']['event_ID']):
            court_id = court['court_ID']
            court_number = court['courtNumber']
            court_choices.append(f"Court: {court_number} (ID: {court_id})")
            
    return court_choices

def fetch_matches_on_court(court_id):
    
    matches = fetch("match/api/")

    match_choices = []
    for match in matches:
        if str(court_id) == str(match['court_event']['court_ID']):
            match_id = match['match_ID']
            team1_acronym = match['team1']['teamAcronym']
            team2_acronym = match['team2']['teamAcronym']
            match_choices.append(f"{team1_acronym} vs {team2_acronym} (ID: {match_id})")
    
    return match_choices     
    