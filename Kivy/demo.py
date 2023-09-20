from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)

class ButtonApp(App):
    def build(self):
        return Button(
            text="Hello",
            size_hint=(0.2, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size="20sp",
            on_press=self.btn_click,
        )
    
    def btn_click(self,btn):
        print("Button Clicked")
        
ButtonApp().run() 



# class DemoApp(App):
#     def build(self):
#         label = Label(text="Hello World",font_size="120sp",italic = True,color=(1,0,0,1))
#         btn = Button(text="Hello")
#         return label
    
# DemoApp().run() 

