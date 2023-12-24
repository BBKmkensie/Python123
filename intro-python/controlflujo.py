if 2 < 5:
    print('2 es menor que 5')

# a == b es igual
# a > b es mayor
# a != b es distinto
# a <= b es menor o igual
# a >= b es mayor o igual

# if 2 == 2:
#     print("2 es igual a 2")
# if 2 == 3:
#     print("2 es igual a 3")
# if 2 > 5:
#     print("2 es mayor a 5")
# if 5 > 2:
#     print("5 es mayor a 2")

# if 2 != 2:
#     print("2 es distinto a 2")
# if 3 != 2:
#     print("3 es distinto a 2")
# if 3 >= 2:
#     print("3 es mayor o igual a 2")
# if 3 >= 3:
#     print("3 es menor o igual a 3")


if 2 > 5:
    # primero se ejecut if y si no es verdad se ejecuta elif
    print('dos es menor a 5')
elif 2 > 5:  # elif se puede repetir todo lo q quiera
    print('2 menor a 5 en elif')
elif 2 < 5:
    print('2 menor a 5 en segundo elif')
else:  # se ejecuta si todo lo anterior es falso
    print('yo me imprimo solo si todo lo anterior evalua en falso')


if 2 > 5:
    # primero se ejecut if y si no es verdad se ejecuta elif
    print('dos es menor a 5')
else:  # se ejecuta si todo lo anterior es falso
    print('yo me imprimo solo si todo lo anterior evalua en falso2')


if 2 < 5:
    print(' if de una linea')  # otra manera de escribir if

print('cuando devuelve true ') if 5 > 2 else print('cuando devuelve false')


if 2 < 5 and 3 > 2:
    # True porque ambas condiciones son verdaderas
    print('ambas devuelven true')

if 2 < 5 and 3 < 2:
    # si una de las  condiciones es falsa no se ejecuta
    print('hay una falsa, esto no se mostrará')


if 1 < 0 or 1 > 0:  # se la evaluacion de la izquierda es true todo es true
    # o ambas true y funciona
    print('una de las dos condiciones devolvió true')


if 1 < 0 or 1 < 0:
    print('amabas falsas no se ejecuta')
