from View.base_screen import BaseScreenView
from libs.datepicker import DatePicker
from libs.timepicker import TimePicker


class EventsScreenView(BaseScreenView):
    def __init__(self, **kw):
        super().__init__(**kw)

    def save_event_data(self):
        event_data = {
            'title': self.ids.title_field.text,
            'start_date': self.ids.start_date_field.text,
            'end_date': self.ids.end_date_field.text,
            'start_time': self.ids.start_time_field.text,
            'end_time': self.ids.end_time_field.text,
            'description': self.ids.description_field.text
        }
        self.controller.on_save_event(event_data)

    def clear_fields(self):
        self.ids.title_field.text = ''
        self.ids.start_date_field.text = ''
        self.ids.end_date_field.text = ''
        self.ids.start_time_field.text = ''
        self.ids.end_time_field.text = ''
        self.ids.description_field.text = ''

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    
