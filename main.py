
# Importamos las librerías necesarias
from tkinter import *
from CTkTable import *
from customtkinter import *
import json
from PIL import Image
import os
import numpy as np
import copy

# Clase principal
class Editor(Tk):

    # Constructor
    def __init__(self):

        # Inicializamos la clase padre (quien es tkinter.Tk)
        super().__init__()

        # Configuración de la ventana
        self.title("Pyint-2D")
        self.state('zoomed')
        self.light_bg ="#c4c4c4"
        self.config(bg= self.light_bg)
        set_appearance_mode("light")
        self.resizable(False, False)

        #Obtiene el nombre de usuario de windows

        self.creador = os.getlogin()

        #Variable de estado del modo de alto contraste

        self.alto_contraste_estado = False

        #Variable de estado del zoom

        self.zoom_activo = False
        self.zoom_activo_b = False

        # Atributos
        self.EstadoPrograma = "" # Creado, en proceso, terminado.
        self.matriz = [[0 for _ in range(16)] for _ in range(16)]
        self.color_actual = "White"
        self.símbolo_actual = None
        self.número_actual = "0"

        # Contenedor principal
        self.main_contenedor = Frame(self, bg= self.light_bg, width=1920, height=1080)
        self.main_contenedor.pack()

        # Contenedores secundarios
        self.contenedor_edición = Canvas(self.main_contenedor, bg= self.light_bg,bd=0, highlightthickness=0)
        self.contenedor_edición.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Pestañas de edición (Numérico, Símbolos, Clásico)
        self.edición = CTkTabview(self.contenedor_edición, width=600, height=600, command = self.ver_matriz_img)
        self.edición.pack(pady=50)

        # Añadir pestañas
        self.edición.add('Edición clásica')
        self.edición.add('Edición con números')
        self.edición.add('Edición con símbolos')
        self.edición.set('Edición clásica')

        # Contenedor de selección de color
        self.contenedor_selección_color = Canvas(self.main_contenedor, bg= self.light_bg,bd=0, highlightthickness=0)
        self.contenedor_selección_color.place(relx=0.9, rely=0.5, anchor=CENTER)

        # Botones de selección de color (Borrar, Colores)

        # Botón de borrar
        self.icono_borrar = CTkImage(light_image=Image.open("iconos/borrar.png"), dark_image=Image.open("iconos/borrar.png"), size=(50, 50))
        self.botón_borrar = CTkButton(self.contenedor_selección_color, text="", image=self.icono_borrar, bg_color= self.light_bg, fg_color= self.light_bg, command = self.cerrar_img)
        self.botón_borrar.pack()

        # Colores
        self.colors = ["#FFFFFF", "#FFFF00", "#FDE54C", "#FBCA97", "#BB834C", "#7B3C00", "#FE3200", "#86295D", "#0D20BA", "#000000"]
        self.botón1_sel_color = CTkButton(self.contenedor_selección_color, bg_color=  self.light_bg,fg_color=self.colors[0], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[0], número_de_color = 0, símbolo = ""))
        self.botón1_sel_color.pack(pady=2)

        self.botón2_sel_color = CTkButton(self.contenedor_selección_color, bg_color=  self.light_bg,fg_color=self.colors[1], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[1], número_de_color = 1, símbolo = "."))
        self.botón2_sel_color.pack(pady=2)

        self.botón3_sel_color = CTkButton(self.contenedor_selección_color, bg_color=  self.light_bg,fg_color=self.colors[2], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[2], número_de_color = 2, símbolo = ":"))
        self.botón3_sel_color.pack(pady=2)

        self.botón4_sel_color = CTkButton(self.contenedor_selección_color, bg_color=  self.light_bg,fg_color=self.colors[3], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[3], número_de_color = 3, símbolo = "-"))
        self.botón4_sel_color.pack(pady=2)

        self.botón5_sel_color = CTkButton(self.contenedor_selección_color, bg_color=  self.light_bg,fg_color=self.colors[4], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[4], número_de_color = 4, símbolo = "="))
        self.botón5_sel_color.pack(pady=2)

        self.botón6_sel_color = CTkButton(self.contenedor_selección_color, bg_color=  self.light_bg,fg_color=self.colors[5], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[5], número_de_color = 5, símbolo = "¡"))
        self.botón6_sel_color.pack(pady=2)

        self.botón7_sel_color = CTkButton(self.contenedor_selección_color, bg_color=  self.light_bg,fg_color=self.colors[6], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[6], número_de_color = 6, símbolo = "&"))
        self.botón7_sel_color.pack(pady=2)

        self.botón8_sel_color = CTkButton(self.contenedor_selección_color, bg_color=  self.light_bg,fg_color=self.colors[7], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[7], número_de_color = 7, símbolo = "$"))
        self.botón8_sel_color.pack(pady=2)

        self.botón9_sel_color = CTkButton(self.contenedor_selección_color, bg_color=  self.light_bg,fg_color=self.colors[8], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[8], número_de_color = 8, símbolo = "%"))
        self.botón9_sel_color.pack(pady=2)

        self.botón10_sel_color = CTkButton(self.contenedor_selección_color, bg_color=  self.light_bg,fg_color=self.colors[9], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[9], número_de_color = 9, símbolo = "@"))
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
        self.contenedor_menu = Canvas(self.main_contenedor, bg= self.light_bg,bd=0, highlightthickness=0)
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

        self.botón_alto_contraste = CTkButton(self.contenedor_menu, text="Alto Contraste", command = lambda: self.alto_contraste(), height=50)
        self.botón_alto_contraste.pack(pady=2)  

        self.botón_zoom = CTkButton(self.contenedor_menu, text="Zoom", command = lambda: self.cambiar_estado_zoom(), height=50)
        self.botón_zoom.pack(pady=2)

    # Métodos #

    # Función para imprimir atributos del objeto creado
    def atributos(self):
        print("Matriz: ", self.Matriz)
        print("Creador: ", self.Creador)
        print("Estado del Programa: ", self.EstadoPrograma)

    # Guardar: va a guardar la imagen (matriz numérica) en formato .json #
    def guardar_matriz(self):
        filetypes = [("Pyint files", "*.Pyint"), ("PNG files", "*.png")]
        nombre_archivo = filedialog.asksaveasfilename(defaultextension=".Pyint", filetypes=filetypes)
        if nombre_archivo:
            if nombre_archivo.endswith('.png'):
                self.matriz_a_png(self.matriz, nombre_archivo)
            else:
                with open(nombre_archivo, 'w') as f:
                    datos = {
                        'matriz': self.matriz,
                        'creador': self.creador
                    }
                    json.dump(datos, f)
    
    def matriz_a_png(self, matriz, nombre_archivo):
        # Convertir la matriz de índices en una matriz de colores
        matriz_colores = [[self.colors[int(indice)] for indice in fila] for fila in matriz]
    
        # Convertir la matriz de colores en formato hexadecimal a una matriz de colores en formato RGB
        matriz_rgb = [[tuple(int(hex_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) for hex_color in fila] for fila in matriz_colores]
    
        # Convertir la matriz a un array de numpy
        array = np.array(matriz_rgb, dtype=np.uint8)
    
        # Crear una imagen a partir del array
        imagen = Image.fromarray(array)
    
        # Guardar la imagen en un archivo .png
        imagen.save(nombre_archivo)
    
    # Cargar: va a cargar la imagen (matriz numérica) en formato .json y desplegar por default la imagen en color #
    def cargar_matriz(self):
        nombre_archivo = filedialog.askopenfilename(defaultextension=".Pyint", filetypes=[("Pyint files", "*.Pyint")])
        if nombre_archivo:
            with open(nombre_archivo, 'r') as f:
                datos = json.load(f)
                self.matriz = datos['matriz']
                self.creador = datos['creador']
            self.ver_matriz_img()
            info_creador = CTkLabel(self, text=f"Creado por: {self.creador}", bg_color= self.light_bg)
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
                        self.tabla_clásica.insert(fila, columna, "", fg_color= self.colors[0], bg_color=self.colors[0])
                    elif self.matriz[fila][columna] == 1:
                        self.tabla_clásica.insert(fila, columna, "", fg_color=self.colors[1], bg_color=self.colors[1])
                    elif self.matriz[fila][columna] == 2:
                        self.tabla_clásica.insert(fila, columna, "", fg_color=self.colors[2], bg_color=self.colors[2])
                    elif self.matriz[fila][columna] == 3:
                        self.tabla_clásica.insert(fila, columna, "", fg_color=self.colors[3], bg_color=self.colors[3])
                    elif self.matriz[fila][columna] == 4:
                        self.tabla_clásica.insert(fila, columna, "", fg_color=self.colors[4], bg_color=self.colors[4])
                    elif self.matriz[fila][columna] == 5:
                        self.tabla_clásica.insert(fila, columna, "", fg_color=self.colors[5], bg_color=self.colors[5])
                    elif self.matriz[fila][columna] == 6:
                        self.tabla_clásica.insert(fila, columna, "", fg_color=self.colors[6], bg_color=self.colors[6])
                    elif self.matriz[fila][columna] == 7:
                        self.tabla_clásica.insert(fila, columna, "", fg_color=self.colors[7], bg_color=self.colors[7])
                    elif self.matriz[fila][columna] == 8:
                        self.tabla_clásica.insert(fila, columna, "", fg_color=self.colors[8], bg_color=self.colors[8])
                    elif self.matriz[fila][columna] == 9:
                        self.tabla_clásica.insert(fila, columna, "", fg_color=self.colors[9], bg_color=self.colors[9])

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
        if self.zoom_activo:
            self.seleccionar_zoom(value)
        else:
            columna = value["column"]
            fila = value["row"]
            self.tabla_clásica.insert(fila, columna, self.número_actual, fg_color=self.color_actual, bg_color=self.color_actual)
            self.matriz[fila][columna] = self.número_actual
            #print(self.matriz)
            self.tabla_clásica.frame[fila, columna].configure(text="")

    # Método para cambiar el símbolo de una celda
    def cambiar_símbolo(self, value):
        if self.zoom_activo:
            self.seleccionar_zoom(value)
        else:
            columna = value["column"]
            fila = value["row"]
            self.matriz[fila][columna] = self.número_actual
            #print(self.matriz)
            self.tabla_símbolos.frame[fila, columna].configure(text= self.símbolo_actual)
    
    def cambiar_estado_zoom(self): 
        if self.zoom_activo:
            self.zoom_activo = False
            # Habilitar los botones
            self.botón1_sel_color.configure(state='normal')
            self.botón2_sel_color.configure(state='normal')
            self.botón3_sel_color.configure(state='normal')
            self.botón4_sel_color.configure(state='normal')
            self.botón5_sel_color.configure(state='normal')
            self.botón6_sel_color.configure(state='normal')
            self.botón7_sel_color.configure(state='normal')
            self.botón8_sel_color.configure(state='normal')
            self.botón9_sel_color.configure(state='normal')
            self.botón10_sel_color.configure(state='normal')
            self.botón_rotar_de.configure(state='normal')
            self.botón_rotar_iz.configure(state='normal')
            self.botón_reflejar_h.configure(state='normal')
            self.botón_reflejar_v.configure(state='normal')
            self.botón_negativo.configure(state='normal')
            self.botón_borrar.configure(state='normal')
            self.botón_alto_contraste.configure(state='normal')
        else:
            self.zoom_activo = True
            # Inhabilitar los botones
            self.botón1_sel_color.configure(state='disabled')
            self.botón2_sel_color.configure(state='disabled')
            self.botón3_sel_color.configure(state='disabled')
            self.botón4_sel_color.configure(state='disabled')
            self.botón5_sel_color.configure(state='disabled')
            self.botón6_sel_color.configure(state='disabled')
            self.botón7_sel_color.configure(state='disabled')
            self.botón8_sel_color.configure(state='disabled')
            self.botón9_sel_color.configure(state='disabled')
            self.botón10_sel_color.configure(state='disabled')
            self.botón_rotar_de.configure(state='disabled')
            self.botón_rotar_iz.configure(state='disabled')
            self.botón_reflejar_h.configure(state='disabled')
            self.botón_reflejar_v.configure(state='disabled')
            self.botón_negativo.configure(state='disabled')
            self.botón_borrar.configure(state='disabled')
            self.botón_alto_contraste.configure(state='disabled')

    def seleccionar_zoom(self, value):
        if not self.zoom_activo_b:

            self.botón_zoom.configure(state='disabled')
            # Guardar la ubicación seleccionada por el usuario
            self.zoom_fila = value["row"]
            self.zoom_columna = value["column"]
        
            # Guardar la matriz original
            self.matriz_original = [fila[:] for fila in self.matriz]
    
            # Determinar los límites de la submatriz centrada en el punto seleccionado
            inicio_fila = max(0, self.zoom_fila - len(self.matriz) // 4)
            fin_fila = min(len(self.matriz), inicio_fila + len(self.matriz) // 2)
            inicio_fila = fin_fila - len(self.matriz) // 2
            
            inicio_columna = max(0, self.zoom_columna - len(self.matriz[0]) // 4)
            fin_columna = min(len(self.matriz[0]), inicio_columna + len(self.matriz[0]) // 2)
            inicio_columna = fin_columna - len(self.matriz[0]) // 2
    
            # Crear la submatriz
            submatriz = [fila[inicio_columna:fin_columna] for fila in self.matriz[inicio_fila:fin_fila]]
        
            # Crear una nueva matriz con el tamaño duplicado
            matriz_zoom = [[0 for _ in range(len(submatriz[0])*2)] for _ in range(len(submatriz)*2)]
        
            # Copiar los valores de la submatriz a la matriz ampliada, duplicando cada celda
            for i in range(len(submatriz)):
                for j in range(len(submatriz[i])):
                    matriz_zoom[i*2][j*2] = submatriz[i][j]
                    matriz_zoom[i*2][j*2 + 1] = submatriz[i][j]
                    matriz_zoom[i*2 + 1][j*2] = submatriz[i][j]
                    matriz_zoom[i*2 + 1][j*2 + 1] = submatriz[i][j]
    
            # Reemplazar la matriz original con la matriz ampliada
            self.matriz = matriz_zoom
        
            # Actualizar la visualización de la matriz
            self.ver_matriz_img()
        
            self.zoom_activo_b = True

        else:
            # Restaurar la matriz original
            self.matriz = [fila[:] for fila in self.matriz_original]
        
            # Actualizar la visualización de la matriz
            self.ver_matriz_img()

            self.zoom_activo_b = False

            self.botón_zoom.configure(state='normal')
        



    # Método para cambiar el número de una celda
    def cambiar_número(self, value):
        if self.zoom_activo:
            self.seleccionar_zoom(value)
        else:
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
        

    # Rotar Derecha: va a permitir rotar la imagen 90 grados a la derecha, es decir convierte las filas en columnas y viceversa de manera que... #
    # ... la ultima fila será la primera columna, la primer columna será, la primera fila será la ultima columna y la ultima columna será la última fila #
    def rotar_derecha_img(self):
        Matriz = self.matriz
        n = len(Matriz)
        Matriz_aux = [[0 for _ in range(n)] for _ in range(n)]  # Create an empty matrix of the same size

        for i in range(n):
            for j in range(n):
                Matriz_aux[j][n-i-1] = Matriz[i][j]  # Transpose and reverse each row

        return Matriz_aux

    # Rotar Izquierda: va a permitir rotar la imagen 90 grados a la izquierda, es decir convierte las filas en columnas y viceversa de manera que... #
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
    # ... la primera fila será la ultima fila, la segunda fila será la penúltima fila y así sucesivamente #
    def espejo_horizontal(self):
        Matriz = self.matriz
        n = len(Matriz)
        Matriz_aux = [[0 for _ in range(n)] for _ in range(n)] 

        for i in range(n):
            for j in range(n):
                
                Matriz_aux[i][j] = Matriz[n-i-1][j]

        return Matriz_aux

    # Espejo Vertical: va a permitir hacer un espejo vertical de la imagen de manera que...#
    # ... la primera columna será la última columna, la segunda columna será la penúltima columna y así sucesivamente #
    def espejo_vertical(self):
        Matriz = self.matriz
        n = len(Matriz)
        Matriz_aux = [[0 for _ in range(n)] for _ in range(n)] 

        for i in range(n):
            for j in range(n):
                Matriz_aux[i][j] = Matriz[i][n-j-1]

        return Matriz_aux
                

    # Escala de Grises: va a permitir convertir la imagen a escala de grises de manera que los colores más cercanos al 0 serán 0 y...#
    # ... los colores más cercanos al 9 serán 9 #
    
    def alto_contraste(self):
        if self.alto_contraste_estado == False:
            self.Matriz_original = copy.deepcopy(self.matriz)
            self.alto_contraste_estado = True
            for fila in range(16):
                for columna in range(16):
                    if self.matriz[fila][columna] < 5:
                        self.matriz[fila][columna] = 0
                    else:
                        self.matriz[fila][columna] = 9
            self.botón1_sel_color.configure(state='disabled')
            self.botón2_sel_color.configure(state='disabled')
            self.botón3_sel_color.configure(state='disabled')
            self.botón4_sel_color.configure(state='disabled')
            self.botón5_sel_color.configure(state='disabled')
            self.botón6_sel_color.configure(state='disabled')
            self.botón7_sel_color.configure(state='disabled')
            self.botón8_sel_color.configure(state='disabled')
            self.botón9_sel_color.configure(state='disabled')
            self.botón10_sel_color.configure(state='disabled')
            self.botón_rotar_de.configure(state='disabled')
            self.botón_rotar_iz.configure(state='disabled')
            self.botón_reflejar_h.configure(state='disabled')
            self.botón_reflejar_v.configure(state='disabled')
            self.botón_negativo.configure(state='disabled')
            self.botón_borrar.configure(state='disabled')
            self.botón_zoom.configure(state='disabled')

            self.ver_matriz_img()
        else:
            self.alto_contraste_estado = False
            self.matriz = copy.deepcopy(self.Matriz_original)
            self.ver_matriz_img()
            self.botón1_sel_color.configure(state='normal')
            self.botón2_sel_color.configure(state='normal')
            self.botón3_sel_color.configure(state='normal')
            self.botón4_sel_color.configure(state='normal')
            self.botón5_sel_color.configure(state='normal')
            self.botón6_sel_color.configure(state='normal')
            self.botón7_sel_color.configure(state='normal')
            self.botón8_sel_color.configure(state='normal')
            self.botón9_sel_color.configure(state='normal')
            self.botón10_sel_color.configure(state='normal')
            self.botón_rotar_de.configure(state='normal')
            self.botón_rotar_iz.configure(state='normal')
            self.botón_reflejar_h.configure(state='normal')
            self.botón_reflejar_v.configure(state='normal')
            self.botón_negativo.configure(state='normal')
            self.botón_borrar.configure(state='normal')
            self.botón_zoom.configure(state='normal')

    # Negativo: va a permitir convertir la imagen a negativo de manera que los colores más cercanos al 0 (de 0 a 5) serán su contraparte más cercano al 9 (de 5 a 9) #
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


    # ASCII_Art: Este hace cumplir una tabla en la que cada número va a tener un símbolo asignado de la siguiente manera: #
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