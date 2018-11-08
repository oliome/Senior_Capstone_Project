from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.adapters.listadapter import ListAdapter
from kivy.properties import StringProperty
#from KivyCalendar import DatePicker

profile_name_text_input = ObjectProperty()
profile_list = ObjectProperty()


class ProfileListButton(ListItemButton):
    pass


class ProfileScreen(Screen):
    profile_name_text_input = ObjectProperty()
    profile_list = ObjectProperty()

    def create_profile(self):
        # Get the profile's name from TextInputs
        profile_name = self.profile_name_text_input.text

        if profile_name != '':
            # Add to ListView
            self.profile_list.adapter.data.extend([profile_name])

            # Reset the ListView
            self.profile_list._trigger_reset_populate()

    def delete_profile(self):
        # If a list item is selected
        if self.profile_list.adapter.selection:

            # Get the text from the item selected
            selection = self.profile_list.adapter.selection[0].text

            # Remove the matching item
            self.profile_list.adapter.data.remove(selection)

            # Reset the ListView
            self.profile_list._trigger_reset_populate()

    #def view_database(self):
     #   if self.profile_list.adapter.selection:


class MenuScreen(Screen):
    pass


class InventoryScreen(Screen):
    def sort_items(self):
        pass

    def sort_dates(self):
        pass


class AddItemScreen(Screen):
    pass


class GroceryLoggerApp(App):
    def build(self):
        self.title = "Gro-Log"
        screen_manager = ScreenManager()
        screen_manager.add_widget(ProfileScreen(name="profile_screen"))
        screen_manager.add_widget(MenuScreen(name="menu_screen"))
        screen_manager.add_widget(InventoryScreen(name="inventory_screen"))
        screen_manager.add_widget(AddItemScreen(name="additem_screen"))
        return screen_manager


my_app = GroceryLoggerApp()
my_app.run()
