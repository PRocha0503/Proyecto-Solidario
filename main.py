
import tkinter
import time
from tkinter import messagebox
from tkinter import OptionMenu
from tkinter import *

#ejemplo de gi
def acceso():

  ventana=tkinter.Tk()
  ventana.title("Biblioteca")
  ventana.geometry( "600x500+100+50")


  user=tkinter.Label(ventana,text="Usuario").place ( x = 170, y = 40)

  password=tkinter.Label(ventana, text="Contraseña").place(x=170, y=80)

  textBox_user = tkinter.Entry(ventana)#.place ( x = 170, y = 60)
  textBox_user.pack(side=tkinter.TOP)
  textBox_password = tkinter.Entry(ventana)#.place ( x = 170, y = 100)
  textBox_password.pack(side=tkinter.TOP)
  

  def ingresar():
    textous=textBox_user.get()
    textopass=textBox_password.get()
    us=""
    con=""
    
    if  textous== us and textopass==con:
      ventana.destroy()
      menu()
    else:
      correcto = messagebox.showerror(message="""Usuario o contraseña incorrectos.
      Intente de nuevo""")
      acceso()

  boton_ingresar = tkinter.Button(ventana, text = "Ingresar", command=ingresar).place(x = 170, y = 200 )

  boton_salir = tkinter.Button(ventana, text = "Salir", command=ventana.destroy).place(x = 170, y = 250 )
  

  boton_color=tkinter.Button(ventana, height=500, width=20, bg= "#3439E1").place (x=0, y=0)
  texto1 = tkinter.Label(ventana, bg= "#3439E1", text = "Base", font = ("Arial", 20)).place( x = 15, y = 120)
  texto2 = tkinter.Label(ventana, bg= "#3439E1", text = "De", font = ("Arial", 20)).place( x = 15, y = 190)
  texto3 = tkinter.Label(ventana, bg= "#3439E1", text = "Datos", font = ("Arial", 20)).place( x = 15, y = 250)
  texto4 = tkinter.Label(ventana, bg= "#3439E1", text = "Biblioteca", font = ("Arial", 20)).place( x = 15, y = 320)

