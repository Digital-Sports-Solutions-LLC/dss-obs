import tkinter as tk
from tkinter import ttk
import requests

def fetch_events():
    url = "http://3.137.207.81:8000/event/api/"
    response = requests.get(url)
    events = response.json()

    event_names_to_data.clear()  # Clear the dictionary before updating
    for event in events:
        event_name = event['name']
        event_id = event['event_ID']
        event_names_to_data[event_name] = event_id

    event_choices = [f"{event_name} ({event_id})" for event_name, event_id in event_names_to_data.items()]
    event_dropdown['values'] = event_choices

def fetch_matches(event_id):
    print(event_id)
    url = f"http://3.137.207.81:8000/match/api/?event_id={event_id}"
    response = requests.get(url)
    matches = response.json()

    match_choices = []
    for match in matches:
        if event_id == match['court_event']['event']['event_ID']:
            continue
        match_number = match['match_ID']
        court_number = match['court_event']['courtNumber']
        team1_acronym = match['team1']['teamAcronym']
        team2_acronym = match['team2']['teamAcronym']
        match_choices.append(f"Court: {court_number} - {team1_acronym} vs {team2_acronym} ({match_number})")

    match_dropdown['values'] = match_choices

def on_event_change(event):
    selected_event = event_dropdown.get()
    # Extract event ID from the selected event string
    selected_event_id = selected_event.split('(')[-1].split(')')[0]
    fetch_matches(selected_event_id)


# Create the main window
root = tk.Tk()
root.title("Dodgeball Match Selector")
root.geometry("600x400")  # Adjust the window size as needed

# Create event dropdown
event_dropdown_label = ttk.Label(root, text="Select Event:")
event_dropdown_label.pack(pady=10)
event_names_to_data = {}  # Store event data for later use
event_dropdown = ttk.Combobox(root, state="readonly", width=40)  # Adjust width
event_dropdown.pack(pady=10)
event_dropdown.bind("<<ComboboxSelected>>", on_event_change)

# Create match dropdown
match_dropdown_label = ttk.Label(root, text="Select Match:")
match_dropdown_label.pack(pady=10)
match_dropdown = ttk.Combobox(root, state="readonly", width=40)  # Adjust width
match_dropdown.pack(pady=10)

# Fetch and populate events on launch
fetch_events()

# Start the main loop
root.mainloop()
