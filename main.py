from kivy.app import from kivymd.app import MDApp

class MyApp(MDApp):
    def build(self):
        return 

if __name__=="__main__":
    MyApp().run()
from kivy.uix.lable import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello world')
    
if __name__ == '__main__':
    MyApp().run()