import mysql.connector

# Crea una conexión a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="prueba"
)

# Crea un cursor
cursor = conn.cursor()

#para ver la tabla usuario se ejecuta con resultados = cursor.fetchall() y print

#listar los datos
# cursor.execute('select * from Usuario')

# resultados = cursor.fetchall()

# for fila in resultados:
#     print(fila)
#otra manera de ejecutarlo
# print(resultados)

#para ver definiciones de las tablas
# cursor.execute('show create table Usuario')

# insertar datos
sql = 'insert into Usuario(email, username, edad) values (%s, %s, %s)'
values = ('micorreo@correo.co.nz', 'nombreusuario', 45)

cursor.execute(sql,values)

conn.commit()

#para ejecutar
print(cursor.rowcount)


