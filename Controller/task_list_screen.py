
from View.TaskListScreen.task_list_screen import TaskListScreenView


class TaskListScreenController:
    """
    The `TaskListScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.task_list_screen.TaskListScreenModel
        self.view = TaskListScreenView(controller=self, model=self.model)

    def on_save_task(self, task_data):
        self.model.save_task(task_data)
        self.view.clear_field()

    def go_back(self):
        self.view.manager_screens.current = 'calendar screen'
        self.view.manager_screens.transition.direction = 'left'
        self.view.clear_field()

    def load_tasks(self):
        self.model.load_tasks()

    def delete_task(self, task):
        self.model.delete_task(task)

    def get_tasks(self):
        return self.model.get_tasks()
    
    def switch_task_status(self, task):
        self.model.switch_task(task)

    def get_view(self) -> TaskListScreenView:
        return self.view
