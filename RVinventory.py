from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.properties import ListProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from datetime import datetime
import kivy
from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')

item_name = ['Milk','Eggs','Bread','Cookies']
item_expiration = ['12/25/2018','12/25/2018','12/25/2018','12/25/2018']
item_barcode = ['123456789','123456789','123456789','123456789']


deselected_list = item_expiration[:]
selected_list = []

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''

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
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view.
        and add/remove items from lists
        '''
        self.selected = is_selected
        if self.selected and self.text in item_name:
            selected_list.append(self.text)
            item_name.remove(self.text)
            print(selected_list)
        elif not self.selected and self.text in selected_list:
            item_name.append(self.text)
            selected_list.remove(self.text)
            print(item_name)
        if self.selected and self.text in item_expiration:
            selected_list.append(self.text)
            item_expiration.remove(self.text)
            print(selected_list)
        elif not self.selected and self.text in selected_list:
            item_expiration.append(self.text)
            selected_list.remove(self.text)
            print(item_expiration)
        if self.selected and self.text in item_barcode:
            selected_list.append(self.text)
            item_barcode.remove(self.text)
            print(selected_list)
        elif not self.selected and self.text in selected_list:
            item_barcode.append(self.text)
            selected_list.remove(self.text)
            print(item_barcode)

class RV1(RecycleView):
    # this needs to be updated every time any label is selected or deselected
    def __init__(self, **kwargs):
        super(RV1, self).__init__(**kwargs)
        self.data = ([{'text': str(row)} for row in sorted(item_name)]
                     + [{'text': str(row)} for row in sorted(selected_list)])

class RV2(RecycleView):
    # this needs to be updated every time any label is selected or deselected
    def __init__(self, **kwargs):
        super(RV2, self).__init__(**kwargs)
        self.data = ([{'text': str(row)} for row in sorted(item_expiration)]
                     + [{'text': str(row)} for row in sorted(selected_list)])

class RV3(RecycleView):
    # this needs to be updated every time any label is selected or deselected
    def __init__(self, **kwargs):
        super(RV3, self).__init__(**kwargs)
        self.data = ([{'text': str(row)} for row in sorted(item_barcode)]
                     + [{'text': str(row)} for row in sorted(selected_list)])


class Screen(BoxLayout):
    now = datetime.now()

    def nowdate(self):
        return self.now.strftime('%d')

    def nowmonth(self):
        return self.now.strftime('%m')

    def nowyear(self):
        return self.now.strftime('%y')

    def nowhour(self):
        return self.now.strftime('%H')

    def nowminute(self):
        return self.now.strftime('%M')

Builder.load_string('''
#:import datetime datetime

<Screen>:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: 30
        Button:
            text: 'Item Name'
        Button:
            text: 'Expiration Date'
        Button
            text: 'Barcode/UPC Number'
    GridLayout:
        cols: 3
        RV1:
            viewclass: 'SelectableLabel'
            SelectableRecycleBoxLayout:
                default_size: None, dp(45)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
                multiselect: True
                touch_multiselect: True
        RV2:
            viewclass: 'SelectableLabel'
            SelectableRecycleBoxLayout:
                default_size: None, dp(45)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
                multiselect: True
                touch_multiselect: True
        RV3:
            viewclass: 'SelectableLabel'
            SelectableRecycleBoxLayout:
                default_size: None, dp(45)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
                multiselect: True
                touch_multiselect: True
    Button:
        size_hint_y: None
        height: 30

<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size

''')

class TestApp(App):
    def build(self):
        return Screen()

if __name__ == '__main__':
    TestApp().run()