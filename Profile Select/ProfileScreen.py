from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

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


    def delete_profile(self):
        # If a list item is selected
        if self.profile_list.adapter.selection:

            # Get the text from the item selected
            selection = self.profile_list.adapter.selection[0].text

            # Remove the matching item
            self.profile_list.adapter.data.remove(selection)

            # Reset the ListView
            self.profile_list._trigger_reset_populate()

    def replace_profile(self):
        # If a list item is selected
        if self.profile_list.adapter.selection:

            # Get the text from the item selected
            selection = self.profile_list.adapter.selection[0].text

            # Remove the matching item
            self.profile_list.adapter.data.remove(selection)

            # Get the profile's name from TextInputs
            profile_name = self.profile_name_text_input.text

            # Add the updated data to the list
            self.profile_list.adapter.data.extend([profile_name])

            # Reset the ListView
            self.profile_list._trigger_reset_populate()

class ProfileDBScreen(App):
    def build(self):
        return ProfileDB()

profileScreen = ProfileDBScreen()
profileScreen.run()

