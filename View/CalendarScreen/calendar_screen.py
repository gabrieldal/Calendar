from View.base_screen import BaseScreenView
from libs.datepicker import CalendarWidget


class CalendarScreenView(BaseScreenView):

    def switch_screen(self, screen_name):
        if screen_name == 'events screen':
            self.manager_screens.transition.direction = 'left'
        elif screen_name == 'event list screen':
            self.manager_screens.transition.direction = 'left'
        elif screen_name == 'task list screen':
            self.manager_screens.transition.direction = 'right'
            
        self.manager_screens.current = screen_name
    
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
