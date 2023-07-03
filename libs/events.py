from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from libs.datepicker import DatePicker
from libs.timepicker import TimePicker
import json


# Carregando o arquivo KV
Builder.load_string('''
<CalendarEventScreen>:
    name: 'calendar_event'
    
    MDBoxLayout:
        orientation: 'vertical'
        canvas:
            Color:
                rgba: 0, 0, 0, 1  # Cor de fundo preta
            Rectangle:
                pos: self.pos
                size: self.size
        MDTopAppBar:
            title: 'Cadastro de Evento'
            elevation: 10
            left_action_items: [['arrow-left', lambda x: app.show_calendar_screen()]]
        
        ScrollView:
            
            MDBoxLayout:
                orientation: 'vertical'
                padding: '16dp'
                
                MDTextField:
                    id: title_field
                    hint_text: 'Título'
                    text_color_normal: 1, 1, 1, 1
                    
                MDBoxLayout:
                    spacing: '8dp'

                    DatePicker:
                        id: start_date_field
                        hint_text: 'Data de início'
                        text_color_normal: 1, 1, 1, 1

                    TimePicker:
                        id: start_time_field
                        hint_text: 'Hora de início'
                        text: '01:00'
                        text_color_normal: 1, 1, 1, 1
                        validator: "time"
                        
                MDBoxLayout:
                    spacing: '8dp'

                    DatePicker:
                        id: end_date_field
                        hint_text: 'Data de término'
                        text_color_normal: 1, 1, 1, 1
                        
                    TimePicker:
                        id: end_time_field
                        hint_text: 'Hora de término'
                        text: '02:00'
                        text_color_normal: 1, 1, 1, 1
                        validator: "time"
                
                MDTextField:
                    id: description_field
                    hint_text: 'Descrição'
                    multiline: True
                    text_color_normal: 1, 1, 1, 1
                
                MDRaisedButton:
                    text: 'Salvar'
                    on_release: app.save_event()
                    size_hint: None, None
                    size: dp(120), dp(48)
                    pos_hint: {'center_x': 0.5}
''')



class CalendarEventScreen(Screen):
    def build(self):
        screen = CalendarEventScreen()
        return screen
    
    

