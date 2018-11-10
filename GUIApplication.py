from kivy.app  import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties  import ListProperty, ObjectProperty
from kivy.uix.listview import ListView
from kivy.uix.button import Button
from random import shuffle
from functools import partial
my_list = ['Zack','Ollie','Reyhan','Aaron']

Builder.load_string('''

#: import Button kivy.uix.button.Button

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
                    root.transition.direction = "right"
                    root.current = "screen2"


''')
#instance is the last button added
class MyScreenManager(ScreenManager):
    added_buttons = ListProperty([])
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
        

  
class MyApp(App):

    def build(self):

        return MyScreenManager()

MyApp().run()
