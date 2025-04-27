from view import User_menu


class Controller:
    def __init__(self):
        self.user_menu = User_menu()

    def logic(self):
        self.user_menu.hello()
