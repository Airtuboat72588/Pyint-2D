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

def on_click(value):
    columna = value["column"]
    fila = value["row"]
    tabla_clásica.frame[fila, columna].configure(fg_color=color_actual)

tabla_clásica = CTkTable(master = edición.tab("Edición clásica"),row=100, column=100, command=on_click, padx = 0, colors = ["white", "white"], width=50, height=50)
tabla_clásica.pack()

root.mainloop()