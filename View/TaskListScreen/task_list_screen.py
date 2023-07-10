from View.base_screen import BaseScreenView
from kivymd.uix.list import MDList,OneLineAvatarIconListItem,IconLeftWidget,IconRightWidget, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item'''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # state a pk which we shall use link the list items with the database primary keys
        #self.pk = pk
        self.text = kwargs['text']
        self.id = kwargs['id']
        self.markup=True


    def mark(self, list_item):
        '''mark the task as complete or incomplete'''
        

        if list_item.ids.check.active:
            list_item.text = '[s]'+list_item.text+'[/s]'
            #db.mark_task_as_complete(list_item.pk)# here
        else:
            list_item.text = self.text


class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom left container'''


class TaskListScreenView(BaseScreenView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save_task(self):
        task_data = {
            'title': self.ids.input_task.text,
            'completed': False
        }
        self.controller.on_save_task(task_data)

    def clear_field(self):
        self.ids.input_task.text = ''

    def update_list(self, tasks: list) -> None:
        """
        Updates the list of tasks.
        """
        list = self.ids.task_list
        list.clear_widgets()

        for task in tasks:
            item = OneLineAvatarIconListItem(
                LeftCheckbox(
                    id='check',
                    on_release= lambda x: self.switch_task(task) # por que ta passando a ultima task adicionada como paramtro?
                    ),
                IconRightWidget(
                    icon= 'trash-can-outline',
                    on_release= lambda x: self.delete_task(task)
                    ),
                text=task['title']
            )
            list.add_widget(item)

    def delete_task(self, item):
        self.controller.delete_task(item)
        
    def switch_task(self, item):
        self.controller.switch_task_status(item)

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        tasks = self.controller.get_tasks()
        self.update_list(tasks)