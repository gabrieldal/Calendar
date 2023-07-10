from Model.base_model import BaseScreenModel
import json


class EventListScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.event_list_screen.EventListScreen.EventListScreenView` class.
    """
    def __init__(self):
        super().__init__()
        self.events = []

    def load_events(self):
        try:
            with open('events.json', 'r+') as file:
                try:
                    self.events = json.load(file)
                except json.JSONDecodeError:
                    self.events = []

        except FileNotFoundError:
            with open('events.json', 'w') as file:
                json.dump(self.events, file, indent=4)
        self.notify_observers()


    def delete_event(self, event):
        # Carregar a lista de eventos do arquivo JSON
        with open('events.json', 'r') as file:
            self.events = json.load(file)

        # Encontrar o índice do evento na lista
        index = self.get_event_index(event)
        if index != -1:
            # Remover o evento da lista
            del self.events[index]

            # Salvar a lista atualizada de eventos no arquivo JSON
            with open('events.json', 'w') as file:
                json.dump(self.events, file, indent=4)
        else:
            # Se o evento não foi encontrado, você pode escolher lançar uma exceção ou realizar outra ação, conforme necessário
            raise ValueError('Evento não encontrado na lista de eventos')

        # Carregar novamente a lista de eventos atualizada
        self.load_events()

    def get_event_index(self, event):
        # Carregar a lista de eventos do arquivo JSON
        with open('events.json', 'r') as file:
            self.events = json.load(file)

        # Encontrar o índice do evento na lista
        for index, e in enumerate(self.events):
            if e == event:
                return index
        
        # Se o evento não foi encontrado, retornar -1 ou lançar uma exceção, conforme necessário
        return -1


    def get_events(self):
        """
        Returns the list of events.
        """
        return self.events
    
    