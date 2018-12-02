from kivy.app  import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.adapters.listadapter import ListAdapter
from kivy.properties  import ListProperty, ObjectProperty
from kivy.uix.listview import ListItemButton, ListItemLabel, CompositeListItem, ListView
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from random import shuffle
from functools import partial
from SQLite_test import *
import json
import requests

profile_table_setup()
my_list = select_all_profiles()
item_list = ObjectProperty()
global current_user
current_user=""
q=0
listofrecname=[]
listofrecs=[]
recindex=0

class ItemListButton(ListItemButton):
    pass

class MessageBox(Popup):
    def __init__(self, obj, **kwargs):
        super(MessageBox, self).__init__(**kwargs)
        self.obj = obj

class OtherItems(Popup):
    def get_name(self, itemtext):
        item = ""
        if itemtext.text == "":
            item = "Invalid Item Name"
            self.ids.itemname.text = item

        else:
            item = itemtext.text
            self.ids.itemname.text = item
            return item

    def get_date_pop(self, month, day, year):
        if month.text == "Select Month" or day.text == "Select Day" or year.text == "Select Year":
            date = "Invalid Expiration Date"
            self.ids.expdatepop.text = date

        else:
            date = year.text+"-"+month.text+"-"+day.text
            self.ids.expdatepop.text = date
            return date

    def submit_other(self, month, day, year):
        if self.get_name(self.itemtext):
            array=["",""]
            array[0] = self.get_name(self.itemtext)
            array[1] = self.get_date_pop(month, day, year)
            add_other_inventory(current_user, array)
            self.dismiss()


