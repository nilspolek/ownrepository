import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text="Firstname: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Lastname: "))
        self.lastname = TextInput(multiline=False)
        self.add_widget(self.lastname)

        self.add_widget(Label(text="E-Mail: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ =="__main__":
    MyApp().run()