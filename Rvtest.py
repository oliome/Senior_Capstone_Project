from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

Builder.load_string('''
<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
<RV>:
    viewclass: 'SelectableLabel'
    RecycleGridLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        cols: 3
        
''')

class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        print(self.text)
       

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
     

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        mylist =['Great Value 2% Milk','11/10/18','078742022871','Tyson Frozen Chicken','12/25/18','078742022871','JIF Peanut Butter 40oz','12/25/18','078742022871','Chipotle Tabasco','12/25/18','078742022871']
        self.data = [{'text': str(x)} for x in mylist]
       


class TestApp(App):
    def build(self):
        return RV()

if __name__ == '__main__':
    TestApp().run()