#instance is the last button added
class MyScreenManager(ScreenManager):
    added_buttons = ListProperty([])
    list_view = ObjectProperty()
    box2 = ObjectProperty(None)

    def __init__(self,*args, **kwargs):
      super().__init__(*args, **kwargs)
      for i in my_list:
          name = i
          self.make_buttons(name)
          
          
    def make_buttons(self, name):
        newbutton = Button(text=name, id = name)
        newbutton.bind(on_press = partial(lambda a:self.auth(name)))
        self.added_buttons.append(newbutton)

    def show_inventory(self):
        return select_inventory(current_user)


    def delete_buttons(self):
        popup = MessageBox(self)    # pass screen1 object
        popup.open()
        global current_user
        for i in self.box2.children:
            if i.text==current_user:
                self.box2.remove_widget(i)
        delete_profile(current_user)
        popup.dismiss()

    def populate_inventory(self,*args):
        list_view= ListView(id="list_view", adapter= ListAdapter(data=select_inventory(current_user), cls=ItemListButton, selection_mode='multiple'))
        self.grid1.add_widget(list_view)

    def depopulate_inventory(self):
        for i in self.grid1.children:
            if i.id=="list_view":
                self.grid1.remove_widget(i)

    def create(self,*args):
        self.current = "create_profile_screen"

    def PopText(self):
        global listofrecname
        global listofrecs
        global q
        
        
        self.ids.recipename.text = listofrecname[q]
        self.ids.ingredients.text = listofrecs[q]

    def RightPopText(self):
        global q
        global recindex
        if(q==recindex-1):
            q=0
        else:
            q+=1
        self.PopText()

    def LeftPopText(self):
        global q
        if(q==0):
            q=recindex-1
        else:
            q-=1
        self.PopText()

    def update_buttons(self):

        add_user = Button(text="Add New Profile")
        add_user.bind(on_press = self.create)
        for i in self.added_buttons:
            name = i.text
            if (name not in select_all_profiles()):
                create_profile(name)

        for j in self.added_buttons:
            name = j.text
            j.bind(on_press= partial(lambda a:self.auth(name)))
            self.box2.add_widget(j)
            
            
            
        self.added_buttons[:]=[]

    def open_popup(self):
        popup = OtherItems()
        popup.open()

    def auth(self,instance):
        self.transition.direction = "left"
        self.current = "menu_screen"
        global current_user
        current_user = instance
        self.ids.bannerbutton.text = "Welcome " + instance + "!"
        self.ids.expirationbutton.text = "You have "+str(count_exp(current_user))+ " items expiring this week!"


    def search_item(self, barcode_number):
        item = ""
        if barcode_number.text != '':
            if barcode_number.text.isdigit():
                if (len(barcode_number.text) == 12):
                    r = requests.get(r'https://api.barcodelookup.com/v2/products?barcode='+barcode_number.text+'&formatted=y&key=q8fh4cx9v6qkwu3d1oh8mo4axf2g0m')
                    if (r.status_code == 200 ):
                        data = r.json()
                        # displaying in json format
                        item = data['products'][0]['product_name']
                        # grabbing the brand property from the products array. Debug for more info
                        self.ids.itemname.text = item
                        return item, barcode_number.text
                    else:
                        self.ids.itemname.text = "Invalid barcode"
                else:
                     self.ids.itemname.text = 'Barcode number enetered is not 7 digits long'       
            else:
                self.ids.itemname.text = "Entered string is not a number"
        else:
            self.ids.itemname.text = "Invalid barcode"


    def get_date(self, month, day, year):
        if month.text == "Select Month" or day.text == "Select Day" or year.text == "Select Year":
            date = "Invalid Expiration Date"
            self.ids.expdate.text = date
        else:
            date = year.text+"-"+month.text+"-"+day.text
            self.ids.expdate.text = date
            return date



    def submit(self, month, day, year, barcode_number):
        if self.itemname.text == "":
            self.search_item(barcode_number)
        if self.get_date(month,day,year):
            array=["","",""]
            (array[0],array[1]) = self.search_item(barcode_number)
            array[2] = self.get_date(month, day, year)
            add_inventory(current_user, array)
            self.ids.barcode_number.text = ""

    def nameTaker(self,selected_inv):
        temp=""
        names=[]
        for i in selected_inv:
            j=0
            temp=""
            i.strip()
            while(j<100):
                if i[j]==' ' and i[j+1]==' ':
                    break
                temp+=i[j]
                j+=1
            names.append(temp)
        return names
            
    def delete_items(self):
        selected=[]
        if len(self.grid1.children[0].adapter.selection)>0:
            for i in self.grid1.children[0].adapter.selection:
                selected.append(i.text)
            selected=self.nameTaker(selected)
            for i in selected:
                delete_inventory(current_user,i)
            self.depopulate_inventory()
            self.populate_inventory()



    def search_recipes(self):
        #if a list item is selected
        selected=[]
        selection=""
        if self.grid1.children[0].adapter.selection:
            for i in self.grid1.children[0].adapter.selection:
                selected.append(i.text)
            selected=self.nameTaker(selected)
            for j in selected:
                selection=selection +" "+j
            if (selection):
                App_ID = 'cf938db6'
                APP_KEY = '91a43a29d2211953084fcca6b71b005b'
                r = requests.get('https://api.edamam.com/search?q='+selection +'&app_id='+App_ID+'&app_key='+APP_KEY)
                if (r.status_code == 200):
                    data = r.json()
                    global listofrecname
                    listofrecname = []
                    global listofrecs
                    listofrecs = []
                    global recindex
                    recindex = 0
                    global q
                    q = 0
                    for i in data['hits']:
                        data1 = i['recipe']
                        dishName = data1['label']
                        listofrecname.append('Recipe for '+dishName) 
                        recindex+=1
                        # prints ingredients needs to print recipe, popup content box layout including label and lable = data, right arror index + 1, left arrow index -1 if index = 0, left arrow == last element of array vise versa..!! change ingredients line
                        recipeforpop = "" 
                        
                        for recipe in data1['ingredientLines']:
                            recipeforpop+=recipe+'\n'
                        listofrecs.append(recipeforpop)
                        self.current = "recipescreen"
                   

#On submit, pass the data in the spinners for the experation dates, easily done imo, errors could arise in passing from class to class
  
class GroceryLoggerApp(App):

    def build(self):
        self.title = "Gro-Log"
        return MyScreenManager()

GroceryLoggerApp().run()
