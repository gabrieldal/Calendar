from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivyIsoDatepicker import CalendarWidget


class CalendarScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(CalendarScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        calendar_widget = CalendarWidget()
        self.add_widget(calendar_widget)


class CalendarApp(App):
    def build(self):
        return CalendarScreen()


if __name__ == '__main__':
    CalendarApp().run()
