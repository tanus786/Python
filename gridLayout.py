from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size=(360,600)
class MyApp(App):
    def build(self):
       layout = GridLayout(rows=2,col_force_default=True,col_default_width=200)
       
       btn1 = Button(text="btn1")
       btn2 = Button(text="btn2")
       btn3 = Button(text="btn3")
       btn4 = Button(text="btn4")
       
       layout.add_widget(btn1)
       layout.add_widget(btn2)
       layout.add_widget(btn3)
       layout.add_widget(btn4)

       return layout
    
MyApp().run()