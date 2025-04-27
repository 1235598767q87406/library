class User_menu:
    def __init__(self):
        pass

    def menu(self):
        print("здравствуйте, это библиотека")
        print("что вы хотите сделать?\n1) Зврегестрироваться")
        print("2) Вять книгу\n3) Сдать книгу")
        vb = int(input("ваш ответ: "))
        return vb
    
    def regestration(self):
        name = input("введите своё имя: ")
        return name
