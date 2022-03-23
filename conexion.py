import sqlite3
from sqlite3 import Error

def create_connection(path):
    '''Crea la conexion a la bbdd
    '''
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("La conexión a la base de datos se ha ejecutado correctamente")
    except Error as e:
        print(f"Ha ocurrido el error '{e}'")
    return connection