from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.clock import mainthread

class MainMenu(Screen):
    name = StringProperty('main_menu')
   
class OtherMenu(Screen):
    name = StringProperty('other_menu')
    added_buttons = ListProperty([])
         
class RootWidget(Widget):
    state = StringProperty('set_main_menu_state')
    screen_manager = ObjectProperty(None)
    grid = GridLayout(cols = 6)
    my_list = ['New Profile +']
    
    

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

    def on_state(self, instance, value):
        if value == 'main_menu':
            self.screen_manager.current = 'main_menu'

    def set_state(self, state):
        global my_list
        if state == 'main_menu':
            self.screen_manager.current = 'main_menu'
            #self.clear_widgets()
            #w = MainMenu()
            #for i in my_list:
                #self.add_widget(Button(text=i))
            
            for i in my_list:
               # button = Button(text="B_" + str(i))
                self.add_widget(Button(text=i))
   
            return my_list
        if state == 'other_menu':
            self.screen_manager.current = 'other_menu'
    
    

my_list = ['New Profile +']
class TestApp(App):

	

	def build(self):
		pass

	def Create_Click(self, name):
		global my_list
		my_list.append(name)		
		print(my_list)
		


	

if __name__ == '__main__':
    TestApp().run()
