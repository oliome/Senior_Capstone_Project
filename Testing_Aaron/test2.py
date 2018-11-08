from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.listview import ListItemButton
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
from kivy.properties import StringProperty

profile_name_text_input = ObjectProperty()
profile_list = ObjectProperty()


Builder.load_string('''
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton



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

#############################################################################
<ProfileScreen>:


    HeaderButton:
        text: "Profile Select"
        pos_hint: {"center_x": .5, "top": 1}

    BoxLayout:
        size_hint: .9,.05
        pos_hint: {"center_x": .5, "top": .85}
        Label:
            text: "Select a profile below or enter a new profile name:"
        TextInput:
            id: profile_name

    BoxLayout:
        size_hint_y: .1
        pos_hint: {"top": .75}
        Button:
            text: "Add New Profile"
            size_hint_x: 15
            on_press: root.create_profile()
        Button:
            text: "Select Profile"
            size_hint_x: 15
            on_press:
                app.root.transition.direction = "left"
                app.root.current = "menu_screen"

    GridLayout:
        cols: 1
        pos_hint: {"top": .65}
        #padding: [100,0,100,100]


    BoxLayout:
        Button:
            text: "Delete Selected Profile"
            size_hint_y: .05
            on_press: root.delete_profile()
#############################################################################
<MenuScreen>:
    HeaderButton:
        text: "Main Menu"
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
                app.root.transition.direction = "up"
                app.root.current = "additem_screen"
        Button:
            text: "View Food Inventory"
            on_press:
                app.root.transition.direction = "left"
                app.root.current = "inventory_screen"
    GridLayout:
        cols: 1
        size_hint: .2, .1
        pos_hint: {"center_x": .5}
        Button:
            text: "Profile Select"
            on_press:
                app.root.transition.direction = "right"
                app.root.current = "profile_screen"
#############################################################################
<RV>:
    FloatLayout:
        StandardButton:
            text: "Back to Main Menu"
            pos_hint: {"top": .9}
            on_press:
                app.root.transition.direction = "right"
                app.root.current = "menu_screen"

        HeaderButton:
            text: "Your Food Inventory"
            pos_hint: {"center_x": .5, "top": 1}

        GridLayout:
            cols: 3
            #padding: 100
            size_hint_y: .1
            pos_hint: {"top": .8}
            Button:
                text: "Item Name"
                #on_press:
                    #app.root.
            Button:
                text: "Expiration Date"
            Button:
                text: "Barcode/UPC Number"


        GridLayout:
            cols: 1
            #[from left,from top,from right,from bottom]
            padding: [0,0,0,300]
            pos_hint: {"top": .7}
            viewclass: 'InventoryScreen'
            SelectableRecycleGridLayout:
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
                multiselect: True
                touch_multiselect: True
                cols: 3

        MiniButton:
            text: "Delete"
            pos_hint: {"center_x": .2 , "center_y": .1}

        StandardButton:
            text: "Search Recipes"
            pos_hint: {"center_x": .38, "center_y": .1}

        MiniButton:
            text: "Add"
            pos_hint: {"center_x": .56, "center_y": .1}
            on_press:
                app.root.transition.direction = "up"
                app.root.current = "additem_screen"
#############################################################################
<AddItemScreen>:
    FloatLayout:
        StandardButton:
            text: "Back to Inventory"
            pos_hint: {"top": .9}
            on_press:
                app.root.transition.direction = "down"
                app.root.current = "inventory_screen"

        HeaderButton:
            text: "Add Item"
            pos_hint: {"center_x": .5, "top": 1}

        Button:
            text: "Scan Barcode or Enter Barcode Number"
            pos_hint: {"center_x": .5, "top": .8}
            size_hint: .5,.05
        TextInput:
            text: "enter barcode number here"
            pos_hint: {"center_x": .5, "top": .75}
            size_hint: .5,.05
        Button:
            text: "Select Expiration Date (optional)"
            pos_hint: {"center_x": .5, "top": .7}
            size_hint: .5,.05
        Button:
            text: "Interactive Calendar Here"
            pos_hint: {"center_x": .5, "top": .65}
            size_hint: .5,.4
            on_press:
                root.show_calendar()

        MiniButton:
            text: "Submit"
            pos_hint: {"center_x": .2 , "center_y": .1}

        MiniButton:
            text: "Other"
            pos_hint: {"center_x": .33, "center_y": .1}

        MiniButton:
            text: "Cancel"
            pos_hint: {"center_x": .46, "center_y": .1}
            on_press:
                app.root.transition.direction = "down"
                app.root.current = "inventory_screen"
''')

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

items = ["Great Value 2% Milk","12/25/18","078742022871","Tyson Frozen Chicken","JIF Peanut Butter 40oz","Chipotle Tabasco","Kraft Cheddar Cheese","Lay's Sour Cream and Onion Chips","Great Value 2% Milk","Tyson Frozen Chicken","JIF Peanut Butter 40oz","Chipotle Tabasco","Kraft Cheddar Cheese","Lay's Sour Cream and Onion Chips","Great Value 2% Milk","Tyson Frozen Chicken","JIF Peanut Butter 40oz","Chipotle Tabasco","Kraft Cheddar Cheese","Lay's Sour Cream and Onion Chips"]

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''

class InventoryScreen(RecycleDataViewBehavior, Label):
    def sort_items(self):
        pass

    def sort_dates(self):
        pass



    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(InventoryScreen, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(InventoryScreen, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in items]

class AddItemScreen(Screen):
    pass


class test2(App):
    def build(self):
        self.title = "test2"
        screen_manager = RV()

        return RV()


my_app = test2()
my_app.run()
