from customtkinter import * 
from tkinter import *
from CTkTable import *

root = Tk()
root.title("Pyint-2D")
root.state('zoomed')
set_appearance_mode("light")

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

edición.add('Edición clásica')
edición.add('Edición con números')
edición.add('Edición con símbolos')
edición.set('Edición clásica')

color_actual = "black"

def cambiar_color(value):
    columna = value["column"]
    fila = value["row"]
    tabla_clásica.insert(fila, columna, 0, fg_color=color_actual, bg_color=color_actual)

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