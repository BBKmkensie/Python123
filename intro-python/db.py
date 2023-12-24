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

# Ejecuta tu consulta SQL
consulta = "SELECT * FROM Usuario"
cursor.execute(consulta)

#fetchall(devuelve toda las instancia en la base de datosy se lo asigna a la variable designada)
# Recupera los resultados
resultados = cursor.fetchall()

#nos devuelve el primer elemento encontrado
# resultados = cursor.fetchone()

# Cierra el cursor y la conexión a la base de datos
# cursor.close()
# conn.close()

# Procesa los resultados en fila
for fila in resultados:
    print(fila)

#para columna simplemnte
# print(resultados)