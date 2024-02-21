import tkinter as tk
import re
from tkinter import ttk
from api import fetch_events, fetch_courts_at_event, fetch_matches_on_court
from obs import obs

def on_event_change(event):
    selected_event = event_dropdown.get()  # Corrected line
    # Extract event ID from the selected event string
    selected_event_id = re.search(r'\(ID: (\d+)\)', selected_event).group(1)
    courts = fetch_courts_at_event(selected_event_id)
    court_dropdown['values'] = courts
    
    # Clear the matches dropdown
    court_dropdown.set('')
    match_dropdown.set('')
    
def on_court_change(event):
    selected_court = court_dropdown.get()  # Corrected line
    # Extract court ID from the selected court string
    selected_court_id = re.search(r'\(ID: (\d+)\)', selected_court).group(1)
    matches = fetch_matches_on_court(selected_court_id)
    match_dropdown['values'] = matches
    
    # Clear the matches dropdown
    match_dropdown.set('')
    
def confirm_selection():
    selected_match = match_dropdown.get()  # Corrected line
    # Extract match ID from the selected court string
    selected_match_id = re.search(r'\(ID: (\d+)\)', selected_match).group(1)
    obs(selected_match_id)

def selector():
    root = tk.Tk()
    root.title("Digital Sports Solutions - OBS Overlay")
    root.geometry("600x400")  # Adjust the window size as needed
    
    event_label = tk.Label(root, text="Select an event:")
    event_label.pack(pady=10)
    
    global event_dropdown  # Define as global
    event_dropdown = ttk.Combobox(root, values=fetch_events(), state="readonly", width=40)
    event_dropdown.pack()
    event_dropdown.bind("<<ComboboxSelected>>", on_event_change)
    
    court_label = tk.Label(root, text="Select a court:")
    court_label.pack(pady=10)
    
    global court_dropdown  # Define as global
    court_dropdown = ttk.Combobox(root, values=[], state="readonly", width=40)
    court_dropdown.pack()
    court_dropdown.bind("<<ComboboxSelected>>", on_court_change)
    
    match_label = tk.Label(root, text="Select a match:")
    match_label.pack(pady=10)
    
    global match_dropdown  # Define as global
    match_dropdown = ttk.Combobox(root, values=[], state="readonly", width=40)
    match_dropdown.pack()

    # Create a confirmation button
    confirm_button = ttk.Button(root, text="Confirm Selection", command=confirm_selection)
    confirm_button.pack(pady=10)
    
    root.mainloop()

selector()