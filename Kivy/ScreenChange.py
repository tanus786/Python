from kivy.app import App 
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label



Window.clearcolor = (1, 1, 1, 1)
Window.size=(320,520)
class ScreenChangeApp(App):
    def build(self):
        pass
    
ScreenChangeApp().run()