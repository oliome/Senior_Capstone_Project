from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<BigButton@Button>:
    font_size: 32
    color: 0, 0, 0, 1

    background_normal: 'grey.jpg'
    background_down: ''
    background_color: .88, .88, .88, 1
    size_hint: .7, .7

<MiniButton@Button>:
    font_size: 16
    color: 0, 0, 0, 1

    background_normal: 'grey.jpg'
    background_down: ''
    background_color: .88, .88, .88, 1
    size_hint: .1, .1

<StandardButton@Button>:
    font_size: 16
    color: 0, 0, 0, 1

    background_normal: 'grey.jpg'
    background_down: ''
    background_color: .88, .88, .88, 1
    size_hint: .2, .1

<FloatLayout>:
    MiniButton:
        text: "Back"
        pos_hint: {"top": 1}
        on_press:
            root.manager.transition.direction = "left"
            root.manager.transition.duration = 1
            root.manager.current = "profile_screen"

    StandardButton:
        text: "Your Grocery Inventory"
        pos_hint: {"center_x": .5, "top": 1}

    MiniButton:
        text: "Delete"
        pos_hint: {"center_x": .2 , "center_y": .1}

    StandardButton:
        text: "Search Recipes"
        pos_hint: {"center_x": .38, "center_y": .1}

    MiniButton:
        text: "Add"
        pos_hint: {"center_x": .56, "center_y": .1}

    BigButton:
        text: "Database Table Here"
        pos_hint: {"center_x": .5, "center_y": .5}
""")

class ProfileScreen(Screen):
    pass

class DatabaseScreen(Screen):
    pass

screen_manager = ScreenManager()

screen_manager.add_widget(ProfileScreen(name="profile_screen"))
screen_manager.add_widget(DatabaseScreen(name="database_screen"))

class ProfileListButton(ListItemButton):
    pass

class ProfileDB(BoxLayout):
    profile_name_text_input = ObjectProperty()
    profile_list = ObjectProperty()

    def create_profile(self):
        # Get the profile's name from TextInputs
        profile_name = self.profile_name_text_input.text

        # Add to ListView
        self.profile_list.adapter.data.extend([profile_name])

        # Reset the ListView
        self.profile_list._trigger_reset_populate()

    #def view_database(self):
     #   if self.profile_list.adapter.selection:

    def delete_profile(self):
        # If a list item is selected
        if self.profile_list.adapter.selection:

            # Get the text from the item selected
            selection = self.profile_list.adapter.selection[0].text

            # Remove the matching item
            self.profile_list.adapter.data.remove(selection)

            # Reset the ListView
            self.profile_list._trigger_reset_populate()

class ProfileScreen(App):
    def build(self):
        return ProfileDB()

profileScreen = ProfileScreen()
profileScreen.run()

