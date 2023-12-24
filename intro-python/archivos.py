# # c = open('chanchito.txt')
# c = open('chanchito.txt', 'a')
# # a es = a apennd permiso para escribir
# # w para modificar el archivo, # lee una solo linea
# # x # para crear archivos
# print(c.read())
# # print(c.readline())  # lee linea a linea

# # for x in c:  # para no colocar read otra manera de leer
# #     print(x)

# # c.write('\nagregamos una nueva linea a nuestro archivo')
# # # \n para una nueva linea
# # c.close()  # para cerrar el archivo

# x = open('chanchito.txt')

# print(x.read())

# para eliminar el archivo o carpeta
import os
if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
else:
    print('El archivo no existe')
# os elimima carpeta y archivos
os.rmdir('micarpeta')
