from Model.base_model import BaseScreenModel
import json


class EventsScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.events_screen.EventsScreen.EventsScreenView` class.
    """
    def save_event(self, event_data):
        try:
            with open('events.json', 'r+') as file:
                try:
                    events = json.load(file)
                except json.JSONDecodeError:
                    events = []
                
                events.append(event_data)
                
                file.seek(0)
                json.dump(events, file, indent=4)
                file.truncate()
        except FileNotFoundError:
            with open('events.json', 'w') as file:
                events = [event_data]
                json.dump(events, file, indent=4)
        
        