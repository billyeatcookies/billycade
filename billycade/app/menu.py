class Menu:
    def __init__(self, app):
        self.items = ['Tic tac toe']

    def show(self):
        n = 0
        print()

        for n, i in enumerate(self.items):
            print(f"{n}.", " - ".join(i))
        
        print(f"\n{n+1}. Exit"
