
from View.EventListScreen.event_list_screen import EventListScreenView


class EventListScreenController:
    """
    The `EventListScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.event_list_screen.EventListScreenModel
        self.view = EventListScreenView(controller=self, model=self.model)
   
    def go_back(self):
        self.view.manager_screens.current = 'calendar screen'
        self.view.manager_screens.transition.direction = 'right'

    def load_events(self):
        self.model.load_events()

    def get_events(self):
        return self.model.get_events()

    def delete_event(self, event):
        self.model.delete_event(event)
        
    
    def get_view(self) -> EventListScreenView:
        return self.view
