from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size=(360,600)
class MyLayoutApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical",spacing=10,padding=100)

        btn1 = Button(text="btn1")
        btn2 = Button(text="btn2")

        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout
    
MyLayoutApp().run()

