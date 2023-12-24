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

# Recupera los resultados
resultados = cursor.fetchall()

# Cierra el cursor y la conexión a la base de datos
# cursor.close()
# conn.close()

# Procesa los resultados
print(resultados)