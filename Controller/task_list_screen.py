
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

    def get_view(self) -> TaskListScreenView:
        return self.view
