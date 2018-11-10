from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.listview import ListItemButton, ListItemLabel, CompositeListItem, ListView
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.adapters.listadapter import ListAdapter
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty


profile_name_text_input = ObjectProperty()
profile_list = ObjectProperty()

item_name_text_input = ObjectProperty()
item_list = ObjectProperty()


class ProfileListButton(ListItemButton):
    def __init__(self, **kwargs):
        super(ProfileListButton, self).__init__(**kwargs)
        self.height = "75dp"


class ItemListButton(ListItemButton):
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

    def add_item(self):
        item_name = self.profile_name_text_input.text
        if item_name != '':
            # Add to ListView
            self.profile_list.adapter.data.extend([item_name])

    items = ["Great Value 2% Milk","12/25/18","078742022871","Tyson Frozen Chicken","JIF Peanut Butter 40oz","Chipotle Tabasco","Kraft Cheddar Cheese","Lay's Sour Cream and Onion Chips","Great Value 2% Milk","Tyson Frozen Chicken","JIF Peanut Butter 40oz","Chipotle Tabasco","Kraft Cheddar Cheese","Lay's Sour Cream and Onion Chips","Great Value 2% Milk","Tyson Frozen Chicken","JIF Peanut Butter 40oz","Chipotle Tabasco","Kraft Cheddar Cheese","Lay's Sour Cream and Onion Chips"]


class AddItemScreen(Screen):
    def add_item(self):
        item_name = self.profile_name_text_input.text
        if item_name != '':
            # Add to ListView
            self.profile_list.adapter.data.extend([item_name])


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
