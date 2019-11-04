from flask import Flask, jsonify, request

app = Flask(__name__)

#El método post nos muestra el envio de un json
#el get nos devuelve un hola mundo
@app.route('/', methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        datoJSON = request.get_json()
        return jsonify({"enviaste":datoJSON})
    else:
        return jsonify({"saludo":"Hola mundo!"})
#nos da la suma de dos numero ingresados en la url - metodo get
@app.route('/suma/<int:num1>/<int:num2>', methods=['GET'])
def obtener_sumatoria(num1,num2):
    return jsonify({"sumatoria":num1+num2})

#nos da la resta de dos numeros ingresados en la url - metodo get
@app.route('/resta/<int:num1>/<int:num2>', methods=['GET'])
def resta(num1,num2): 
    return jsonify({"resta":num1-num2})

if __name__ == '__main__':
    app.run(debug=True, port=1616)