# if 6 > 3:
#     print('5 es mayor a 3')

# if 3 > 3:
#     print('Esto no se va a imprimir')

# # Acá va un comentario
# if 5 > 3:  # Acá va un comentario
#     print('5 es mayor a 3')


# varaibles
x = 5
y = 'chanchito feliz'

print(x, y)

correo = 'chachito@feliz.com'

print(correo)

_mi_var = 'chanchito'
MIVAR23 = 'chanchito'
a, b, c = 'Lala', 'Lele', 'Lili'

# print(a, b, c)

valor1 = valor2 = valor3 = 'Chanchito Feliz'
# print(valor1, valor2, valor3)

# concatenacion
inicio = 'hola'
final = 'mundo'
# print(inicio + final)  # sin espacio
# print(inicio, final)  # con espacio


# string y  numeros
palabra = 'hola mundo'  # string
oracion = "hola mundo comilla doble"  # string

# numeros
entero = 20
conDecimales = 20.2  # float
complejos = 1j

# print(palabra, oracion, entero, conDecimales, complejos)


# listas
# lista = [1, 2, 3]  # lista con corchetes
lista = ['Hola', 'Mundo', 'Chanchito feliz']
lista2 = lista.copy()
lista.append('chachito triste')  # agrega alemento a la lista
# list.clear()  # limpia la lista
# print(lista, lista2.count(3))  # el count te cuanta
# print(len(lista), len(lista2))  # el len te cuanta los elementos lista

largoLista = len(lista)
largoLista2 = len(lista2)

# print(largoLista, largoLista2)

# print(lista[0])

# lista.pop()  # elimina el ultimo elemento de nuestra lista
# lista.pop()

# lista.remove('Hola') #elimina un elemento por su valor

lista.reverse()  # tener los mismos tipos de datos si se quiere ordenar
# print(lista)

tupla = ('hola', 'mundo' 'somos', 'tupla')  # no se pueden modificar
listaDeTupla = list(tupla)  # se pasa de tupla a lista para poder modifica
listaDeTupla.append('chanchito')  # su cpntenido
# print(listaDeTupla)

rango = range(6)  # va del 0 al 6
# print(rango)

# diccionarios
diccionario = {
    "nombre": "chanchito feliz",
    "raza": "Persa",
    "edad": 5
}
# print(diccionario)
# print(diccionario['nombre'])
# print(diccionario['raza  '])

# print(diccionario.get('nombre'))
diccionario['nombre'] = 'Fluffy'
# print(diccionario)


# print(len(diccionario))


diccionario['ronronea'] = 'Si'  # cambia valores
# print(diccionario)
# diccionario.pop('ronronea')

# diccionario.popitem()  # elimina el ultimo valor q ingresaste
copiaGatito = diccionario.copy()
# copiaGatito = dict(diccionario)
# del diccionario['ronronea']  # elimina los elementos del diccionario
diccionario.clear()
# print(diccionario, copiaGatito)
# diccionario
fluffy = {
    "nombre": "Fluffy",
    "edad": 4
}

mamba = {
    "nombre": "Black Mamba",
    "edad": 12
}

gatitos = {
    "Fluffy": fluffy,
    "Mamba":  mamba

}
print(gatitos)

# otra forma de crear diccionarios

perritos = dict(nombre="Chanchito Feliz", edad=6)
print(perritos)


# boolean
verdadero = True
falso = False

print(verdadero, falso)
