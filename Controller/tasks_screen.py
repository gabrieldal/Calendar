
from View.TasksScreen.tasks_screen import TasksScreenView


class TasksScreenController:
    """
    The `TasksScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.tasks_screen.TasksScreenModel
        self.view = TasksScreenView(controller=self, model=self.model)

    def get_view(self) -> TasksScreenView:
        return self.view
