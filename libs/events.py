from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from libs.datepicker import DatePicker


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

                    MDTextField:
                        id: start_time_field
                        hint_text: 'Hora de início'
                        text: '01:00'
                        text_color_normal: 1, 1, 1, 1
                        on_double_tap: app.show_time_picker()
                        
                MDBoxLayout:
                    spacing: '8dp'

                    DatePicker:
                        id: end_date_field
                        text_color_normal: 1, 1, 1, 1
                        hint_text: 'Data de término'
                        
                    MDTextField:
                        id: end_time_field
                        hint_text: 'Hora de término'
                        text: '02:00'
                        text_color_normal: 1, 1, 1, 1
                        on_double_tap: app.show_time_picker()
                
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
    
    def show_calendar_screen(self):
        # Implemente a lógica para exibir a tela de calendário
        pass

    
    def save_event(self):
        # Implemente a lógica para salvar o evento no calendário
        title = self.root.ids.title_field.text
        start_date = self.root.ids.start_date_field.text
        end_date = self.root.ids.end_date_field.text
        start_time = self.root.ids.start_time_field.text
        end_time = self.root.ids.end_time_field.text
        description = self.root.ids.description_field.text
        
        # Faça algo com os dados do evento
        
        # Limpe os campos de entrada
        self.root.ids.title_field.text = ''
        self.root.ids.start_date_field.text = ''
        self.root.ids.end_date_field.text = ''
        self.root.ids.start_time_field.text = ''
        self.root.ids.end_time_field.text = ''
        self.root.ids.description_field.text = ''
        
