import os

class user:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    users = []

    def add_user(self):
        self.users.append(self)

    @classmethod
    def get_users(cls):
        return cls.users

    @classmethod
    def login(cls, email, password):
        for user in cls.users:
            if user.email == email and user.password == password:
                return True
        return False

def main():
    print("Bem vindo ao sistema de cadastro de usuários!")
    print("Digite 1 para cadastrar um novo usuário.")
    print("Digite 2 para fazer login.")
    print("Digite 3 para sair.")
    input_option = input(" ")
    match input_option:
        case "1":
            name = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            password = input("Digite sua senha: ")
            new_user = user(name, email, password)
            new_user.add_user()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Usuário cadastrado com sucesso!")
            main()
        case "2":
            email = input("Digite seu email: ")
            password = input("Digite sua senha: ")
            if user.login(email, password):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Olá {user.get_users()[0].name}! Login realizado com sucesso!")
                exit()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Email ou senha incorretos.")
            main()
        case "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Saindo do sistema...")
            exit()

if __name__ == "__main__":
    main()    
