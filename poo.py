class Member:
    height = None
    imc = None
    name = None

    def __init__(self, name):
        self.name = name

    def register(self):
        print("Usuario registrado")

    def welcome(self):
        print(f"Hola, bienvenido {self.name}")

rafa = Member("Rafa")

rafa.height = 172
rafa.imc = 15
print(rafa.height)
print(rafa.imc)
rafa.register()
print(type(rafa))
#rafa.name = "Rafael"
rafa.welcome()

billy = Member("Billy")
#billy.name = "Billy"
billy.welcome()



