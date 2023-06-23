from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDDatePicker

Builder.load_string("""
<CalendarWidget>:
    orientation: 'vertical'
    padding: "10dp"

    MDFlatButton:
        text: "Selecionar Data"
        on_release: root.show_date_picker()

    MDLabel:
        id: selected_date_label
        text: "Data selecionada:"

""")


class CalendarWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CalendarWidget, self).__init__(**kwargs)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_save, on_cancel=self.on_date_cancel)
        date_dialog.open()

    def on_date_save(self, instance, date):
        selected_date_label = self.ids.selected_date_label
        selected_date_label.text = f"Data selecionada: {date.strftime('%d/%m/%Y')}"

    def on_date_cancel(self, instance, date):
        pass


class CalendarApp(MDApp):
    def build(self):
        return CalendarWidget()


if __name__ == "__main__":
    CalendarApp().run()
