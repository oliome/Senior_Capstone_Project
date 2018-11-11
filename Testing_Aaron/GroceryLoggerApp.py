import json
import requests

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
        self.selection_mode = 'multiple'


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
    item_list = ObjectProperty()

    items = ["Great Value 2% Milk", "12/25/18", "078742022871", "Tyson Frozen Chicken", "JIF Peanut Butter 40oz",
             "Chipotle Tabasco", "Kraft Cheddar Cheese", "Lay's Sour Cream and Onion Chips", "Great Value 2% Milk",
             "Tyson Frozen Chicken", "JIF Peanut Butter 40oz", "Chipotle Tabasco", "Kraft Cheddar Cheese",
             "Lay's Sour Cream and Onion Chips", "Great Value 2% Milk", "Tyson Frozen Chicken",
             "JIF Peanut Butter 40oz", "Chipotle Tabasco", "Kraft Cheddar Cheese", "Lay's Sour Cream and Onion Chips"]

    def sort_items(self):
        pass

    def sort_dates(self):
        pass

    def search_recipes(self):
        #if a list item is selected
        if self.item_list.adapter.selection:
            selection = self.item_list.adapter.selection[0].text
            App_ID = 'cf938db6'
            APP_KEY = '91a43a29d2211953084fcca6b71b005b'
            r = requests.get('https://api.edamam.com/search?q='+selection +'&app_id='+App_ID+'&app_key='+APP_KEY)
            data = r.json()
            for i in data['hits']:
                print('*****************************')
                print('*****************************')
                data1 = i['recipe']
                dishName = data1['label']
                print('Recipe for '+dishName)
                for recipe in data1['ingredientLines']:
                    print(recipe)


class AddItemScreen(Screen):
    def search_item(self, barcode_number):
        if barcode_number.text != '':
            r = requests.get(r'https://api.barcodelookup.com/v2/products?barcode='+barcode_number.text+'&formatted=y&key=i35p2ky2g8uicz1palr2al0ndb1c2t')
            data = r.json()
            # displaying in json format
            item = data['products'][0]['product_name']
            # grabbing the brand property from the products array. Debug for more info
            print(item)
            print(barcode_number.text)
        else:
            print("no barcode entered")


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
