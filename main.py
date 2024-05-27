# Imports #

# Importamos las clases necesarias
from clase_editor import Editor

# Importamos las librerías necesarias
from customtkinter import * 
from tkinter import *
from CTkTable import *

# Inicio #

# Menú #
# Vamos a hacer el menu de nuestro proyecto para navegar entre funcionalidades #



# Crear una Ventana Nueva de Tkinter #
root = Tk()
# Configuración de la Ventana #
root.title("Pyint-2D")
# Maximizar la Ventana #
root.state('zoomed')
# Cambiar el Fondo de la Ventana a brillante #
set_appearance_mode("light")

matriz = [[0 for _ in range(16)] for _ in range(16)]

def cambiar_a_símbolos():
    global color_actual
    global símbolo_actual
    global número_actual
    print(tabla_clásica.get())
    if edición.get() == "Edición con símbolos":
        if color_actual == "black":
            símbolo_actual = "@"
    elif edición.get() == "Edición clásica":
        color_actual = "black"
    elif edición.get() == "Edición con números":
        color_actual = "black"
        número_actual = "0"

edición = CTkTabview(root, width=600, height=600, command = cambiar_a_símbolos)
edición.pack()

# Agregar pestañas al Tabview #
edición.add('Edición clásica')
edición.add('Edición con números')
edición.add('Edición con símbolos')
edición.set('Edición clásica')

color_actual = "black"

def cambiar_color(value):
    columna = value["column"]
    fila = value["row"]
    tabla_clásica.insert(fila, columna, 0, fg_color=color_actual, bg_color=color_actual)
    matriz[fila][columna] = 0
    print(matriz)
    tabla_clásica.config

def cambiar_símbolo(value):
    columna = value["column"]
    fila = value["row"]
    tabla_símbolos.frame[fila, columna].configure(text=símbolo_actual)
def cambiar_número(value):
    columna = value["column"]
    fila = value["row"]
    tabla_números.frame[fila, columna].configure(text=número_actual)

tabla_clásica = CTkTable(master = edición.tab("Edición clásica"),row=16, column=16, command=cambiar_color, padx = 0, colors = ["white", "white"], width=50, height=50)
tabla_clásica.pack()

tabla_símbolos = CTkTable(master = edición.tab("Edición con símbolos"),row=16, column=16, command=cambiar_símbolo, padx = 0, colors = ["white", "white"], width=50, height=50)
tabla_símbolos.pack()

tabla_números = CTkTable(master = edición.tab("Edición con números"),row=16, column=16, command=cambiar_número, padx = 0, colors = ["white", "white"], width=50, height=50)
tabla_números.pack()

root.mainloop()