from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

#puedes pasarle datos atraves de la url
# @app.route('/lala/<usuario>')
# def lala(usuario):
#     return 'lala' + usuario

# GET, POST, PUT se utiliza para reemplazar un recurso , PATH realiza la misma accion q put, se ocupa para actualizar parcialmente un recurso , DELETE
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
    return 'El id del post es: ' + post_id


@app.route('/lele')
def lele():
    return 'lele'