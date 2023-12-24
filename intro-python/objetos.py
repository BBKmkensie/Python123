# la clase es como el plano de una casa y la casa construida los objetos
# class Usuario:  # primera letra en mayuscula y la instancia en minuscula
#     nombre = 'Felipe'
#     apellido = 'Feliz'


# usuario = Usuario()
# usuario2 = Usuario()

# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

# la clase con __init__ y self
# class Usuario:
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido


# # el nombre y apellido lo obtine de lso parametros
# usuario = Usuario('Felipe', 'Feliz')
# usuario2 = Usuario('Chanchito', 'Feliz')

# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)
# nustras clases son el plano de la casa o los usuarios, los objetos
# son instancias de estos planos los usuarios q ya existen la casa construida
# init se ejecuta siempre al crear una de estas clases
# self hace referencia a una instancia q creamos

# con saludos
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola, mi nombre es', self.nombre, self.apellido)


class Admin(Usuario):
    def superSaludo(self):
        print('Hola!, me llamo,', self.nombre, 'y soy administrador')


# usuario = Usuario('Felipe', 'Feliz')
# # usuario2 = Usuario('Chanchito', 'Feliz')

# usuario.saludo()
# usuario.nombre = 'Chanchito'
# usuario.saludo()

# # # eliminar usuario
# # del usuario.nombre
# # del usuario
# # print(usuario)

# herencia
# Permite que una clase (llamada clase
# hija o subclase) herede atributos y métodos de otra clase (llamada clase padre o superclase).
# admin = Admin('Super', 'Feliz')
# admin.saludo()
# admin.superSaludo()


class Animal:
    def __init__(self, nombre, onomatopeya,):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)


class Gato(Animal):
    tipo = 'gato'

    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola, soy un gato extendido!')


class Perro(Animal):
    tipo = 'perro'

    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('instanciando un perro')


class Canario(Animal):
    tipo = 'canario'


gato = Gato('Fluffy', 'maullido')
gato.saludo()


perro = Perro('Firulais', 'ladrido')
perro.saludo()

canariorro = Canario('Piolin', 'silvido')
canariorro.saludo()
