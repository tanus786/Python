from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MyApp(App):
    def build(self):
        return Image(source='demo.jpeg',size_hint=(None,None),width=200,height=100,pos_hint={"center_x": 0.5, "center_y": 0.5})
    
MyApp().run()