from Model.base_model import BaseScreenModel
import json


class TaskListScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.task_list_screen.TaskListScreen.TaskListScreenView` class.
    """
    def __init__(self):
        super().__init__()
        self.tasks = []

    def save_task(self, task_data):
        # Carregar a lista de eventos do arquivo JSON
        try:
            with open('tasks.json', 'r+') as file:
                try:
                    self.tasks = json.load(file)
                except json.JSONDecodeError:
                    self.tasks = []
                
                self.tasks.append(task_data)
                
                file.seek(0)
                json.dump(self.tasks, file, indent=4)
                file.truncate()
        except FileNotFoundError:
            with open('tasks.json', 'w') as file:
                self.tasks = task_data
                json.dump(self.tasks, file, indent=4)
        # Carregar novamente a lista de eventos atualizada
        self.load_tasks()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r+') as file:
                try:
                    self.tasks = json.load(file)
                except json.JSONDecodeError:
                    self.tasks = []

        except FileNotFoundError:
            with open('tasks.json', 'w') as file:
                json.dump(self.tasks, file, indent=4)
        self.notify_observers()

    def detele_task(self, task):
        # Carregar a lista de eventos do arquivo JSON
        with open('tasks.json', 'r') as file:
            self.tasks = json.load(file)

        # Encontrar o índice do evento na lista
        index = self.get_task_index(task)
        if index != -1:
            # Remover o evento da lista
            del self.tasks[index]

            # Salvar a lista atualizada de eventos no arquivo JSON
            with open('tasks.json', 'w') as file:
                json.dump(self.tasks, file, indent=4)
        else:
            # Se o evento não foi encontrado, você pode escolher lançar uma exceção ou realizar outra ação, conforme necessário
            raise ValueError('Evento não encontrado na lista de eventos')

        # Carregar novamente a lista de eventos atualizada
        self.load_tasks()

    def get_task_index(self, task):
        # Carregar a lista de eventos do arquivo JSON
        with open('tasks.json', 'r') as file:
            self.tasks = json.load(file)

        # Encontrar o índice do evento na lista
        for index, e in enumerate(self.tasks):
            if e == task:
                return index
        
        # Se o evento não foi encontrado, retornar -1 ou lançar uma exceção, conforme necessário
        return -1

    def get_tasks(self):
        return self.tasks