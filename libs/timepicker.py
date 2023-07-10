from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivymd.uix.textfield import MDTextField
from kivy.uix.popup import Popup
from datetime import datetime

class TimePicker(MDTextField):
    def __init__(self, *args, **kwargs):
        super(TimePicker, self).__init__(*args, **kwargs)
        
        self.init_ui() 
        
    def init_ui(self):
        self.clock = MDTimePicker()
        self.popup = Popup(content=self.clock)
        self.clock.parent_popup = self.popup
        
        self.bind(focus=self.show_time_picker)
        
    def show_time_picker(self, isnt, time):
        if time:
            parent_layout = self.clock.parent
            if parent_layout:
                parent_layout.remove_widget(self.clock)
            previous_time = datetime.strptime("03:20", '%H:%M').time()
            self.clock.set_time(previous_time)
            self.clock.bind(time=self.get_time)
            self.clock.open()
        
        
    def get_time(self, instance, time):
        formatted_time = time.strftime("%H:%M")
        self.text = formatted_time