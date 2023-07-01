from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.pickers import MDTimePicker
from libs.datepicker import CalendarWidget
from libs.events import CalendarEventScreen

class CalendarScreen(Screen):
    pass

class EventScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        sm = ScreenManager()
        sm.add_widget(CalendarScreen(name='calendar'))
        sm.add_widget(EventScreen(name='event'))
        return sm
    
    def show_event_screen(self):
        self.root.current = 'event'

    def show_calendar_screen(self):
        self.root.current = 'calendar'

if __name__ == '__main__':
    MainApp().run()
