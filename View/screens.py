# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.calendar_screen import CalendarScreenModel
from Controller.calendar_screen import CalendarScreenController
from Model.event_list_screen import EventListScreenModel
from Controller.event_list_screen import EventListScreenController
from Model.task_list_screen import TaskListScreenModel
from Controller.task_list_screen import TaskListScreenController
from Model.events_screen import EventsScreenModel
from Controller.events_screen import EventsScreenController
from Model.tasks_screen import TasksScreenModel
from Controller.tasks_screen import TasksScreenController

screens = {
    "calendar screen": {
        "model": CalendarScreenModel,
        "controller": CalendarScreenController,
    },

    "event list screen": {
        "model": EventListScreenModel,
        "controller": EventListScreenController,
    },

    "task list screen": {
        "model": TaskListScreenModel,
        "controller": TaskListScreenController,
    },

    "events screen": {
        "model": EventsScreenModel,
        "controller": EventsScreenController,
    },

    "tasks screen": {
        "model": TasksScreenModel,
        "controller": TasksScreenController,
    },
}