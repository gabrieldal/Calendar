from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from datepicker import CalendarWidget

class CalendarScreen(MDBoxLayout):
    pass


class MainApp(MDApp):
    def build(self):
        Window.size = (300, 500)  # Tamanho da janela para exibição desktop
        return CalendarScreen()


if __name__ == '__main__':
    MainApp().run()
