from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.graphics import Color, Rectangle
from libs.datepicker import CalendarWidget

class CalendarScreen(MDBoxLayout):
    def __init__(self, **kwargs):
        super(CalendarScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = "10dp"
        
        with self.canvas:
            Color(0, 0, 0, 1)  # Cor de fundo preta
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

        calendar_widget = CalendarWidget()
        self.add_widget(calendar_widget)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class MainApp(MDApp):
    def build(self):
        return CalendarScreen()


if __name__ == '__main__':
    MainApp().run()
