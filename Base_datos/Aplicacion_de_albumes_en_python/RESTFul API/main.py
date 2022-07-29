from flask import Flask, jsonify, request

from conexion import crear_usuario, iniciar_sesion
from conexion import insertar_album, insertar_artista
from conexion import get_albums, get_album, get_artistas, get_artista
from conexion import modificar_album, eliminar_album, modificar_artista, eliminar_artista, eliminar_usuario
from conexion import get_albums_usuario, get_artistas_usuario

app = Flask(__name__)

@app.route("/api/v1/usuarios", methods=["POST"])
@app.route("/api/v1/usuarios/<int:id>", methods=["DELETE"])
@app.route("/api/v1/usuarios/<int:id>/album", methods=["GET"])
def usuario(id=None):
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            print(data)

            if crear_usuario(data['correo'], data['contrasena']):
                return jsonify({"code": "ok"})
            else:
                return jsonify({"code": "existe"})
        except:
            return jsonify({"code": "error"})
    elif request.method == "GET" and id is not None:
        return jsonify(get_albums_usuario(id))
    elif request.method == "DELETE" and id is not None:
        if eliminar_usuario(id):
            return jsonify(code='ok')
        else:
            return jsonify(code='ok')



@app.route("/api/v1/albums", methods=["GET", "POST"])
@app.route("/api/v1/albums/<int:id>", methods=["GET", "PATCH", "DELETE"])
def albums(id=None):
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            print(data)
            if insertar_album(data):
                return jsonify({"code": "ok"})
            else:
                return jsonify({"code": "no"})
        except:
            return jsonify({"code": "error"})
    elif request.method == "GET" and id is None:
        return jsonify(get_albums())
    elif request.method == "GET" and id is not None:
        return jsonify(get_album(id))
    elif request.method == "PATCH" and id is not None and request.is_json:
        data = request.get_json()
        columna = data['columna']
        valor = data['valor']

        if modificar_album(id, columna, valor):
            return jsonify(code='ok')
        else:
            return jsonify(code='error')
    elif request.method == "DELETE" and id is not None:
        if eliminar_album(id):
            return jsonify(code='ok')
        else:
            return jsonify(code='ok')


@app.route("/api/v1/sesiones", methods=["POST"])
def sesion():
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            correo = data['correo']
            contra = data['contrasena']
            id, ok = iniciar_sesion(correo, contra)
            if ok:
                return jsonify({"code": "ok", "id": id})
            else:
                return jsonify({"code": "noexiste"})
        except:
            return jsonify({"code": "error"})


@app.route("/api/v1/artistas", methods=["GET", "POST"])
@app.route("/api/v1/artistas/<int:id>", methods=["GET", "PATCH", "DELETE"])
def artistas(id=None):
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            print(data)
            if insertar_artista(data):
                return jsonify({"code": "ok"})
            else:
                return jsonify({"code": "no"})
        except:
            return jsonify({"code": "error"})
    elif request.method == "GET" and id is None:
        return jsonify(get_artistas())
    elif request.method == "GET" and id is not None:
        return jsonify(get_artista(id))
    elif request.method == "PATCH" and id is not None and request.is_json:
        data = request.get_json()
        columna = data['columna']
        valor = data['valor']   

        if modificar_artista(id, columna, valor):
            return jsonify(code='ok')
        else:
            return jsonify(code='error')
    elif request.method == "DELETE" and id is not None:
        if eliminar_artista(id):
            return jsonify(code='ok')
        else:
            return jsonify(code='error')


app.run(debug=True)