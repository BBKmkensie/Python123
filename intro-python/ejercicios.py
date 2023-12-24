# dato = input('Ingese dato:')

# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'fragones']

# if lista.count(dato) > 0:
#     print("El dato existe", dato)
# else:
#     print('El dato no existe:(', dato)
# # ----------------------------------------------

# primero = input('Ingrese primer número: ')
# segundo = input('Ingrese segundo número: ')

# primerNumero = int(primero)
# segundoNumero = int(segundo)
# print(primerNumero + segundoNumero)

# calculadora

primero = input('Ingrese primer número: ')
try:  # intenta ejecutar la logica q se le entrega
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingrese segundo número: ')
try:  # intenta ejecutar la logica q se le entrega
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

# if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
#     print('Ingresa mal un dato, prueba de nuevo solo con números')
# else:
#     print(primero + segundo)

# Agregando mas operaciones
simbolo = input('ingrese operación: ')

if simbolo == '+':
    print('Suma:', primero + segundo)
elif simbolo == '-':
    print('Resta:', primero - segundo)
elif simbolo == '*':
    print('Multiplicación:', primero * segundo)
elif simbolo == '/':
    print('División:', primero / segundo)
else:
    print('El símbolo ingresado no es válido')
