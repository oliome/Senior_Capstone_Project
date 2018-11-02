import kivy
#kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

class ProfileScreen(GridLayout):
	def __init__(self, **kwargs):
		super(ProfileScreen, self).__init__(**kwargs)
		self.cols = 1

		self.newProfile = (Button(text='Add New Profile', font_size=14)) #creates button w/ text
		self.add_widget(self.newProfile)
		self.newProfile.bind(on_press=self.newProfile_Click)

	def newProfile_Click(self,instance):
		box = BoxLayout()

		self.popup = Popup(title='What is your name?',
						   title_align='center',
						   auto_dismiss=False,
						   content=box,
						   size_hint=(None, None),
						   size=(400, 100))


		self.text = (TextInput(multiline=False, font_size=24))
		createButton = (Button(text='Create Profile',size_hint=(.5, 1)))
		cancelButton = (Button(text='Cancel',size_hint=(.3, 1)))
		box.add_widget(self.text)
		box.add_widget(createButton)
		box.add_widget(cancelButton)
		self.text.bind(on_text_validate=self.Create_Click)
		cancelButton.bind(on_press=self.popup.dismiss)
		createButton.bind(on_press=self.Create_Click)
		self.popup.open()


	def Create_Click(self,instance):
		self.cols += 1
		self.remove_widget(self.newProfile)
		newbutton = Button(text=self.text.text, id=self.text.text)
		newbutton.bind(on_press=self.DBscreen)
		self.add_widget(newbutton)
		self.add_widget(self.newProfile)
		self.popup.dismiss()

	def DBscreen(self,instance):
		self.clear_widgets()
		dbScreen.run()






class MyApp(App):

	def build(self):
		self.title = 'Select User Profile'
		return ProfileScreen()


#class DatabaseScreen(App):
#
#	def build(self):
#		self.title = "Your Grocery Inventory"
#		return FloatLayout()


#dbScreen = DatabaseScreen()
#dbScreen.run()

if __name__ == '__main__':
    MyApp().run()
