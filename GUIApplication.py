from kivy.app  import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties  import ListProperty, ObjectProperty
from kivy.uix.listview import ListItemButton, ListItemLabel, CompositeListItem, ListView
from kivy.uix.button import Button
from random import shuffle
from functools import partial

import json
import requests

my_list = ['Zack','Ollie','Reyhan','Aaron']

Builder.load_string('''
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton
#: import Button kivy.uix.button.Button
#: import main GUIApplication
<HeaderButton@Button>:
    font_size: 32
    size_hint_y: .1

<MiniButton@Button>:
    font_size: 16
    size_hint: .1, .1

<StandardButton@Button>:
    font_size: 16


    #background_normal: 'grey.jpg'
    #background_down: ''
    #background_color: .88, .88, .88, 1
    size_hint: .2, .1

<MyScreenManager>:
    box2: box2
    Screen:
        name: "openscreen"
        BoxLayout:
            orientation: "horizontal"
            Button:
                font_size: 32
                background_normal: ''
                background_color: 1, .3, .4, .85
                text: "Gro - Log"
                on_release:
                    root.current = "screen2"

    Screen:
        name: "screen2"
        on_enter: root.update_buttons()
        BoxLayout:
            id: box2
            orientation: "horizontal"
     
            Button:
                
                text: "Add New Profile"
                on_release:
                    root.current = "screen1"

    Screen:
        name: "screen1"
        on_leave: root.ids.textinput.text = ''
        on_enter: root.ids.textinput.focus = True
        Popup:
            title: 'What is your name?'
            title_align: 'center'
            auto_dismiss: False
            content: box
            pos_hint: {'x': .3, 'y': .4}
            size_hint: (None, None)
            size: (400, 100)    
            BoxLayout:
                id: box
                TextInput:
                    id: textinput
                    focus: True
                    text: ''
                    multiline: False
                    font_size: 24
                    on_text_validate: root.added_buttons.append(Button(text=root.ids.textinput.text))
                    on_text_validate: root.current = "screen2"
                Button: 
                    id: createButton
                    text: 'Create Profile'
                    size_hint: (.5, 1)
                    on_press: root.added_buttons.append(Button(text=root.ids.textinput.text))
                    on_press: root.current = "screen2"
                Button:
                    id: cancelButton
                    text: 'Cancel'
                    size_hint: (.3, 1)
                    on_press: root.current = "screen2"   

    Screen:
        name: "screen3"
        
        Button:
            id: bannerbutton
            font_size: 15
            size_hint_y: .04
            text: ""
            pos_hint: {"center_x": .5, "top": 1}
        GridLayout:
            cols: 2
            size_hint: .7, .2
            pos_hint: {"center_x": .5, "top": .6}
            spacing: 50
            Button:
                text: "Add Item"
                pos_hint: {"bottom": .5}
                on_press:
                    root.transition.direction = "up"
                    root.current = "screen4"
            Button:
                text: "View Food Inventory"
                on_press:
                    root.transition.direction = "left"
                    root.current = "screen5"
        GridLayout:
            cols: 1
            size_hint: .2, .1
            pos_hint: {"center_x": .5}
            Button:
                text: "Switch Profile"
                on_press:
                    root.transition.direction = "right"
                    root.current = "screen2"


    Screen:
        name:"screen4"
        on_leave: root.ids.barcode_number.text = ''
        on_enter: root.ids.barcode_number.focus = True
        on_leave: root.ids.itemname.text = ''
        FloatLayout:
            Label:
                id: itemname
                pos_hint: {"center_x": .7, "top": .8}
                text: ""
            Button:
                font_size: 15
                size_hint_y: .04
                text: "Add an Item"
                pos_hint: {"center_x": .5, "top": 1}
            Button:
                size_hint: .2, .1
                font_size: 16
                text: "Back to Inventory"
                pos_hint: {"top": .9}
                on_press:
                    root.transition.direction = "down"
                    root.current = "screen5"

        
            TextInput:
                id: barcode_number
                hint_text: "Scan or Enter Barcode Number"
                write_tab: False
                multiline: False
                pos_hint: {"center_x": .4, "top": .7}
                size_hint: .4,.05

            Button:
                
                text: "Search"
                pos_hint: {"center_x": .7, "top": .7}
                size_hint: .2,.05
                on_press:
                    root.search_item(barcode_number)
                on_press: 

            Button:
                
                text: "Enter Expiration Date (optional)"
                pos_hint: {"center_x": .5, "top": .65}
                size_hint: .6,.05
                on_press:
                    root.get_date(month, day, year)

            Spinner:
                id: month
                text: "Select Month"
                pos_hint: {"center_x": .3, "top": .6}
                size_hint: .2,.05
                values: ['01','02','03','04','05','06','07','08','09','10','11','12']

            Spinner:
                id: day
                text: "Select Day"
                pos_hint: {"center_x": .5, "top": .6}
                size_hint: .2,.05
                values: ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

            Spinner:
                id: year
                text: "Select Year"
                pos_hint: {"center_x": .7, "top": .6}
                size_hint: .2,.05
                values: ['2018','2019','2020']





            Button:
                font_size: 16
                size_hint: .1, .1
                text: "Submit"
                pos_hint: {"center_x": .2 , "center_y": .1}

            Button:
                font_size: 16
                size_hint: .1, .1
                text: "Other"
                pos_hint: {"center_x": .33, "center_y": .1}

            Button:
                font_size: 16
                size_hint: .1, .1
                text: "Cancel"
                pos_hint: {"center_x": .46, "center_y": .1}
                on_press:
                    root.transition.direction = "down"
                    root.current = "screen5"       
    Screen:
        name:"screen5"
        item_list: item_list_view

        FloatLayout:
            StandardButton:
                text: "Back to Main Menu"
                pos_hint: {"top": .9}
                on_press:
                    app.root.transition.direction = "right"
                    app.root.current = "screen3"

            HeaderButton:
                text: "Your Food Inventory"
                pos_hint: {"center_x": .5, "top": 1}

            GridLayout:
                cols: 3
                size_hint_y: .1
                pos_hint: {"top": .8}
                Button:
                    text: "Item Name"
       
                Button:
                    text: "Expiration Date"
                Button:
                    text: "Barcode/UPC Number"


            GridLayout:
                cols: 3

                padding: [0,0,0,300]
                pos_hint: {"top": .7}
                ListView:
                    id: item_list_view
                    adapter: ListAdapter(data=["Great Value Milk","Tyson Frozen Chicken","JIF Creamy Peanut Butter","Chipotle Tabasco", "Kraft Cheddar Cheese", "Lay's Sour Cream and Onion Chips", "Great Value 2% Milk"], cls=main.ItemListButton, selection_mode='multiple')
#                adapter: ListAdapter(data=["Great Value 2% Milk                                           12/25/18                                         123412346","Tyson Frozen Chicken","JIF Peanut Butter 40oz","Chipotle Tabasco","Kraft Cheddar Cheese","Lay's Sour Cream and Onion Chips","Great Value 2% Milk","Tyson Frozen Chicken","JIF Peanut Butter 40oz","Chipotle Tabasco","Kraft Cheddar Cheese","Lay's Sour Cream and Onion Chips","Great Value 2% Milk","Tyson Frozen Chicken","JIF Peanut Butter 40oz","Chipotle Tabasco","Kraft Cheddar Cheese","Lay's Sour Cream and Onion Chips"], cls=main.ItemListButton)



            MiniButton:
                text: "Delete"
                pos_hint: {"center_x": .2 , "center_y": .1}

            StandardButton:
                id: search
                text: "Search Recipes"
                pos_hint: {"center_x": .38, "center_y": .1}
                on_press:
                    root.search_recipes()

            MiniButton:
                text: "Add"
                pos_hint: {"center_x": .56, "center_y": .1}
                on_press:
                    root.transition.direction = "up"
                    root.current = "screen4"

''')
#instance is the last button added
class MyScreenManager(ScreenManager):
    added_buttons = ListProperty([])
    item_list = ObjectProperty()
    box2 = ObjectProperty(None)

    def __init__(self,*args, **kwargs):
      super().__init__(*args, **kwargs)
      for i in my_list:
          name = i
          self.make_buttons(name)
          
          
    def make_buttons(self, name):
        newbutton = Button(text=name)
        newbutton.bind(on_press = partial(lambda a:self.auth(name)))
        self.added_buttons.append(newbutton)
    
    def update_buttons(self,*args):
        
        #self.box2.clear_widgets()
        shuffle(self.added_buttons)

        for i in self.added_buttons:
            name = i.text
            i.bind(on_press= partial(lambda a:self.auth(name)))
            self.box2.add_widget(i)
            
            
            
        self.added_buttons[:] = []

    def auth(self,instance):
        self.transition.direction = "left"
        self.current = "screen3" 
        self.ids.bannerbutton.text = "Welcome " + instance + "!"

    def search_item(self, barcode_number):
        if barcode_number.text != '':
            r = requests.get(r'https://api.barcodelookup.com/v2/products?barcode='+barcode_number.text+'&formatted=y&key=i35p2ky2g8uicz1palr2al0ndb1c2t')
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
        else: print(month.text+"/"+day.text+"/"+year.text)

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
     
class ItemListButton(ListItemButton):
    pass
  
class MyApp(App):

    def build(self):
        self.title = "Gro-Log"
        return MyScreenManager()

MyApp().run()
