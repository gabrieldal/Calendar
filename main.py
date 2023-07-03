from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import MDList,TwoLineAvatarIconListItem,IconLeftWidget,IconRightWidget
from libs.datepicker import CalendarWidget
from libs.events import CalendarEventScreen
import json
import os

class CalendarScreen(Screen):
    pass

class EventScreen(CalendarEventScreen):
    pass

class EventViewScreen(Screen):
    def on_pre_enter(self):
        app = MDApp.get_running_app()
        app.load_events()

class MainApp(MDApp):
    def build(self):
        # Verifica se o arquivo events.json existe
        if not os.path.isfile('events.json'):
            # Cria o arquivo events.json se não existir
            with open('events.json', 'w') as f:
                f.write('[]')  # Escreve uma lista vazia no arquivo

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        sm = ScreenManager()
        sm.add_widget(CalendarScreen(name='calendar'))
        sm.add_widget(EventScreen(name='event'))
        sm.add_widget(EventViewScreen(name='event_view'))
        return sm
    
    def show_event_screen(self):
        self.root.transition = SlideTransition(direction='left')
        self.root.current = 'event'
        self.root.transition = NoTransition()
        self.root.transition = SlideTransition(direction='right')

    def show_calendar_screen(self):
        event_screen = self.root.get_screen('event')
        event_screen.ids.title_field.text = ''
        event_screen.ids.start_date_field.text = ''
        event_screen.ids.end_date_field.text = ''
        event_screen.ids.start_time_field.text = ''
        event_screen.ids.end_time_field.text = ''
        event_screen.ids.description_field.text = ''
        self.root.transition = SlideTransition(direction='right')
        self.root.current = 'calendar'
        self.root.transition = NoTransition()
        self.root.transition = SlideTransition(direction='left')

    def show_event_view_screen(self):
        self.root.transition = SlideTransition(direction='right')
        self.root.current = 'event_view'
        self.root.transition = NoTransition()
        self.root.transition = SlideTransition(direction='left')

    def save_event(self):
        event_screen = self.root.get_screen('event')
        title = event_screen.ids.title_field.text
        start_date = event_screen.ids.start_date_field.text
        end_date = event_screen.ids.end_date_field.text
        start_time = event_screen.ids.start_time_field.text
        end_time = event_screen.ids.end_time_field.text
        description = event_screen.ids.description_field.text
        
        event_data = {
            'title': title,
            'start_date': start_date,
            'end_date': end_date,
            'start_time': start_time,
            'end_time': end_time,
            'description': description
        }
        
        with open('events.json', 'r+') as file:
            try:
                events = json.load(file)
            except json.JSONDecodeError:
                events = []
            
            editing_event_index = getattr(event_screen, 'editing_event_index', None)
            if editing_event_index is not None:
                events[editing_event_index] = event_data
            else:
                events.append(event_data)
            
            file.seek(0)  # Volta para o início do arquivo
            json.dump(events, file, indent=4)
            file.truncate()  # Limpa o conteúdo restante, se houver
        
        event_screen.ids.title_field.text = ''
        event_screen.ids.start_date_field.text = ''
        event_screen.ids.end_date_field.text = ''
        event_screen.ids.start_time_field.text = ''
        event_screen.ids.end_time_field.text = ''
        event_screen.ids.description_field.text = ''
        
        self.show_calendar_screen()

    def load_events(self):
        with open('events.json', 'r') as file:
            try:
                events = json.load(file)
            except json.JSONDecodeError:
                events = []

        screen = self.root.get_screen('event_view')
        list = screen.ids.event_list

        list.clear_widgets()

        for event in events:
            item = TwoLineAvatarIconListItem(
                IconLeftWidget(
						icon="pencil",
						on_release=lambda x: self.edit_event(event)
						),
					IconRightWidget(
						icon="delete",
						on_release=lambda x: self.delete_event(event)
						),
                text=event['title'],
                secondary_text=event['start_date'] + ' ' + event['start_time'] + ' - ' + event['end_date'] + ' ' + event['end_time'] + ' ' + event['description']
            )
            list.add_widget(item)
        
    def edit_event(self, event):
        event_screen = self.root.get_screen('event')
        event_screen.ids.title_field.text = event['title']
        event_screen.ids.start_date_field.text = event['start_date']
        event_screen.ids.start_time_field.text = event['start_time']
        event_screen.ids.end_date_field.text = event['end_date']
        event_screen.ids.end_time_field.text = event['end_time']
        event_screen.ids.description_field.text = event['description']
        event_screen.editing_event_index = self.get_event_index(event)
        self.show_event_screen()

    def delete_event(self, event):
        # Carregar a lista de eventos do arquivo JSON
        with open('events.json', 'r') as file:
            events = json.load(file)

        # Encontrar o índice do evento na lista
        index = self.get_event_index(event)
        if index != -1:
            # Remover o evento da lista
            del events[index]

            # Salvar a lista atualizada de eventos no arquivo JSON
            with open('events.json', 'w') as file:
                json.dump(events, file, indent=4)
        else:
            # Se o evento não foi encontrado, você pode escolher lançar uma exceção ou realizar outra ação, conforme necessário
            raise ValueError('Evento não encontrado na lista de eventos')

        # Carregar novamente a lista de eventos atualizada
        self.load_events()

    def get_event_index(self, event):
        # Carregar a lista de eventos do arquivo JSON
        with open('events.json', 'r') as file:
            events = json.load(file)

        # Encontrar o índice do evento na lista
        for index, e in enumerate(events):
            if e == event:
                return index

        # Se o evento não foi encontrado, retornar -1 ou lançar uma exceção, conforme necessário
        return -1

if __name__ == '__main__':
    MainApp().run()
