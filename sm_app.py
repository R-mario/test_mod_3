import sqlite3
from sqlite3 import Error
import conexion as conn


connection = conn.create_connection("sm_app.db")

def execute_query(connection,query):
    '''Ejecuta la query que se le pase en la bbdd
    '''
    cursor = connection.cursor()
    print(query)
    try:
        cursor.execute(query)
        connection.commit()
        print("Consulta ejecutada con éxito")
    except Error as e:
        print(f"Ha ocurrido el error '{e}'")

def execute_read_query(connection, query):
    '''funcion que permite obtener la informacion a partir de la query
    que se le pase'''
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Ha ocurrido el error '{e}'")

'''tablas de usuarios, posts, comentarios y likes
todas las tablas tendran un id que los vincula a la tabla usuarios'''

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password TEXT NOT NULL,
    name TEXT UNIQUE NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    nationality TEXT NOT NULL
);
"""

create_posts_table = """
CREATE TABLE IF NOT EXISTS  posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""
#creamos todas las tablas
execute_query(connection,create_users_table)
execute_query(connection,create_posts_table)
execute_query(connection,create_comments_table)
execute_query(connection,create_likes_table)

'''crea usuarios,posts,comentarios y likes'''
create_users = """
INSERT INTO
    users (name,password, age, gender, nationality)
VALUES
    ('John','asdw', 25, 'hombre', 'USA'),
    ('Anna','lolailo', 32, 'mujer', 'France'),
    ('Mary','super', 35, 'mujer', 'England'),
    ('Miguel','30042002', 40, 'hombre', 'España'),
    ('Isabel','1234', 21, 'mujer', 'Canada')
    ;
"""


create_posts = """
INSERT INTO
    posts (title, description, user_id)
VALUES
    ("Happy", "I am feeling very happy today", 1),
    ("Hot Weather", "The weather is very hot today", 2),
    ("Help", "I need some help with my work", 2),
    ("Great News", "I am getting married", 1),
    ("Interesting Game", "It was a fantastic game of tennis", 5),
    ("Party", "Anyone up for a late-night party today?", 3)
    ;
"""

create_comments = """
INSERT INTO
    comments (text, user_id, post_id)
VALUES
    ('Count me in', 1, 6),
    ('What sort of help?', 5, 3),
    ('Congrats buddy', 2, 4),
    ('I was rooting for Nadal though', 4, 5),
    ('Help with your thesis?', 2, 3),
    ('Many congratulations', 5, 4)
    ;
"""

create_likes = """
INSERT INTO 
    likes (user_id, post_id)
VALUES
    (1, 6),
    (2, 3),
    (1, 5),
    (5, 4),
    (2, 4),
    (4, 2),
    (3, 6)
    ;
"""
#se crean usuarios artificiales para que la rrss no este vacia de primeras
execute_query(connection,create_users)
execute_query(connection,create_posts)
execute_query(connection,create_comments)
execute_query(connection,create_likes)

connection.close()