from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.textinput import Label

class MainMenu(Screen):
	name = StringProperty('main_menu')
	



class OtherMenu(Screen):
	name = StringProperty('other_menu')

class RootWidget(Widget):
	state = StringProperty('set_main_menu_state')
	screen_manager = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(RootWidget, self).__init__(**kwargs)

	def on_state(self, instance, value):
		if value == 'main_menu':
			self.screen_manager.current = 'main_menu'

	def set_state(self, state):
		if state == 'main_menu':
			self.screen_manager.current = 'other_menu'
		if state == 'other_menu':
			self.screen_manager.current = 'main_menu'


class TestApp(App):

	def build(self):
		pass

	def Create_Click(self):
		print (self.ids.profilescene.cols)
		self.ids.profilescene.cols = self.ids.profilescene.cols + 1
		self.ids.profilescene.remove_widget(self.ids.profilebutton)
		self.ids.profilescene.newbutton = Button(text=self.ids.textinput.text)
		self.ids.profilescene.add_widget(self.ids.profilescene.newbutton)
		#onbind new button to switch scenes
		self.add_widget(self.ids.profilebutton)
		self.ids.popup.dismiss()

if __name__ == '__main__':
	TestApp().run()
