from View.base_screen import BaseScreenView
from kivymd.uix.list import MDList,OneLineAvatarIconListItem,IconLeftWidget,IconRightWidget

class TaskListScreenView(BaseScreenView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save_task(self, task_data):
        task_data = self.ids.input_task.text
        self.controller.on_save_task(task_data)

    def clear_field(self):
        self.ids.input_task.text = ''

    def update_list(self, tasks):
        """
        Updates the list of tasks.
        """
        list = self.ids.task_list
        list.clear_widgets()

        for task in tasks:
            item = OneLineAvatarIconListItem(
                IconLeftWidget(
                        icon="pencil",
                        on_release=lambda x: x #self.edit_task(task)
                        ),
                    IconRightWidget(
                        icon="delete",
                        on_release=lambda x: self.delete_task(task)
                        ),
                text=task
            )
            list.add_widget(item)

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        tasks = self.controller.get_tasks()
        self.update_list(tasks)