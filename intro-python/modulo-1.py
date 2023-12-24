# llamamos al modulo
import modulos as xs  # con el as le cambiamos el nombre al modulo
from camelcase import CamelCase
print(xs.mascotas)
xs.saludo('Nicolas')

c = CamelCase()
s = 'esta oración necesita CamelCase!'

camelcased = c.hump(s)
print(camelcased)

# # from modulos import saludo, mascotas
# print(mascotas)
# saludo('Nicolas')
