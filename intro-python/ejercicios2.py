# multiplicar dos  numeros sin uusar el simbolo de multiplicacion
a = 4
b = 8
resultado = 0

for x in range(a):
    resultado += b

print(resultado)
# ingresar nombre y apellido e imprimirlo al reves

nombre = 'Nicolas'
apellido = 'Feliz'

concatenacion = nombre + ' ' + apellido

print(concatenacion[:: -1])
# escribir una función que encuentre el elemento menor de una lista
lista = [1, 2, 5, 3, 55, -24, -13]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('menor', menor)


# escribir una función que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3

def calcularVolumen(r):
    return 4/3 * 3.14 * r ** 3


resultado = calcularVolumen(6)
print(resultado)

# escribir una función que indique si el usuario es mayor de edad


def esMayor(usuario):
    return usuario.edad > 17


class Usuario:
    def __init__(self, edad):
        self.edad = edad


usuario = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

# print(resultado1, resultado2)

# escribir una función que indique si un numero es par o impar


def esPar(n):
    return n % 2 == 0


resultado = esPar(11)
# print(resultado)


# escribir una función que cuantas vocales tienen una palabra
palabra = 'ChanchitoFeliz'
vocales = 0
for x in palabra:
    y = x.lower()  # para poder contar las mayusculas
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

# print(vocales)


# escribir una aplicacion que reciba una cantidad infinita de numeros hasta
# decir basta, luego que devuelva la suma de los numeros ingresados
# lista = []
# print('Ingrese numeros y para salir escriba "basta"')
# while True:
#     valor = input('Ingrese valor: ')
#     if valor == 'basta':
#         break
#     else:
#         try:
#             valor = int(valor)
#             lista.append(valor)
#         except:
#             print('Dato invalido')
#             exit()

# resultado = 0
# for x in lista:
#     resultado += x

# print(resultado)

# escribir una funcion que reciba nombre y apellido  y los vaya agregando a
# un archivo

def agregandoNombreAArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()


agregandoNombreAArchivo('Chanchito', 'Feliz')
