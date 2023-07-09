
from View.EventsScreen.events_screen import EventsScreenView


class EventsScreenController:
    """
    The `EventsScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.events_screen.EventsScreenModel
        self.view = EventsScreenView(controller=self, model=self.model)

    def on_save_event(self, event_data):
        self.model.save_event(event_data)
        self.go_back()

    def go_back(self):
        self.view.manager_screens.current = 'calendar screen'
        self.view.manager_screens.transition.direction = 'right'
        self.view.clear_fields()

    def get_view(self) -> EventsScreenView:
        return self.view