def menu():
  def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
  
  ventana2=tkinter.Tk()
  ventana2.title("Menú")
  ventana2.geometry( "600x500+100+50")
  def consulta():
      
      ventana3=tkinter.Tk()
      ventana3.title("Consulta")
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

      #texto2 = tkinter.Label(ventana3, text = "Consulta", font = ("Arial", 30)).place( x = 275, y = 400)
      boton_usuario = tkinter.Button(ventana3, text = "Usuario", command = usuarioBD).place(x = 170, y = 50 )
      boton_color=tkinter.Button(ventana3, height=500, width=20, bg= "#3439E1").place (x=0, y=0)
      texto = tkinter.Label(ventana3, bg= "#3439E1", text = "Consulta", font = ("Arial", 20)).place( x = 15, y = 200)

      #Se despliega tabla de datos de usuarioBD
      #---------------------------------------------

      boton_prestamo2 = tkinter.Button(ventana3, text = "Préstamo", command = prestamoBD).place(x = 170, y =90 )

      #Se despliega tabla de datos de prestamoBD
      #---------------------------------------------

      boton_libro = tkinter.Button(ventana3, text = "Libro", command = libroBD).place(x = 170, y = 130 )

      #Se despliega tabla de datos de libroBD
      #---------------------------------------------
      #self.
      boton_menu = Button(ventana3, text = "Menú", 
                         command = combine_funcs(menu, ventana3.destroy)).place(x = 170, y = 250)
       
  def registro():
        
        def registrarBD():
          """añadir datos a Base de datos"""
          correcto = messagebox.showinfo(message="Se ha registrado con exito", title="Exito")
          return
          
        ventana4=tkinter.Tk()
        ventana4.title("Registro")
        ventana4.geometry( "600x500+100+50")
        #texto3 = tkinter.Label(ventana4, text = "Registro de Usuarios", font = ("Arial", 30)).place( x = 160, y = 400)
        boton_color=tkinter.Button(ventana4, height=500, width=20, bg= "#3439E1").place (x=0, y=0)
        texto = tkinter.Label(ventana4, bg= "#3439E1", text = "Registro", font = ("Arial", 20)).place( x = 15, y = 200)
        boton_registrar = tkinter.Button(ventana4, text = "Registrar", command= registrarBD).place(x = 170, y = 190)

        #funcion para agregar datos de persona registrada a base de datos
        #-----------------------------------------------

        nombre=tkinter.Label(ventana4,text="Nombre").place ( x = 170, y = 5)
        apellidop=tkinter.Label(ventana4,text="Apellido Paterno").place ( x = 170, y = 25)
        apellidom=tkinter.Label(ventana4,text="Apellido Materno").place ( x = 170, y = 50)
        edad=tkinter.Label(ventana4,text="Edad").place ( x = 170, y = 73)
        genero=tkinter.Label(ventana4,text="Género").place ( x = 170, y = 95)
        escolaridad=tkinter.Label(ventana4,text="Escolaridad").place ( x = 170, y = 115)
        ocupacion=tkinter.Label(ventana4,text="Ocupación").place ( x = 170, y = 140)
        
        textBox_nombre = tkinter.Entry(ventana4).place ( x = 300, y = 5)
        #textBox_nombre.pack(side=tkinter.TOP)
        textBox_apellidop = tkinter.Entry(ventana4).place ( x = 300, y = 25)
        #textBox_apellidop.pack(side=tkinter.TOP)
        textBox_apellidom = tkinter.Entry(ventana4).place ( x = 300, y = 50)
        #textBox_apellidom.pack(side=tkinter.TOP)
        textBox_edad = tkinter.Entry(ventana4).place ( x = 300, y = 73)
        #textBox_edad.pack(side=tkinter.TOP)
        textBox_genero = tkinter.Entry(ventana4).place ( x = 300, y = 95)
        #textBox_genero.pack(side=tkinter.TOP)
        textBox_escolaridad = tkinter.Entry(ventana4).place ( x = 300, y = 115)
        #textBox_escolaridad.pack(side=tkinter.TOP)
        textBox_ocupacion = tkinter.Entry(ventana4).place ( x = 300, y = 140)
        #textBox_ocupacion.pack(side=tkinter.TOP)
        if textBox_nombre or textBox_apellidop or textBox_apellidom or textBox_edad or textBox_genero or textBox_escolaridad or textBox_ocupacion == "":
          pass
        #self.
        boton_menu2 = Button(ventana4, text = "Menú", 
                        command = combine_funcs(menu, ventana4.destroy)).place(x = 320, y = 250)
        
  def libros():
        
        def registarLibro():
          #---------------------------------
          #---------Registro en DB   
          #------------------------------
          correcto = messagebox.showinfo(message="Se ha registrado con exito", title="Exito")
          return
        
        ventana5=tkinter.Tk()
        ventana5.title("Libros")
        ventana5.geometry( "600x500+100+50")
        #texto4 = tkinter.Label(ventana5, text = "Registro Libros", font = ("Arial", 30)).place( x = 230, y = 400)
        boton_color=tkinter.Button(ventana5, height=500, width=20, bg= "#3439E1").place (x=0, y=0)
        texto = tkinter.Label(ventana5, bg= "#3439E1", text = "Libros", font = ("Arial", 20)).place( x = 15, y = 200)
        
       
        boton_registrar2 = tkinter.Button(ventana5, text = "Registrar", command=registarLibro).place(x = 170, y = 190)
        autor=tkinter.Label(ventana5,text="Autor").place ( x = 170, y = 5)
        titulo=tkinter.Label(ventana5,text="Titulo").place ( x = 170, y = 25)
        clave=tkinter.Label(ventana5,text="Clave").place ( x = 170, y = 45)
        cantidad=tkinter.Label(ventana5,text="Cantidad").place ( x = 170, y = 69)
        coleccion=tkinter.Label(ventana5,text="Colección").place ( x = 170, y = 93)
        cantidad_prestados=tkinter.Label(ventana5,text="Cantidad prestados").place ( x = 170, y = 115)
        numero_ejemplar=tkinter.Label(ventana5,text="N° de ejemplar").place ( x = 170, y = 137)
        textBox_autor = tkinter.Entry(ventana5).place ( x = 300, y = 5)
        #textBox_autor.pack(side=tkinter.TOP)
        textBox_titulo = tkinter.Entry(ventana5).place ( x = 300, y = 25)
        #textBox_titulo.pack(side=tkinter.TOP)
        textBox_clave = tkinter.Entry(ventana5).place ( x = 300, y = 45)
        #textBox_clave.pack(side=tkinter.TOP)
        textBox_cantidad = tkinter.Entry(ventana5).place ( x = 300, y = 69)
        #textBox_cantidad.pack(side=tkinter.TOP)
        textBox_coleccion = tkinter.Entry(ventana5).place ( x = 300, y = 93)
        #textBox_coleccion.pack(side=tkinter.TOP)
        textBox_cantidad_prestados = tkinter.Entry(ventana5).place ( x = 300, y = 115)
        #textBox_cantidad_prestados.pack(side=tkinter.TOP)
        textBox_numero_ejemplar = tkinter.Entry(ventana5).place ( x = 300, y = 137)
        #textBox_numero_ejemplar.pack(side=tkinter.TOP)
        #self.
        boton_menu3 = Button(ventana5, text = "Menú", 
                         command = combine_funcs(menu, ventana5.destroy)).place(x = 170, y = 250)

  def prestamo():
        
        def registarPrestamo():
          #---------------------------------
          #---------Registro en DB   
          #------------------------------
          correcto = messagebox.showinfo(message="Se ha registrado con exito", title="Exito")
          return
        
        ventana6=tkinter.Tk()
        ventana6.title("Préstamo")
        ventana6.geometry( "600x500+100+50")
        #texto5 = tkinter.Label(ventana6, text = "Préstamo", font = ("Arial", 30)).place( x = 250, y = 400)
        boton_color=tkinter.Button(ventana6, height=500, width=20, bg= "#3439E1").place (x=0, y=0)
        texto = tkinter.Label(ventana6, bg= "#3439E1", text = "Préstamo", font = ("Arial", 20)).place( x = 15, y = 200)
        
        
        boton_registrar3 = tkinter.Button(ventana6, text = "Registrar", command=registarPrestamo).place(x = 170, y = 140)    
        fechain=tkinter.Label(ventana6,text="Fecha Inicial").place ( x = 170, y = 5)
        fechafi=tkinter.Label(ventana6,text="Fecha Final").place ( x = 170, y = 25)
        libros=tkinter.Label(ventana6,text="Libros").place ( x = 170, y = 45)
        estado=tkinter.Label(ventana6,text="Estado").place ( x = 170, y = 65)
        textBox_fechain = tkinter.Entry(ventana6).place ( x = 300, y = 5)
        #textBox_fechain.pack(side=tkinter.TOP)
        textBox_fechafi = tkinter.Entry(ventana6).place ( x = 300, y = 25)
        #textBox_fechafi.pack(side=tkinter.TOP)
        textBox_libros = tkinter.Entry(ventana6).place ( x = 300, y = 45)
        #textBox_libros.pack(side=tkinter.TOP)
        textBox_estado = tkinter.Entry(ventana6).place ( x = 300, y = 65)
        #textBox_estado.pack(side=tkinter.TOP)
        #self.
        boton_menu4 = Button(ventana6, text = "Menú", 
                         command = combine_funcs(menu, ventana6.destroy)).place(x = 170, y = 180)
        
  def busqueda():
        
        def buscarBD():
          #----------------------------
          #Buscar en base de datos seleccion de tablaUsuario
          #---------------------------
          return
        ventana7=tkinter.Tk()
        ventana7.title("Búsqueda")
        ventana7.geometry( "600x500+100+50")
        boton_color=tkinter.Button(ventana7, height=500, width=20, bg= "#3439E1").place (x=0, y=0)
        texto = tkinter.Label(ventana7, bg= "#3439E1", text = "Búsqueda", font = ("Arial", 20)).place( x = 15, y = 200)
        #texto6 = tkinter.Label(ventana7, text = "Búsqueda", font = ("Arial", 30)).place( x = 270, y = 400)
       
        
        textBox_buscar = tkinter.Entry(ventana7).place(x = 170 , y = 270)
        boton_buscar = tkinter.Button(ventana7, text = "Buscar",command = buscarBD).place(x = 170, y = 320)
     
        varDes = StringVar(ventana7)
        varDes.set('Seleccionar tabla')

        varModo = StringVar(ventana7)
        varModo.set('Seleccionar rubro')

        opciones = ['Usuario','Prestamo', 'Libro']
        ventanaDeslizante = OptionMenu(ventana7, varDes, *opciones)
        ventanaDeslizante.config(width=20)
        ventanaDeslizante.place(x = 170, y = 50)
        opciones2 = ['Nombre','Fecha','Cantidad','Autor']
        ventanaModoTrans = OptionMenu(ventana7, varModo, *opciones2)
        ventanaModoTrans.config(width=20)
        ventanaModoTrans.place(x = 170, y = 150)
        #self.
        boton_menu5 = Button(ventana7, text = "Menú", 
                        command = combine_funcs(menu, ventana7.destroy)).place(x = 170, y = 370)
  
  
  boton_consulta = Button(ventana2, text = "Consulta", 
                         command = combine_funcs(ventana2.destroy, consulta)).place(x = 170, y = 50)
  
  boton_registro = Button(ventana2, text = "Registro de usuarios", 
                         command = combine_funcs(ventana2.destroy, registro)).place(x = 170, y = 90)
 
  boton_prestamo = Button(ventana2, text = "Préstamo", 
                         command = combine_funcs(ventana2.destroy, prestamo)).place(x = 170, y = 130)
  
  boton_registro_libro = Button(ventana2, text = "Registro de libros", 
                         command = combine_funcs(ventana2.destroy, libros)).place(x = 170, y = 170)
  
  boton_edicion_datos = Button(ventana2, text = "Edicion de datos", 
                         command = combine_funcs(ventana2.destroy, libros)).place(x = 170, y = 210)
  
  boton_busqueda = Button(ventana2, text = "Busqueda", 
                         command = combine_funcs(ventana2.destroy, busqueda)).place(x = 170, y = 250)

  boton_salir2 = tkinter.Button(ventana2, text = "Salir", command= ventana2.destroy).place(x = 170, y = 330 )
  
  boton_color=tkinter.Button(ventana2, height=500, width=20, bg= "#3439E1").place (x=0, y=0)
  texto = tkinter.Label(ventana2, bg= "#3439E1", text = "Menú", font = ("Arial", 20)).place( x = 15, y = 200)
        
acceso()
