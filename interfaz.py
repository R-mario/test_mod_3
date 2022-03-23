'''La idea es dise;ar una interfaz que permita crear un nuevo usuario o logearse,
si se crea un usuario se a;ade a la bbdd, si se logea permite mostrar su informacion (perfil) en
una ventana: sus comentarios, likes y posts
si accede a su perfil puede postear algo nuevo (se registra en la tabla de posts)
en la otra ventana: mostrar los posts de los demas, y que permita interactuar con ellos
si accede a su 'feed' puede dar like o comentar en el post de otra persona (se registra en la
tabla de likes y comentarios)
'''
'''de momento se puede comprobar si un usuario esta o no en la bbdd, y si no esta permite a;adirlo
faltaria crear una nueva ventana con las opciones de visualizacion de tu perfil (comentarios, posts y likes)
y tambien poder interaccionar con ello'''


import tkinter as tk
from tkinter import messagebox
import sm_app as bd
import conexion as conn

#creamos la conexion a la bbdd utilizando la funcion del modulo conexion
connection = conn.create_connection("sm_app.db")

def insert_db(user,cont,edad,genero,nacionalidad):
    insert_user = '''
            INSERT INTO 
            users (name,password, age, gender, nationality)
            VALUES 
            ('{}','{}',{},'{}','{}');'''.format(user,cont,int(edad),genero,nacionalidad)
    bd.execute_query(connection,insert_user)

def getEntry():
    ''' Funcion que recoge texto del Entry, este debera almacenarlo
    en la bbdd junto a la contrase;a '''
    usuario = user.get()
    contras = cont.get()
    checkUser(usuario,contras)

def checkUser(usuario,contras):
    ''' si el usuario ya existe en la bbdd, se entra a su perfil, 
    si no existe se mete en la bbdd'''
    find_user = '''
            SELECT
                users.name
            FROM
                users
                '''

    resultado = bd.execute_read_query(connection,find_user)

    # userWindow = tk.Toplevel(root)
    if usuario in resultado[0]:
        tk.Label(userWindow, text=f'bienvenido a tu perfil,{usuario} ').grid(row=0,column=0)
    else:
        option = messagebox.askyesno(title='Registro',message=f'El usuario {usuario} no existe, quieres registrarte?')
        if option:

            tk.Label(main,text='Introduce tu edad: ').grid(row=4,column=0)
            age = tk.Entry(main)
            age.grid(row=4,column=1)

            tk.Label(main,text='Introduce tu genero: ').grid(row=5,column=0,sticky='w')            
            opcion = tk.StringVar()
            genM =tk.Radiobutton(main, text="Hombre", variable=opcion, 
                        value='hombre')
            genM.grid(row=5,column=1,sticky='w')
            genF = tk.Radiobutton(main, text="Mujer", variable=opcion,
                        value='mujer')
            genF.grid(row=6,column=1,sticky='w')
            genO = tk.Radiobutton(main, text="Otros", variable=opcion, 
                        value='otros')
            genO.grid(row=7,column=1,sticky='w')
            genero = opcion.get()

            tk.Label(main,text='Introduce tu pais de nacimiento: ').grid(row=8,column=0,sticky='w')      
            nacionalidad = tk.Entry(main)
            nacionalidad.grid(row=8,column=1)

            enter.destroy()

            register = tk.Button(root,text='Registrase',command=lambda: insert_db(usuario,contras,age.get(),genero,nacionalidad.get()))
            register.grid(padx=5,pady=5,row=9,column=0,sticky='e')

            salir.grid(padx=5,pady=5,row=9,column=0,sticky='e')
            

def clearInput():
    '''elimina el texto introducido en las entry'''
    user.delete(0,'end')
    cont.delete(0,'end')


root = tk.Tk()
root.geometry('350x450+700+200')

header = tk.Frame(root)
header.grid()

label = tk.Label(header, text='Bienvenido a la rSocial')
label.grid(row=0,column=0)

main = tk.Frame(root)
main.grid()

tk.Label(main,text='Introduce tu nombre de usuario: ').grid(row=1,column=0,sticky='w')
user = tk.Entry(main)
user.grid(row=1,column=1)

tk.Label(main,text='Introduce tu contraseña: ').grid(row=2,column=0,sticky='w')
cont = tk.Entry(main,show='*')
cont.grid(row=2,column=1)

#boton enseña
enter = tk.Button(root,text='Enter',command=getEntry)
enter.grid(padx=5,pady=5,row=3,column=0,sticky='e')

#boton salida
salir = tk.Button(root,text='Delete',command=clearInput)
salir.grid(padx=5,pady=5,row=3,column=1,sticky='w')
root.mainloop()
connection.close()