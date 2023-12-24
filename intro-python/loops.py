# loop while es algo q se va a repetir y repetir
# hasta q se cumpla el valor de salida
# i = 0

# while i < 5:
#     print(i)
#     if i == 3:
#         # break # break detiene la ejecucion del while
#         continue  # se saltara la ejecucion del i +1 y simpre sera un 3 infinito
#     i += 1

# otra manera para ejecutar continue
# i = 0

# while i < 5:
#     i += 1
#     if i == 3:
#         # break # break detiene la ejecucion del while
#         continue  # se saltara la ejecucion del i +1 y simpre sera un 3 infinito
#     print(i)


# foor loops

# usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']  # lista

# for usuario in usuarios:
#     print(usuario)

# usuario = 'Chanchito Feliz'

# for c in usuario:  # deletrea la lista usuario
#     print(c)

# usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']

# for usuario in usuarios:
#     if usuario == 'roberto': # los dice todos antes de roberto
#         break
#     print(usuario)


# usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']

# for usuario in usuarios:
#     if usuario == 'roberto':  # se salta a roberto
#         continue
#     print(usuario)

# for x in range(3, 30, 5):  # te inprime del 0 al 6, con 1, 6 del 1 al 6
#     print(x)  # 3, 30, 3 va en 3 en 3
# else:
#     print('Hemos terminado!!')


# usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']

# edades = [24, 25, 26, 35] # un for dentro de otro for

# for usuario in usuarios:
#     for edad in edades:
#         print(usuario, edad)
