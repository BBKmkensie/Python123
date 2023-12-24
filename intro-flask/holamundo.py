from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

#mostrando datos desde la base de datos
import mysql.connector

#con esto ya tenemos la conecion a mysql
midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="prueba"
)

#ahora ontendremos el cursor
cursor = midb.cursor(dictionary=True)
@app.route('/')
def index():
    return 'hola mundo'

# puedes pasarle datos atraves de la url
# @app.route('/lala/<usuario>')
# def lala(usuario):
#     return 'lala' + usuario

# @app.route('/post/<post_id>')
# def lala(post_id):
#     return 'El id del post es: ' + post_id

#Metodos HTTP
# GET, POST, PUT se utiliza para reemplazar un recurso , PATH realiza la misma accion q put, se ocupa para actualizar parcialmente un recurso , DELETE
# @app.route('/post/<post_id>', methods=['GET', 'POST'])
# def lala(post_id):
#     return 'El id del post es: ' + post_id

# yo puedo decidir dentro de un mismo metodo que porcion de codigo ejecutar get o post
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
    if request.method == 'GET':
        return 'El id del post es:' + post_id
    else:
        return 'Este es otro metodo y no GET'
    
#se puede dejar el get y post en una funcion o separarlo en dos funciones, recomendable en 1
# @app.route('/post/<post_id>', methods=['GET'])
# def lala(post_id):
#     return 'El id del post es: ' + post_id

# @app.route('/post/<post_id>', methods=['POST'])
# def lili(post_id):
#     return 'El id del post es: ' + post_id


# @app.route('/lele')
# def lele():
#     return 'lele'


#todas estas rutas tienen por defecto get por ende si quiero ocupar pos hay q agregarlo
# de esta manera mandamos datos de un clente web atraves un formularioa nuestro servidor contruido en flask
# @app.route('/lele', methods=['POST'])
# def lele():
#     print(request.form)    
#     print(request.form['llave1'])    
#     print(request.form['llave2'])    
#     return 'lele'

#contruyendo URLs # redirecionar el usuario
# @app.route('/lele', methods=['POST'])
# def lele():
#     #tambien la podemos direccionar al index o se escribe una url sino el nombre de la funcion
#     print(url_for('lala', post_id=2))
#     print(request.form)    
#     print(request.form['llave1'])    
#     print(request.form['llave2'])    
#     return 'lele'

#Redireccionamiento al usuario

# @app.route('/lele', methods=['POST', 'GET'])
# def lele():
#     #para abortar las peticiones
#     abort(401)
#     #si ocupo la funcion de redirect siempre debo ocupar un return
#     return redirect(url_for('lala', post_id=2))
#     return 'lele'

#Renderizado plantillas, en este caso un archivo html
# @app.route('/lele', methods=['POST', 'GET'])
# def lele():
#     #para abortar las peticiones
#     # abort(401)
#     #si ocupo la funcion de redirect siempre debo ocupar un return
#     # return redirect(url_for('lala', post_id=2))
#     return render_template('lele.html')

#respondiendo con un JSON
@app.route('/lele', methods=['POST', 'GET'])
def lele():
    cursor.execute('select * from Usuario')
    usuarios = cursor.fetchall()
    print(usuarios)
    
    #para abortar las peticiones
    # abort(401)
    #si ocupo la funcion de redirect siempre debo ocupar un return
    # return redirect(url_for('lala', post_id=2))
    # return {
    #     "username": 'Chanchito Feliz',
    #     "email": 'chachito@feliz.com'
    # }
    
    return render_template('lele.html', usuarios=usuarios)
    
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola Mundo')

# nueva ruta con get y post el get para obtener el formulario y 
# el post para manejar lo que aremos para crear un registro y luego 
# manejar esas dos logicas de manera independiente.
##Ingresando registros a la base de datos
# @app.route('/crear', methods=['GET', 'POST'])
# def crear():
#     if request.method == "POST":
#         username = request.form['username']
#         email = request.form['email']
#         edad = request.form['edad']
#         sql = "insert into Usuario (username, email, edad) values(%s, %s, %s)"
#         values = (username, email, edad)
#         cursor.execute(sql, values)
#         conn.commit()
        
        
#         return redirect(url_for('lele'))
#     return render_template('crear.html')

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == "POST":
        # Si la solicitud es un POST (es decir, se envió el formulario)
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        
        # Preparar una consulta SQL para insertar los datos en la base de datos
        sql = "INSERT INTO Usuario (username, email, edad) VALUES (%s, %s, %s)"
        values = (username, email, edad)
        
        # Ejecutar la consulta SQL y confirmar los cambios en la base de datos
        cursor.execute(sql, values)
        midb.commit()
        
        # Después de la inserción, redirigir a otra vista llamada 'lele'
        return redirect(url_for('lele'))
    
    # Si la solicitud es GET (mostrar el formulario)
    return render_template('crear.html')

