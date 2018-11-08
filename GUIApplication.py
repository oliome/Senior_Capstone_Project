from http://kivy.app  import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from http://kivy.properties  import ListProperty, ObjectProperty
from kivy.uix.listview import ListView
from random import shuffle
my_list = ['Add New Profile']

Builder.load_string('''

#: import Button kivy.uix.button.Button

<MyScreenManager>:
    box2: box2
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
        FloatLayout:
            Button:
                text: "Database Table Here"
                pos_hint: {"center_x": .5, "center_y": .5}   
                font_size: 32
                color: 0, 0, 0, 1
                background_normal: 'grey.jpg'
                background_down: ''
                background_color: .88, .88, .88, 1
                size_hint: .7, .7

            Button:
                text: "Delete"
                pos_hint: {"center_x": .2 , "center_y": .1}
                font_size: 16
                color: 0, 0, 0, 1
                background_normal: 'grey.jpg'
                background_down: ''
                background_color: .88, .88, .88, 1
                size_hint: .1, .1
            Button:
                text: "Back"
                pos_hint: {"top": 1}
                font_size: 16
                color: 0, 0, 0, 1
                on_press: root.current = "screen2"
                background_normal: 'grey.jpg'
                background_down: ''
                background_color: .88, .88, .88, 1
                size_hint: .1, .1

            Button:
                text: "Your Grocery Inventory"
                pos_hint: {"center_x": .5, "top": 1}
                font_size: 16
                color: 0, 0, 0, 1
                background_normal: 'grey.jpg'
                background_down: ''
                background_color: .88, .88, .88, 1
                size_hint: .2, .1

            Button:
                text: "Search Recipes"
                pos_hint: {"center_x": .38, "center_y": .1}
                font_size: 16
                color: 0, 0, 0, 1
                background_normal: 'grey.jpg'
                background_down: ''
                background_color: .88, .88, .88, 1
                size_hint: .2, .1

''')

class MyScreenManager(ScreenManager):

    box2 = ObjectProperty(None)
    added_buttons = ListProperty([])

    def update_buttons(self,*args):
        
        #self.box2.clear_widgets()
        shuffle(self.added_buttons)

        for i in self.added_buttons:
            
            self.box2.add_widget(i)
            i.bind(on_press=lambda a:self.auth(i.text))
            
        self.added_buttons[:] = []

    def auth(self,instance):
        self.current = "screen3" 
        print(instance)

class MyApp(App):

    def build(self):

        return MyScreenManager()

MyApp().run()
