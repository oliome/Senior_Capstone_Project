from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.listview import ListItemButton, ListItemLabel, CompositeListItem, ListView
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from random import shuffle
from functools import partial

import json
import requests

my_list = ['Zack', 'Ollie', 'Rehan', 'Aaron']
item_list = ObjectProperty()


class ItemListButton(ListItemButton):
    pass


class Other(Popup):
    pass


# instance is the last button added
class MyScreenManager(ScreenManager):
    added_buttons = ListProperty([])
    item_list = ObjectProperty()
    box2 = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in my_list:
            name = i
            self.make_buttons(name)

    def make_buttons(self, name):
        newbutton = Button(text=name)
        newbutton.bind(on_press=partial(lambda a: self.auth(name)))
        self.added_buttons.append(newbutton)

    def update_buttons(self, *args):

        # self.box2.clear_widgets()
        # shuffle(self.added_buttons) why was this being shuffled in the first place?

        for i in self.added_buttons:
            name = i.text
            i.bind(on_press=partial(lambda a: self.auth(name)))
            self.box2.add_widget(i)

        self.added_buttons[:] = []

    def open_popup(self):
        popup = Other()
        popup.open()

    def auth(self, instance):
        self.transition.direction = "left"
        self.current = "menu_screen"
        self.ids.bannerbutton.text = "Welcome " + instance + "!"

    def search_item(self, barcode_number):
        if barcode_number.text != '':
            r = requests.get(
                r'https://api.barcodelookup.com/v2/products?barcode=' + barcode_number.text + '&formatted=y&key=vwsib6fj958n3v9vtjt7sgtch7xclr')
            data = r.json()
            # displaying in json format
            item = data['products'][0]['product_name']
            # grabbing the brand property from the products array. Debug for more info
            self.ids.itemname.text = item
            print(item)
            print(barcode_number.text)
        else:
            print("no barcode entered")

    def get_date(self, month, day, year):
        if month.text == "Select Month" or day.text == "Select Day" or year.text == "Select Year":
            print("Invalid Expiration Date")
        else:
            date = month.text + "/" + day.text + "/" + year.text
            self.ids.expdate.text = date
            print(date)

    def search_recipes(self):
        # if a list item is selected
        if self.item_list.adapter.selection:
            selection = self.item_list.adapter.selection[0].text
            App_ID = 'cf938db6'
            APP_KEY = '91a43a29d2211953084fcca6b71b005b'
            r = requests.get(
                'https://api.edamam.com/search?q=' + selection + '&app_id=' + App_ID + '&app_key=' + APP_KEY)
            data = r.json()
            for i in data['hits']:
                print('*****************************')
                print('*****************************')
                data1 = i['recipe']
                dishName = data1['label']
                print('Recipe for ' + dishName)
                for recipe in data1['ingredientLines']:
                    print(recipe)


class GroceryLoggerApp(App):

    def build(self):
        self.title = "Gro-Log"
        return MyScreenManager()


GroceryLoggerApp().run()