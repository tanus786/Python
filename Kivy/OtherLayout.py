from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout

Window.clearcolor=(1,1,1,1)
Window.size=(360,600)

class MyOtherApp(App):
    def build(self):
        layout = PageLayout()
        btn1 = Button(text="btn1",size_hint=(None,None),width=80)
        btn2 = Button(text="btn2",size_hint=(None,None),width=80)
        # layout = FloatLayout()
        # layout= AnchorLayout(anchor_x="right",anchor_y="bottom")
        # btn = Button(text="btn1",size_hint=(None,None),width=80,pos_hint={"center_x":0.5,"center_y":0.5})
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout
    
MyOtherApp().run()