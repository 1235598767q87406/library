from model import read_user, write_user
from user import User
from view import User_menu


class Controller:
    def __init__(self):
        self.user_menu = User_menu()

    def logic(self):
        otvet = self.user_menu.menu()

        if otvet == 1:
            name = self.user_menu.regestration()
            new_user = User(name)
            print(f"новый пользователь {new_user.name} создан")
        elif otvet == 2:
            print("2")
        elif otvet == 3:
            print("3")
        else:
            print("ошибка")
