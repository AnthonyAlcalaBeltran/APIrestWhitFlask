
from flask import Flask, jsonify, request
#importaremos abort para poder redireccionar al usuario ..
# .. cuando no se encuentre el recurso buscado por id
from flask import abort
#nos permitira pedir el json a agregar
from flask import request
app = Flask(__name__)

#simulador de jason para los datos
libros = [
    {
        'id': 1,
        'titulo': u'la divina comedia',
        'descripcion': u'lallaalalalalal', 
        'existencia': False
    },
    {
        'id': 2,
        'titulo': u'la metamorfosis',
        'descripcion': u'leleleelel', 
        'existencia': False
    },
    {
        'id': 3,
        'titulo': u'lManual de usuario Genesys',
        'descripcion': u'lilililililiiii', 
        'existencia': True
    }
]

#la ruta .../libros nos muestra toda la informacion de los libros en formato json
@app.route('/libros', methods=['GET'])
def mostrar_libros():
    return jsonify({'libros': libros})

#ahora buscaremos los libros por su identificador usando la ruta ../libros/id
@app.route('/libros/<int:id_libro>', methods=['GET'])
def mostrar_libro_por_id(id_libro):
    libro = [libro for libro in libros if libro['id'] == id_libro]
    if len(libro) == 0:
#en caso la lista de libros quede vacia el usuario sera redireccinado a la pagina 404 not found
        abort(404)
    return jsonify({'libro': libro[0]})

#(post)Ahora haremos que nos permita agregar un JSON con los datos de algun libro
@app.route('/libros', methods=['POST'])
def crear_libro():
    if not request.json or not 'titulo' in request.json:
        abort(400)
    libro_nuevo = {
        'id': libros[-1]['id'] + 1,
        'titulo': request.json['titulo'],
        'descripcion': request.json.get('descripcion', ""),
        'existencia': request.json['existencia'],
    }
    libros.append(libro_nuevo)
    return jsonify({'libro': libro_nuevo}), 201    

if __name__ == '__main__':
    app.run(debug=True, port=1616)
