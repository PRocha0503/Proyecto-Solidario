# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:36:48 2020

@author: Usuario
"""

# -*- coding: utf-8 -*-
"""

@author: LJAG
"""


import sqlite3
from sqlite3 import Error
import tkinter
import time
from tkinter import messagebox
from tkinter import OptionMenu
from tkinter import *
import os

## DB --------------------------------------------------------

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("created", create_table_sql)
        
    except Error as e:
        print(e)


def insert_usuario(conn, nom, appat, apmat, edadI, gen, esc, ocp, disc, tpus, ca, numtau):
     
    try:
        cur = conn.cursor()
        
        sqlinsert = ''' INSERT INTO UsuariosBD(Nombre, Apellido_Paterno, 
                    Apellido_Materno, 
                    Edad, Genero, 
                    Escolaridad, 
                    Ocupacion, 
                    Discapacidad, 
                    Tipo_Usuario, 
                    Clave_Acceso,
                    Num_Tarjeta_usuario)
                    VALUES(?,?,?,?,?,?,?,?,?,?) '''
        
        
        cur = conn.cursor()
        cur.execute(sqlinsert,(nom, appat, apmat, edadI, gen, esc, ocp, disc, tpus, ca, numtau))
        conn.commit()
    
    
    except Error as e:
        print(e)
    
    

def admin_check(conn):
    
    try:
        cur = conn.cursor()
        
        cur.execute("SELECT Nombre FROM UsuariosBD WHERE Nombre=?", ("adminBD",))
        adcheck = cur.fetchall()
        
        
               
        
        if len(adcheck) == 0:
            
            sql = ''' INSERT INTO UsuariosBD(Nombre, Clave_Acceso)
            VALUES(?,?) '''
            cur = conn.cursor()
            cur.execute(sql,('adminBD','1234',))
            conn.commit()
            
        else:
            print("El administrador ya esta registrado")
        
    except Error as e:
        print(e)



def login_data(user_login, code_login, conn):
    
        
    try:
        
        
        cur = conn.cursor()
        
        print(user_login)
        
        cur.execute("SELECT Nombre, Clave_Acceso FROM UsuariosBD WHERE Nombre=?", (user_login,))
        
        log_data = cur.fetchall()
        
        print(log_data)
        
        if len(log_data) == 0:
            print("El usuario no esta registrado")
            user_not_found()
            
            #Insert a way to exit login
        
        else:
        
            print(log_data)
            print(len(log_data))
            print(type(log_data))
            print(log_data[0][0])
        
            
            
            if (log_data[0][0] == user_login) and (log_data[0][1] == code_login):
            
                print("Acceso permitido")
                login_sucess()
            
            else:
                print("El usuario o la contraseña son incorrectos")
                password_not_recognised()
            
            
        
    except Error as e:
        print(e)

    
    


def main():
    
    database = r"C:\sqlite\db\pruebabd.db" # CONNECTION IS CREATED, ADRESS FOR LOCAL FILE
    
    
    #Tabla de usuarios

    users_table = """ CREATE TABLE IF NOT EXISTS UsuariosBD (
                                        id_U integer PRIMARY KEY,
                                        Nombre text NOT NULL,
                                        Apellido_Paterno text,
                                        Apellido_Materno text,
                                        Edad integer,
                                        Genero text,
                                        Escolaridad text,
                                        Ocupacion text,
                                        Discapacidad text,
                                        Tipo_Usuario text,
                                        Clave_Acceso text,
                                        Num_Tarjeta_usuario text
                                    ); """

    
    #Tabla conexion usuarios prestamos
    
    U_P_table = """ CREATE TABLE IF NOT EXISTS U_P_table (
                                        id_U integer  integer,
                                        id_P integer integer
                                    ); """
  
    #Tabla conexion prestamos libros
    
    P_L_table = """ CREATE TABLE IF NOT EXISTS P_L_table (
                                        id_P integer integer,
                                        id_L integer integer
                                    ); """
    
    #Tabla de Prestamos

    prestamos_table = """ CREATE TABLE IF NOT EXISTS prestamos_table (
                                        id_P integer PRIMARY KEY,
                                        Fecha_Inicial text NOT NULL,
                                        Fecha_Final text NOT NULL,
                                        Libros integer,
                                        Estado integer
                                    ); """
    
    
    #Tabla de libros

    libros_table = """ CREATE TABLE IF NOT EXISTS libros_table (
                                        id_L integer PRIMARY KEY,
                                        Autor text NOT NULL,
                                        Titulo text NOT NULL,
                                        Clave text,
                                        Cantidad integer,
                                        Coleccion text,
                                        Cantidad_prestados integer,
                                        Num_ejemplar text,
                                        Volumen text,
                                        Num_adquisicion text,
                                        Num_tarjeta_libro text,
                                        ISBN text,
                                        Clasificacion text 
                                    ); """
    
    
    

    # create a database connection
    global conn
    conn = create_connection(database)
    
    
    

    # create tables
    if conn is not None:
        # create tables
        create_table(conn, users_table)
        
        create_table(conn, U_P_table)
        
        create_table(conn, P_L_table)
        
        create_table(conn, prestamos_table)
        
        create_table(conn, libros_table)
        
        
        
        #admin_check(conn)
        
        #login_data("adminBD","1234", conn)

    else:
        print("Error! No se pudo conectar a la base de datos.")





### GUI ------------------------------------------------------



# Designing window for registration

def register():
    
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()


# Designing window for login 

def login():
    
    
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Ingrese su información para acceder").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Usuario").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Contraseña").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    



# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    
    login_data(username1, password1, conn)
    
    
    """

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()
        
    """




# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    menu()
    main_screen.withdraw()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    
    main()
    
    global main_screen
    main_screen = Tk()  # create a GUI window
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("Account Login")  # set the title of GUI window
    Label(text="Base de Datos", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() # create a Form label
    Label(text="").pack()
    Label(text="").pack()
    Button(text="Ingresar", height="2", width="30", command = login).pack() # create Login Button
    Label(text="").pack()
    #Button(text="Register", height="2", width="30", command=register).pack() # create a register button

    main_screen.mainloop() # start the GUI


##------------------------------------------------------------------------------
##-------------------------------GUI PART #2------------------------------------
##------------------------------------------------------------------------------




def menu():  
  ventana2= tkinter.Tk()
  ventana2.geometry( "600x500+100+50")
  
  def salir():
      ventana2.destroy()
      main_screen.destroy()
      sys.exit()

  texto = tkinter.Label(ventana2, text = "Menú", font = ("Arial", 30)).place( x = 300, y = 400)
  boton_consulta = tkinter.Button(ventana2, text = "Consulta", command=consulta).place(x = 50, y = 50 )
  boton_registro_usuario = tkinter.Button(ventana2, text = "Registro de usuarios", command=registro).place(x = 50, y =90 )
  boton_prestamo = tkinter.Button(ventana2, text = "Préstamo", command=prestamo).place(x = 50, y = 130 )
  boton_registro_libro = tkinter.Button(ventana2, text = "Registro de libros", command=libros).place(x = 50, y = 170 )
  boton_edicion_datos = tkinter.Button(ventana2, text = "Edicion de datos").place(x = 50, y = 210 )
  boton_busqueda = tkinter.Button(ventana2, text = "Busqueda", command=busqueda).place(x = 50, y = 250 )

  #boton_salir2 = tkinter.Button(ventana2, text = "Salir", command= ventana2.destroy).place(x = 250, y = 250 )
  
  boton_salir2 = tkinter.Button(ventana2, text = "Salir", command= salir).place(x = 250, y = 250 )

def consulta():
    
  ventana3=tkinter.Tk()
  ventana3.geometry( "600x500+100+50")

  def usuarioBD():
    tablaUsuario=tkinter.Tk()
    tablaUsuario.geometry( "+400+100")
    usuarioDisplay = tkinter.Label(tablaUsuario, text = """Aqui se muestra
    la tabla """).grid(row=0, column=0, sticky="nsew")
    """en esta label se debera 
    de mostrar el DB"""
    salir = tkinter.Button(tablaUsuario, text = "Cerrar", command= tablaUsuario.destroy).grid(row=1, column=1, sticky="nsew")
    return

  def prestamoBD():
    tablaPrestamo=tkinter.Tk()
    tablaPrestamo.geometry( "+400+100")
    prestamoDisplay = tkinter.Label(tablaPrestamo, text = """Aqui se muestra
    la tabla """).grid(row=0, column=0, sticky="nsew")
    salir = tkinter.Button(tablaPrestamo, text = "Cerrar", command= tablaPrestamo.destroy).grid(row=1, column=1, sticky="nsew")
    return

  def libroBD():
    tablaLibro=tkinter.Tk()
    tablaLibro.geometry( "+400+100")
    libroDisplay = tkinter.Label(tablaLibro, text = """Aqui se muestra
    la tabla """).grid(row=0, column=0, sticky="nsew")
    salir = tkinter.Button(tablaLibro, text = "Cerrar", command= tablaLibro.destroy).grid(row=1, column=1, sticky="nsew")
    return

  texto2 = tkinter.Label(ventana3, text = "Consulta", font = ("Arial", 30)).place( x = 275, y = 400)
  boton_usuario = tkinter.Button(ventana3, text = "Usuario", command = usuarioBD).place(x = 50, y = 50 )

  #Se despliega tabla de datos de usuarioBD
  #---------------------------------------------

  boton_prestamo2 = tkinter.Button(ventana3, text = "Préstamo", command = prestamoBD).place(x = 50, y =90 )

  #Se despliega tabla de datos de prestamoBD
  #---------------------------------------------

  boton_libro = tkinter.Button(ventana3, text = "Libro", command = libroBD).place(x = 50, y = 130 )

  #Se despliega tabla de datos de libroBD
  #---------------------------------------------

  boton_menu = tkinter.Button(ventana3, text = "Menú", command=ventana3.destroy).place(x = 150, y = 250)
   
def registro():
    def registrarBD(conn, nom, appat, apmat, edadI, gen, esc, ocp, disc, tpus, ca, numtau):
        #---------------------------------
        #"""añadir datos a Base de datos"""
        
        insert_usuario(conn, nom, appat, apmat, edadI, gen, esc, ocp, disc, tpus, ca, numtau)
        
        
        #username_login_entry = Entry(login_screen, textvariable=username_verify)
        
        #-----------------------------------
                
        correcto = messagebox.showinfo(message="Se ha registrado con exito", title="Exito")
        return
      
    ventana4=tkinter.Tk()
    ventana4.geometry( "600x500+100+50")
    texto3 = tkinter.Label(ventana4, text = "Registro de Usuarios", font = ("Arial", 30)).place( x = 160, y = 400)
    boton_menu2 = tkinter.Button(ventana4, text = "Menú", command=ventana4.destroy).place(x = 320, y = 350)
    boton_registrar = tkinter.Button(ventana4, text = "Registrar", command= registrarBD).place(x = 250, y = 300)

    #funcion para agregar datos de persona registrada a base de datos
    
    
    
    #-----------------------------------------------
    
    # definir variables para la los cuadros de texto
    nom = StringVar()
    appat = StringVar()
    apmat = StringVar()
    edadI = StringVar()
    gen = StringVar()
    esc = StringVar()
    ocp = StringVar()
    disc = StringVar()
    tpus = StringVar()


    nombre = tkinter.Label(ventana4,text="Nombre").place ( x = 100, y = 10)
    apellidop = tkinter.Label(ventana4,text="Apellido Paterno").place ( x = 100, y = 35)
    apellidom = tkinter.Label(ventana4,text="Apellido Materno").place ( x = 100, y = 60)
    edad = tkinter.Label(ventana4,text="Edad").place ( x = 100, y = 85)
    genero = tkinter.Label(ventana4,text="Género").place ( x = 100, y = 110)
    escolaridad = tkinter.Label(ventana4,text="Escolaridad").place ( x = 100, y = 135)
    ocupacion = tkinter.Label(ventana4,text="Ocupación").place ( x = 100, y = 160)
    discapacidad = tkinter.Label(ventana4,text="Discapacidad").place( x =100, y = 185)
    
    textBox_nombre = tkinter.Entry(ventana4, textvariable = nom)
    #textBox_nombre.pack(side=tkinter.TOP)
    textBox_nombre.place( x =250, y = 10)
    
    textBox_apellidop = tkinter.Entry(ventana4, textvariable = appat)
    #textBox_apellidop.pack(side=tkinter.TOP)
    textBox_apellidop.place( x =250, y = 35)
    
    textBox_apellidom = tkinter.Entry(ventana4, textvariable = apmat)
    #textBox_apellidom.pack(side=tkinter.TOP)
    textBox_apellidom.place( x =250, y = 60)
    
    textBox_edad = tkinter.Entry(ventana4, textvariable = edadI)
    #textBox_edad.pack(side=tkinter.TOP)
    textBox_edad.place( x =250, y = 85)
    
    textBox_genero = tkinter.Entry(ventana4, textvariable = gen)
    #textBox_genero.pack(side=tkinter.TOP)
    textBox_genero.place( x =250, y = 110)
    
    textBox_escolaridad = tkinter.Entry(ventana4, textvariable = esc)
    #textBox_escolaridad.pack(side=tkinter.TOP)
    textBox_escolaridad.place( x =250, y = 135)
    
    textBox_ocupacion = tkinter.Entry(ventana4, textvariable = ocp)
    #textBox_ocupacion.pack(side=tkinter.TOP)
    textBox_ocupacion.place( x =250, y = 160)
    
    textBox_discapacidad = tkinter.Entry(ventana4, textvariable = disc)
    #textBox_discapacidad.pack(side=tkinter.TOP)
    textBox_discapacidad.place( x =250, y = 185)
    
    textBox_tipousuario = tkinter.Entry(ventana4, textvariable = tpus)
    #textBox_tipousuario.pack(side=tkinter.TOP)
    textBox_tipousuario.place( x =250, y = 210)
    
    if textBox_nombre or textBox_apellidop or textBox_apellidom or textBox_edad or textBox_genero or textBox_escolaridad or textBox_ocupacion == "":
      pass




    
def libros():
    def registarLibro():
      #---------------------------------
      #---------Registro en DB   
      #------------------------------
      correcto = messagebox.showinfo(message="Se ha registrado con exito", title="Exito")
      return
    
    ventana5=tkinter.Tk()
    ventana5.geometry( "600x500+100+50")
    texto4 = tkinter.Label(ventana5, text = "Registro Libros", font = ("Arial", 30)).place( x = 230, y = 400)
    boton_menu3 = tkinter.Button(ventana5, text = "Menú", command=ventana5.destroy).place(x = 300, y = 250)
    boton_registrar2 = tkinter.Button(ventana5, text = "Registrar", command=registarLibro).place(x = 250, y = 190)
    autor=tkinter.Label(ventana5,text="Autor").place ( x = 95, y = 5)
    titulo=tkinter.Label(ventana5,text="Titulo").place ( x = 95, y = 25)
    clave=tkinter.Label(ventana5,text="Clave").place ( x = 95, y = 45)
    cantidad=tkinter.Label(ventana5,text="Cantidad").place ( x = 95, y = 69)
    coleccion=tkinter.Label(ventana5,text="Colección").place ( x = 95, y = 93)
    cantidad_prestados=tkinter.Label(ventana5,text="Cantidad prestados").place ( x = 95, y = 115)
    numero_ejemplar=tkinter.Label(ventana5,text="N° de ejemplar").place ( x = 95, y = 137)
    textBox_autor = tkinter.Entry(ventana5)
    textBox_autor.pack(side=tkinter.TOP)
    textBox_titulo = tkinter.Entry(ventana5)
    textBox_titulo.pack(side=tkinter.TOP)
    textBox_clave = tkinter.Entry(ventana5)
    textBox_clave.pack(side=tkinter.TOP)
    textBox_cantidad = tkinter.Entry(ventana5)
    textBox_cantidad.pack(side=tkinter.TOP)
    textBox_coleccion = tkinter.Entry(ventana5)
    textBox_coleccion.pack(side=tkinter.TOP)
    textBox_cantidad_prestados = tkinter.Entry(ventana5)
    textBox_cantidad_prestados.pack(side=tkinter.TOP)
    textBox_numero_ejemplar = tkinter.Entry(ventana5)
    textBox_numero_ejemplar.pack(side=tkinter.TOP)

def prestamo():
    def registarPrestamo():
      #---------------------------------
      #---------Registro en DB   
      
      
      
      #------------------------------
      correcto = messagebox.showinfo(message="Se ha registrado con exito", title="Exito")
      return
    
    ventana6=tkinter.Tk()
    ventana6.geometry( "600x500+100+50")
    texto5 = tkinter.Label(ventana6, text = "Préstamo", font = ("Arial", 30)).place( x = 250, y = 400)
    boton_menu4 = tkinter.Button(ventana6, text = "Menú", command=ventana6.destroy).place(x = 300, y = 180)
    boton_registrar3 = tkinter.Button(ventana6, text = "Registrar", command=registarPrestamo).place(x = 250, y = 140)    
    fechain=tkinter.Label(ventana6,text="Fecha Inicial").place ( x = 110, y = 5)
    fechafi=tkinter.Label(ventana6,text="Fecha Final").place ( x = 110, y = 25)
    libros=tkinter.Label(ventana6,text="Libros").place ( x = 110, y = 45)
    estado=tkinter.Label(ventana6,text="Estado").place ( x = 110, y = 65)
    textBox_fechain = tkinter.Entry(ventana6)
    textBox_fechain.pack(side=tkinter.TOP)
    textBox_fechafi = tkinter.Entry(ventana6)
    textBox_fechafi.pack(side=tkinter.TOP)
    textBox_libros = tkinter.Entry(ventana6)
    textBox_libros.pack(side=tkinter.TOP)
    textBox_estado = tkinter.Entry(ventana6)
    textBox_estado.pack(side=tkinter.TOP)
    
def busqueda():
    def buscarBD():
      #----------------------------
      #Buscar en base de datos seleccion de tablaUsuario
      
      
      #---------------------------
      return
    ventana7=tkinter.Tk()
    ventana7.geometry( "600x500+100+50")
    texto6 = tkinter.Label(ventana7, text = "Búsqueda", font = ("Arial", 30)).place( x = 270, y = 400)
    boton_menu5 = tkinter.Button(ventana7, text = "Menú", command=ventana7.destroy).place(x = 330, y = 300)
    textBox_buscar = tkinter.Entry(ventana7).place(x = 230 , y = 200)
    boton_buscar = tkinter.Button(ventana7, text = "Buscar",command = buscarBD).place(x = 400, y = 200)
 
    varDes = StringVar(ventana7)
    varDes.set('Seleccionar tabla')

    varModo = StringVar(ventana7)
    varModo.set('Seleccionar rubro')

    opciones = ['Usuario','Prestamo', 'Libro']
    ventanaDeslizante = OptionMenu(ventana7, varDes, *opciones)
    ventanaDeslizante.config(width=20)
    ventanaDeslizante.place(x = 80, y = 120)
    opciones2 = ['Nombre','Fecha','Cantidad','Autor']
    ventanaModoTrans = OptionMenu(ventana7, varModo, *opciones2)
    ventanaModoTrans.config(width=20)
    ventanaModoTrans.place(x = 350, y = 120)



main_account_screen() # call the main_account_screen() function
