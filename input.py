from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.size=(360,600)
class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout,self).__init__(**kwargs)
        self.cols=1

        self.add_widget(Label(text="Enter Your Name"))
        self.name=TextInput(multiline= False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Enter Your Email"))
        self.email=TextInput(multiline= False)
        self.add_widget(self.email)

        self.submit= Button(text="Submit")
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        print(self.name.text)
        print(self.email.text)

        self.add_widget(Label(text=f"Hello{self.name.text} your email is {self.email.text}"))

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
MyApp().run()



# class MyApp(App):
#     def build(self):
        # layout= GridLayout(cols=1,
        # row_force_default=True,
        # row_default_height=50,
        # padding = 40,
        # spacing=20)
        
        # layout=BoxLayout(orientation="vertical",padding = 150,spacing=30)

        # self.name = TextInput(text="Enter your name")
        # self.password = TextInput(text="Enter your password")
        # self.login = Button(text="Login", on_press=self.loginbtn)

        # layout.add_widget(self.name)
        # layout.add_widget(self.password)
        # layout.add_widget(self.login)

#         return layout
    
#     def loginbtn(self,obj):
#         print(self.name.text)
#         print(self.password.text)
            
# MyApp().run()