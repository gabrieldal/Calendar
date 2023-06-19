import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from datetime import datetime, timedelta

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        header = Label(text=self.get_current_month(), size_hint=(1, 0.1))
        layout.add_widget(header)

        calendar_layout = GridLayout(cols=7)
        for day in ['D', 'S', 'T', 'Q', 'Q', 'S', 'S']:
            calendar_layout.add_widget(Label(text=day))

        prev_days = self.get_month_days()
        for i in range(prev_days[0].weekday()+1):
            prev_month_day = prev_days[0] - timedelta(days=1)
            calendar_layout.add_widget(Button(text=str(prev_month_day.day), disabled=True))
            prev_days.insert(0, prev_month_day)

        days = self.get_month_days()
        for day in days:
            button = Button(text=str(day.day))
            calendar_layout.add_widget(button)

        while len(calendar_layout.children) < 42:
            next_month_day = days[-1] + timedelta(days=1)
            calendar_layout.add_widget(Button(text=str(next_month_day.day), disabled=True))
            days.append(next_month_day)
            

        layout.add_widget(calendar_layout)
        return layout
    

    def get_current_month(self):
        month_names = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
                       'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        now = datetime.now()
        return month_names[now.month - 1] + ' ' + str(now.year)
    
    def get_month_days(self):
        now = datetime.now()
        first_day = datetime(now.year, now.month, 1)
        last_day = datetime(now.year, now.month + 1, 1) - timedelta(days=1)
        days = []
        current_day = first_day
        while current_day <= last_day:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days


    
if __name__ == '__main__':
    MyApp().run()