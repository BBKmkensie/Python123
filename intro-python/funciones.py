# funciones

def miFuncion():
    print("Mi primera función!")


# miFuncion()

# def imprimeDato(nombre, apellido):  # argumento
#     print('Mi argumento es', nombre, apellido)


# imprimeDato('Chanchito', 'bella')


def imprimeDato(*nombre):  # * mas de unargumento
    # sin [1] arroja todos los valoren en tupla
    print('Mi nombre completo  es', nombre[1])


# imprimeDato('Chanchito', 'Feliz', 'lala', 'lele')  # me los pasa como una tupla

# otra manera de aceder a los argumentos
def nombreCompleto(apellido, nombre):
    print(nombre, apellido)


# nombreCompleto(nombre='Chanchito', apellido='Feliz')

# otra manera con kwargs
def nombreCompleto2(**kwargs):  # argumento por llave
    print(kwargs['nombre'], kwargs['apellido'])


# nombreCompleto2(nombre='Chanchito', apellido='Feliz')


def miFuncion2(argumento='Chanchito'):
    print(argumento)


# miFuncion2('Batman')  # imprime Batman
# miFuncion2()  # imprime Chanchito

def miFuncionLista(lista):
    for el in lista:
        print(el)


miFuncionLista(['Chanchito', 'Feliz'])

# otra funcion


def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ''
    return i


# nombre = concatenaNombres(['Chanchito', 'Feliz'])
# print(nombre)


# recursividad
def recursion(i):
    if (i < 1):
        return i
    print(i)
    recursion(i - 1)


recursion(6)
