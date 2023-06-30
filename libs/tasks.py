from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox


class TasksPopup(Popup):
    def __init__(self, day, **kwargs):
        super(TasksPopup, self).__init__(**kwargs)
        self.title = f"Tasks for Day {day}"
        self.size_hint = (0.8, 0.6)
        self.content = self.create_content()

    def create_content(self):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        task1_input = TextInput(hint_text="Task 1", size_hint=(1, 0.1))
        content.add_widget(task1_input)

        task2_input = TextInput(hint_text="Task 2", size_hint=(1, 0.1))
        content.add_widget(task2_input)

        completed_checkbox = CheckBox(active=False, size_hint=(1, 0.1))
        content.add_widget(completed_checkbox)

        return content