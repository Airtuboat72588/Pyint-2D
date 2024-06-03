
# Importamos las librerías necesarias
from tkinter import *
from CTkTable import *
from customtkinter import *
import json
from PIL import Image
import os
from datetime import datetime

# Clase principal
class Editor(Tk):

    # Constructor
    def __init__(self):

        # Inicializamos la clase padre (quien es tkinter.Tk)
        super().__init__()

        # Configuración de la ventana
        self.title("Pyint-2D")
        self.state('zoomed')
        self.config(bg="#c4c4c4")
        set_appearance_mode("light")
        self.resizable(False, False)

        #Obtiene el nombre de usuario de windows

        self.creador = os.getlogin()

        # Atributos
        self.EstadoPrograma = "" # Creado, en proceso, terminado.
        self.matriz = [[0 for _ in range(16)] for _ in range(16)]
        self.color_actual = "White"
        self.símbolo_actual = None
        self.número_actual = "0"

        # Contenedor principal
        self.main_contenedor = Frame(self, bg="#c4c4c4", width=1920, height=1080)
        self.main_contenedor.pack()

        # Contenedores secundarios
        self.contenedor_edición = Canvas(self.main_contenedor, bg="#c4c4c4",bd=0, highlightthickness=0)
        self.contenedor_edición.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Pestañas de edición (Numerico, Símbolos, Clásico)
        self.edición = CTkTabview(self.contenedor_edición, width=600, height=600, command = self.ver_matriz_img)
        self.edición.pack(pady=50)

        # Añadir pestañas
        self.edición.add('Edición clásica')
        self.edición.add('Edición con números')
        self.edición.add('Edición con símbolos')
        self.edición.set('Edición clásica')

        # Contenedor de selección de color
        self.contenedor_selección_color = Canvas(self.main_contenedor, bg="#c4c4c4",bd=0, highlightthickness=0)
        self.contenedor_selección_color.place(relx=0.9, rely=0.5, anchor=CENTER)

        # Botones de selección de color (Borrar, Colores)

        # Botón de borrar
        self.icono_borrar = CTkImage(light_image=Image.open("iconos/borrar.png"), dark_image=Image.open("iconos/borrar.png"), size=(50, 50))
        self.botón_borrar = CTkButton(self.contenedor_selección_color, text="", image=self.icono_borrar, bg_color="#c4c4c4", fg_color="#c4c4c4", command = self.cerrar_img)
        self.botón_borrar.pack()

        # Colores
        self.colors = ["#FFFFFF", "#ff0000", "#ff7700", "#ffe600", "#00ff0d", "#00ffee", "#0011ff", "#7b00ff", "#ff00fb", "#000000"]
        self.botón1_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[0], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[0], número_de_color = 0, símbolo = ""))
        self.botón1_sel_color.pack(pady=2)

        self.botón2_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[1], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[1], número_de_color = 1, símbolo = "."))
        self.botón2_sel_color.pack(pady=2)

        self.botón3_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[2], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[2], número_de_color = 2, símbolo = ":"))
        self.botón3_sel_color.pack(pady=2)

        self.botón4_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[3], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[3], número_de_color = 3, símbolo = "-"))
        self.botón4_sel_color.pack(pady=2)

        self.botón5_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[4], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[4], número_de_color = 4, símbolo = "="))
        self.botón5_sel_color.pack(pady=2)

        self.botón6_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[5], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[5], número_de_color = 5, símbolo = "¡"))
        self.botón6_sel_color.pack(pady=2)

        self.botón7_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[6], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[6], número_de_color = 6, símbolo = "&"))
        self.botón7_sel_color.pack(pady=2)

        self.botón8_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[7], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[7], número_de_color = 7, símbolo = "$"))
        self.botón8_sel_color.pack(pady=2)

        self.botón9_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[8], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[8], número_de_color = 8, símbolo = "%"))
        self.botón9_sel_color.pack(pady=2)

        self.botón10_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[9], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[9], número_de_color = 9, símbolo = "@"))
        self.botón10_sel_color.pack(pady=2)

        # Tablas de edición

        # Tabla clásica
        self.tabla_clásica = CTkTable(master=self.edición.tab("Edición clásica"), row=16, column=16, command=self.cambiar_color, padx=2, pady=2, colors=["white", "white"], width=50, height=50, corner_radius=0)
        self.tabla_clásica.pack(pady=2)

        # Tabla de símbolos
        self.tabla_símbolos = CTkTable(master=self.edición.tab("Edición con símbolos"), row=16, column=16, command=self.cambiar_símbolo, padx=2, pady=2, colors=["white", "white"], width=50, height=50, corner_radius=0)
        self.tabla_símbolos.pack(pady=2)

        # Tabla de números
        self.tabla_números = CTkTable(master=self.edición.tab("Edición con números"), row=16, column=16, command=self.cambiar_número, padx=2, pady=2, colors=["white", "white"], width=50, height=50, corner_radius=0)
        self.tabla_números.pack(pady=2)   

        # Contenedor de menú
        self.contenedor_menu = Canvas(self.main_contenedor, bg="#c4c4c4",bd=0, highlightthickness=0)
        self.contenedor_menu.place(relx=0.1, rely=0.5, anchor=CENTER)

        # Botones de menú (Guardar, Abrir, Rotar Derecha, Rotar Izquierda, Reflejo Horizontal, Reflejo Vertical, Negativo, Alto Contraste)
        self.botón_guardar = CTkButton(self.contenedor_menu, text="Guardar", command= self.guardar_matriz, height=50)
        self.botón_guardar.pack(pady=2)  

        self.botón_abrir = CTkButton(self.contenedor_menu, text="Abrir", command= self.cargar_matriz, height=50)
        self.botón_abrir.pack(pady=2)  

        self.botón_rotar_de = CTkButton(self.contenedor_menu, text="Rotar Derecha", command= lambda: self.transformar_img(valor = 1), height=50)
        self.botón_rotar_de.pack(pady=2)  

        self.botón_rotar_iz = CTkButton(self.contenedor_menu, text="Rotar Izquierda", command= lambda: self.transformar_img(valor = 2), height=50)
        self.botón_rotar_iz.pack(pady=2)  

        self.botón_reflejar_h = CTkButton(self.contenedor_menu, text="Reflejo Horizontal", command= lambda: self.transformar_img(valor = 3), height=50)
        self.botón_reflejar_h.pack(pady=2)  

        self.botón_reflejar_v = CTkButton(self.contenedor_menu, text="Reflejo Vertical", command= lambda: self.transformar_img(valor = 4), height=50)
        self.botón_reflejar_v.pack(pady=2)  

        self.botón_negativo = CTkButton(self.contenedor_menu, text="Negativo", command= lambda: self.transformar_img(valor = 5), height=50)
        self.botón_negativo.pack(pady=2)  

        self.botón_alto_contraste = CTkButton(self.contenedor_menu, text="Alto Contraste", command= lambda: self.transformar_img(valor = 6), height=50)
        self.botón_alto_contraste.pack(pady=2)  

    # Métodos #

    # Funcion para imprimir atributos del objeto creado
    def atributos(self):
        print("Matriz: ", self.Matriz)
        print("Creador: ", self.Creador)
        print("Estado del Programa: ", self.EstadoPrograma)

    # Guardar: va a guardar la imagen (matriz numérica) en formato .json #
    def guardar_matriz(self):
        nombre_archivo = filedialog.asksaveasfilename(defaultextension=".Pyint", filetypes=[("Pyint files", "*.Pyint")])
        if nombre_archivo:
            with open(nombre_archivo, 'w') as f:
                datos = {
                    'matriz': self.matriz,
                    'creador': self.creador
                }
                json.dump(datos, f)

    # Cargar: va a cargar la imagen (matriz numérica) en formato .json y desplegar por default la imagen en color #
    def cargar_matriz(self):
        nombre_archivo = filedialog.askopenfilename(defaultextension=".Pyint", filetypes=[("Pyint files", "*.Pyint")])
        if nombre_archivo:
            with open(nombre_archivo, 'r') as f:
                datos = json.load(f)
                self.matriz = datos['matriz']
                self.creador = datos['creador']
            self.ver_matriz_img()
            info_creador = CTkLabel(self, text=f"Creado por: {self.creador}", bg_color="#c4c4c4")
            info_creador.place(relx=0.97, rely=0.99, anchor='se')

    # Editar: va a permitir editar la imagen (matriz numérica) en color #
    def editar_img(self):
        pass

    # Ver: va a permitir ver la imagen (ya sea a color, números y símbolos) en color #
    def ver_matriz_img(self):
        if self.edición.get() == "Edición con símbolos":
            for fila in range(16):
                for columna in range(16):
                    if self.matriz[fila][columna] == 0:
                        self.tabla_símbolos.frame[fila, columna].configure(text="")
                    elif self.matriz[fila][columna] == 1:
                        self.tabla_símbolos.frame[fila, columna].configure(text=".")
                    elif self.matriz[fila][columna] == 2:
                        self.tabla_símbolos.frame[fila, columna].configure(text=":")
                    elif self.matriz[fila][columna] == 3:
                        self.tabla_símbolos.frame[fila, columna].configure(text="-")
                    elif self.matriz[fila][columna] == 4:
                        self.tabla_símbolos.frame[fila, columna].configure(text="=")
                    elif self.matriz[fila][columna] == 5:
                        self.tabla_símbolos.frame[fila, columna].configure(text="¡")
                    elif self.matriz[fila][columna] == 6:
                        self.tabla_símbolos.frame[fila, columna].configure(text="&")
                    elif self.matriz[fila][columna] == 7:
                        self.tabla_símbolos.frame[fila, columna].configure(text="$")
                    elif self.matriz[fila][columna] == 8:
                        self.tabla_símbolos.frame[fila, columna].configure(text="%")
                    elif self.matriz[fila][columna] == 9:
                        self.tabla_símbolos.frame[fila, columna].configure(text="@")
        elif self.edición.get() == "Edición clásica":
            for fila in range(16):
                for columna in range(16):
                    if self.matriz[fila][columna] == 0:
                        self.tabla_clásica.insert(fila, columna, "", fg_color="#FFFFFF", bg_color="#FFFFFF")
                    elif self.matriz[fila][columna] == 1:
                        self.tabla_clásica.insert(fila, columna, "", fg_color="#ff0000", bg_color="#ff0000")
                    elif self.matriz[fila][columna] == 2:
                        self.tabla_clásica.insert(fila, columna, "", fg_color="#ff7700", bg_color="#ff7700")
                    elif self.matriz[fila][columna] == 3:
                        self.tabla_clásica.insert(fila, columna, "", fg_color="#ffe600", bg_color="#ffe600")
                    elif self.matriz[fila][columna] == 4:
                        self.tabla_clásica.insert(fila, columna, "", fg_color="#00ff0d", bg_color="#00ff0d")
                    elif self.matriz[fila][columna] == 5:
                        self.tabla_clásica.insert(fila, columna, "", fg_color="#00ffee", bg_color="#00ffee")
                    elif self.matriz[fila][columna] == 6:
                        self.tabla_clásica.insert(fila, columna, "", fg_color="#0011ff", bg_color="#0011ff")
                    elif self.matriz[fila][columna] == 7:
                        self.tabla_clásica.insert(fila, columna, "", fg_color="#7b00ff", bg_color="#7b00ff")
                    elif self.matriz[fila][columna] == 8:
                        self.tabla_clásica.insert(fila, columna, "", fg_color="#ff00fb", bg_color="#ff00fb")
                    elif self.matriz[fila][columna] == 9:
                        self.tabla_clásica.insert(fila, columna, "", fg_color="#000000", bg_color="#000000")

        elif self.edición.get() == "Edición con números":
            for fila in range(16):
                for columna in range(16):
                    if self.matriz[fila][columna] == 0:
                        self.tabla_números.frame[fila, columna].configure(text="0")
                    elif self.matriz[fila][columna] == 1:
                        self.tabla_números.frame[fila, columna].configure(text="1")
                    elif self.matriz[fila][columna] == 2:
                        self.tabla_números.frame[fila, columna].configure(text="2")
                    elif self.matriz[fila][columna] == 3:
                        self.tabla_números.frame[fila, columna].configure(text="3")
                    elif self.matriz[fila][columna] == 4:
                        self.tabla_números.frame[fila, columna].configure(text="4")
                    elif self.matriz[fila][columna] == 5:
                        self.tabla_números.frame[fila, columna].configure(text="5")
                    elif self.matriz[fila][columna] == 6:
                        self.tabla_números.frame[fila, columna].configure(text="6")
                    elif self.matriz[fila][columna] == 7:
                        self.tabla_números.frame[fila, columna].configure(text="7")
                    elif self.matriz[fila][columna] == 8:
                        self.tabla_números.frame[fila, columna].configure(text="8")
                    elif self.matriz[fila][columna] == 9:
                        self.tabla_números.frame[fila, columna].configure(text="9")

    # Método para cambiar el color de una celda
    def cambiar_color(self, value):
        columna = value["column"]
        fila = value["row"]
        self.tabla_clásica.insert(fila, columna, self.número_actual, fg_color=self.color_actual, bg_color=self.color_actual)
        self.matriz[fila][columna] = self.número_actual
        #print(self.matriz)
        self.tabla_clásica.frame[fila, columna].configure(text="")

    # Método para cambiar el símbolo de una celda
    def cambiar_símbolo(self, value):
        columna = value["column"]
        fila = value["row"]
        self.matriz[fila][columna] = self.número_actual
        #print(self.matriz)
        self.tabla_símbolos.frame[fila, columna].configure(text= self.símbolo_actual)

    # Método para cambiar el número de una celda
    def cambiar_número(self, value):
        columna = value["column"]
        fila = value["row"]
        self.matriz[fila][columna] = self.número_actual
        #print(self.matriz)
        self.tabla_números.frame[fila, columna].configure(text= str(self.número_actual))

    # Cerrar: va a limpiar el lienzo para crear una imagen más #
    def cerrar_img(self):
        if self.edición.get() == "Edición clásica":
            for fila in range(16):
                for columna in range(16):
                    self.tabla_clásica.insert(fila, columna, "", fg_color="#FFFFFF", bg_color="#FFFFFF")
        elif self.edición.get() == "Edición con símbolos":
            for fila in range(16):
                for columna in range(16):
                    self.tabla_símbolos.frame[fila, columna].configure(text="")
        elif self.edición.get() == "Edición con números":
            for fila in range(16):
                for columna in range(16):
                    self.tabla_números.frame[fila, columna].configure(text="")
        self.matriz = [[0 for _ in range(16)] for _ in range(16)]
        self.tabla_clásica.clear()
        self.tabla_símbolos.clear()
        self.tabla_números.clear()

    # Zoom_In: va a permitir hacer zoom in a la imagen por cuadrantes (4 cuadrantes) #
    def zoom_in(self):
        pass

    # Zoom_Out: va a permitir hacer zoom out (devuelve a tamaño convensional) #
    def zoom_out(self):
        pass

    # Función que llamará a las funciones de transformaciones dependiendo del botón que se presione 
    def transformar_img(self, valor):

        if valor == 1:
            self.matriz = self.rotar_derecha_img()
        elif valor == 2:
            self.matriz = self.rotar_izquierda_img()
        elif valor == 3:
            self.matriz = self.espejo_horizontal()
        elif valor == 4:
            self.matriz = self.espejo_vertical()
        elif valor == 5:
            self.matriz = self.negativo()
        elif valor == 6:
            self.matriz = self.alto_contraste()
        else:
            return "Valor no valido"
        
        self.ver_matriz_img()

        return "Imagen transformada exitosamente"
        

    # Rotar Derecha: va a permitir rotar la imagen 90 grados a la derecha, es decir convierte las filas en columnas y viseversa de manera que... #
    # ... la ultima fila será la primera columna, la primer columna será, la primera fila será la ultima columna y la ultima columna será la última fila #
    def rotar_derecha_img(self):
        Matriz = self.matriz
        n = len(Matriz)
        Matriz_aux = [[0 for _ in range(n)] for _ in range(n)]  # Create an empty matrix of the same size

        for i in range(n):
            for j in range(n):
                Matriz_aux[j][n-i-1] = Matriz[i][j]  # Transpose and reverse each row

        return Matriz_aux

    # Rotar Izquierda: va a permitir rotar la imagen 90 grados a la izquierda, es decir convierte las filas en columnas y viseversa de manera que... #
    # ... la ultima fila será la última columna, la primer columna será la ultima fila, la primera fila será la primera columna y la ultima columna será la última fila #
    def rotar_izquierda_img(self):
        Matriz = self.matriz
        n = len(Matriz)
        Matriz_aux = [[0 for _ in range(n)] for _ in range(n)]  # Create an empty matrix of the same size

        for i in range(n):
            for j in range(n):
                Matriz_aux[n-j-1][i] = Matriz[i][j]  # Transpose and reverse each column

        return Matriz_aux

    # Espejo Horizontal: va a permitir hacer un espejo horizontal de la imagen de manera que...#
    # ... la primera fila será la ultima fila, la segunda fila será la penultima fila y así sucesivamente #
    def espejo_horizontal(self):
        Matriz = self.matriz
        n = len(Matriz)
        Matriz_aux = [[0 for _ in range(n)] for _ in range(n)] 

        for i in range(n):
            for j in range(n):
                
                Matriz_aux[i][j] = Matriz[n-i-1][j]

        return Matriz_aux

    # Espejo Vertical: va a permitir hacer un espejo vertical de la imagen de manera que...#
    # ... la primera columna será la última columna, la segunda columna será la penultima columna y así sucesivamente #
    def espejo_vertical(self):
        Matriz = self.matriz
        n = len(Matriz)
        Matriz_aux = [[0 for _ in range(n)] for _ in range(n)] 

        for i in range(n):
            for j in range(n):
                Matriz_aux[i][j] = Matriz[i][n-j-1]

        return Matriz_aux
                

    # Escala de Grises: va a permitir convertir la imagen a escala de grises de manera que los colores más cercanos al 0 seran 0 y...#
    # ... los colores más cercanos al 9 seran 9 #
    def alto_contraste(self):
        Matriz = self.matriz
        n = len(Matriz)
        Matriz_aux = [[0 for _ in range(n)] for _ in range(n)] 

        for i in range(n):
            for j in range(n):
                if Matriz[i][j] == 0:
                    Matriz[i][j] = 0
                else:
                    Matriz[i][j] = 9
        
        return Matriz

    # Negativo: va a permitir convertir la imagen a negativo de manera que los colores más cercanos al 0 (de 0 a 5) seran su contraparte más cercano al 9 (de 5 a 9) #
    def negativo(self):
        Matriz = self.matriz
        n = len(Matriz)
        Matriz_aux = [[0 for _ in range(n)] for _ in range(n)] 

        for i in range(n):
            for j in range(n):

                match Matriz[i][j]:
                    case 0:
                        Matriz[i][j] = 9
                    case 1:
                        Matriz[i][j] = 8
                    case 2:
                        Matriz[i][j] = 7
                    case 3:
                        Matriz[i][j] = 6
                    case 4:
                        Matriz[i][j] = 5
                    case 5:
                        Matriz[i][j] = 4
                    case 6:
                        Matriz[i][j] = 3
                    case 7:
                        Matriz[i][j] = 2
                    case 8:
                        Matriz[i][j] = 1
                    case 9:
                        Matriz[i][j] = 0
        
        return Matriz


    # ASCII_Art: Este hace cumplir una tabla en la que cada número va a tener un simbolo asignado de la siguiente manera: #
    # 0: " ", 1: ".", 2: ":", 3: "-", 4: "=", 5: "¡", 6: "&", 7: "$", 8: "%", 9: "@" #
    def ASCII_Art(self):
        
        Matriz = self.matriz
        n = len(Matriz)
        Matriz_aux = [[0 for _ in range(n)] for _ in range(n)] 

        for i in range(n):
            for j in range(n):    
                match Matriz[i][j]:
                    case 0:
                        Matriz[i][j] = " "
                    case 1:
                        Matriz[i][j] = "."
                    case 2:
                        Matriz[i][j] = ":"
                    case 3:
                        Matriz[i][j] = "-"
                    case 4:
                        Matriz[i][j] = "="
                    case 5:
                        Matriz[i][j] = "¡"
                    case 6:
                        Matriz[i][j] = "&"
                    case 7:
                        Matriz[i][j] = "$"
                    case 8:
                        Matriz[i][j] = "%"
                    case 9:
                        Matriz[i][j] = "@"
        
        return Matriz


    # Método para seleccionar un color
    def seleccionar_color(self, color, número_de_color, símbolo):
        self.color_actual = color
        self.número_actual = número_de_color
        self.símbolo_actual = símbolo

Editor = Editor()
Editor.mainloop()
