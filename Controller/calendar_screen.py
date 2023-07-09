
from View.CalendarScreen.calendar_screen import CalendarScreenView


class CalendarScreenController:
    """
    The `CalendarScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.calendar_screen.CalendarScreenModel
        self.view = CalendarScreenView(controller=self, model=self.model)

    def get_view(self) -> CalendarScreenView:
        return self.view
