from customtkinter import * 
from tkinter import *
from CTkTable import *

root = Tk()
root.title("Pyint-2D")
root.state('zoomed')
set_appearance_mode("light")

edición = CTkTabview(root, width=600, height=600, )
edición.pack()

edición.add('Edición clásica')
edición.add('Edición con números')
edición.add('Edición con símbolos')
edición.set('Edición clásica')

color_actual = "black"
def cambiar_a_símbolos():
    global color_actual
    global símbolo_actual
    if color_actual == "black":
        símbolo_actual = "@"

def cambiar_color(value):
    columna = value["column"]
    fila = value["row"]
    tabla_clásica.frame[fila, columna].configure(fg_color=color_actual)
def cambiar_símbolo(value):
    columna = value["column"]
    fila = value["row"]
    tabla_símbolos.frame[fila, columna].configure(text=símbolo_actual)

tabla_clásica = CTkTable(master = edición.tab("Edición clásica"),row=16, column=16, command=cambiar_color, padx = 0, colors = ["white", "white"], width=50, height=50)
tabla_clásica.pack()

tabla_símbolos = CTkTable(master = edición.tab("Edición con símbolos"),row=16, column=16, command=cambiar_símbolo, padx = 0, colors = ["white", "white"], width=50, height=50)
tabla_símbolos.pack()

root.mainloop()