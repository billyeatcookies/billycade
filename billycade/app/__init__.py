from .menu import Menu


class App:
    def __init__(self, *args, **kwargs):
        self.menu = Menu(self)
    
    def launch(self):
        print("welcome to arcade!")
        self.menu.show()
