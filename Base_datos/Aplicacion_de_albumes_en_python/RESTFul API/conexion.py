import mysql.connector

bd = mysql.connector.connect(
    user='pacheco', password='12345678',
    database='albumapp')

cursor = bd.cursor()

def get_usuarios():
    consulta = "SELECT * FROM usuario"

    cursor.execute(consulta)
    usuarios = []
    for row in cursor.fetchall():
        usuario = {
            'id': row[0],
            'correo': row[1],
            'contrasena': row[2]
        }
        usuarios.append(usuario)
    return usuarios
        
def existe_usuario(correo):
    query = "SELECT COUNT(*) FROM usuario WHERE correo = %s"
    cursor.execute(query, (correo,))

    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False

import hashlib
def crear_usuario(correo, contra):
    if existe_usuario(correo):
        return False
    else:
        h = hashlib.new('sha256', bytes(contra, 'utf-8'))
        h = h.hexdigest()
        insertar = "INSERT INTO usuario(correo, contrasena) VALUES(%s, %s)"
        cursor.execute(insertar, (correo, h))
        bd.commit()

        return True

def eliminar_usuario(id):
    eliminar = "DELETE from usuario WHERE id = %s"
    cursor.execute(eliminar, (id,))
    bd.commit()
    if cursor.rowcount:
        return True
    else:
        return False    

def iniciar_sesion(correo, contra):
    h = hashlib.new('sha256', bytes(contra, 'utf-8'))
    h = h.hexdigest()
    query = "SELECT id FROM usuario WHERE correo = %s AND contrasena = %s"
    cursor.execute(query, (correo, h))
    id = cursor.fetchone()
    if id:
        return id[0], True
    else:
        return None, False

def insertar_album(album):
    titulo_album = album['titulo_album']
    ano_produccion = album['ano_produccion']
    nombre_artista = album['nombre_artista']
    tracks = album['tracks']
    link_caratula = album['link_caratula']
    usuarioId = album['usuarioId']

    insertar = "INSERT INTO album \
        (titulo_album, ano_produccion, nombre_artista, tracks, link_caratula, usuarioId) \
        VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(insertar, 
    (titulo_album, ano_produccion, nombre_artista, tracks, link_caratula, usuarioId))
    bd.commit()

    if cursor.rowcount:
        return True
    else:
        return False

def get_albums():
    query = "SELECT id, titulo_album, ano_produccion, nombre_artista, tracks, link_caratula, usuarioId FROM album"
    cursor.execute(query)
    albums = []
    for row in cursor.fetchall():
        album = {
            'id': row[0],
            'titulo_album': row[1],
            'ano_produccion': row[2],
            'nombre_artista': row[3],
            'tracks': row[4],
            'link_caratula': row[5] 
        }
        albums.append(album)
    
    return albums

def get_album(id):
    query = "SELECT * FROM album WHERE id = %s"
    cursor.execute(query, (id,))
    album = {}
    row = cursor.fetchone()
    if row:
        album['id'] = row[0]
        album['titulo_album'] = row[1]
        album['ano_produccion'] = row[2]
        album['nombre_artista'] = row[3]
        album['tracks'] = row[4]
        album['link_caratula'] = row[5]

    return album

def modificar_album(id, columna, valor):
    update = f"UPDATE album SET {columna} = %s WHERE id = %s"
    cursor.execute(update, (valor, id))
    bd.commit()

    if cursor.rowcount:
        return True
    else:
        return False

def eliminar_album(id):
    eliminar = "DELETE from album WHERE id = %s"
    cursor.execute(eliminar, (id,))
    bd.commit()

    if cursor.rowcount:
        return True
    else:
        return False

def get_albums_usuario(id):
    query = "SELECT * FROM album WHERE usuarioId = %s"
    cursor.execute(query, (id,))
    albums = []
    for row in cursor.fetchall():
        album = {
            'id': row[0],
            'titulo_album': row[1],
            'ano_produccion': row[2],
            'nombre_artista': row[3],
            'tracks': row[4],
            'link_caratula': row[5]
        }
        albums.append(album)
    return albums

def insertar_artista(artista):
    tracks = artista['tracks']
    titulo_album = artista['titulo_album']
    nombre_artista = artista['nombre_artista']
    imagen_artista = artista['imagen_artista']
    nacimiento = artista['nacimiento']
    usuarioId = artista['usuarioId']
    
    insertar = "INSERT INTO artista \
        (tracks, titulo_album, nombre_artista, imagen_artista, nacimiento, usuarioId) \
        VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(insertar, 
    (tracks, titulo_album, nombre_artista, imagen_artista, nacimiento, usuarioId))
    bd.commit()

    if cursor.rowcount:
        return True
    else:
        return False

def get_artistas():
    query = "SELECT id, tracks, titulo_album, nombre_artista, imagen_artista, nacimiento,  usuarioId FROM artista"
    cursor.execute(query)
    artistas = []
    for row in cursor.fetchall():
        artista = {
            'id': row[0],
            'tracks': row[1],
            'titulo_album': row[2],
            'nombre_artista': row[3],
            'imagen_artista': row[4],
            'nacimiento': row[5],
        }
        artistas.append(artista)
    
    return artistas

def get_artista(id):
    query = "SELECT * FROM artista WHERE id = %s"
    cursor.execute(query, (id,))
    artista = {}
    row = cursor.fetchone()
    if row:
        artista['id'] = row[0]
        artista['tracks'] = row[1]
        artista['titulo_album'] = row[2]
        artista['nombre_artista'] = row[3]
        artista['imagen_artista'] = row[4]
        artista['nacimiento'] = row[4]

    return artista

def modificar_artista(id, columna, valor):
    update = f"UPDATE artista SET {columna} = %s WHERE id = %s"
    cursor.execute(update, (valor, id))
    bd.commit()

    if cursor.rowcount:
        return True
    else:
        return False

def eliminar_artista(id):
    eliminar = "DELETE from artista WHERE id = %s"
    cursor.execute(eliminar, (id,))
    bd.commit()

    if cursor.rowcount:
        return True
    else:
        return False

def get_artistas_usuario(id):
    query = "SELECT * FROM artista WHERE usuarioId = %s"
    cursor.execute(query, (id,))
    artistas = []
    for row in cursor.fetchall():
        album = {
            'id': row[0],
            'tracks': row[1],
            'titulo_album': row[2],
            'nombre_artista': row[3],
            'imagen_artista': row[4],
            'nacimiento': row[5],
        }
        artistas.append(album)
    return artistas