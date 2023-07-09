from View.base_screen import BaseScreenView
from kivymd.uix.list import MDList,TwoLineAvatarIconListItem,IconLeftWidget,IconRightWidget

class EventListScreenView(BaseScreenView):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def update_list(self, events: list) -> None:
        """
        Updates the list of events.
        """
        list = self.ids.event_list

        list.clear_widgets()

        for event in events:
            item = TwoLineAvatarIconListItem(
                IconLeftWidget(
						icon="pencil",
						on_release=lambda x: x #self.edit_event(event)
						),
					IconRightWidget(
						icon="delete",
						on_release=lambda x: self.delete_event(event)
						),
                text=event['title'],
                secondary_text=event['start_date'] + ' ' + event['start_time'] + ' - ' + event['end_date'] + ' ' + event['end_time'] + ' ' + event['description']
            )
            list.add_widget(item)

    def delete_event(self, event):
        self.controller.delete_event(event)

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        events = self.model.get_events()
        self.update_list(events)
        
