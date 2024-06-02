from tkinter import *
from CTkTable import *
from customtkinter import *
from clase_editor import Editor
class root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Pyint-2D")
        self.state('zoomed')
        self.config(bg="#c4c4c4")
        set_appearance_mode("light")

        self.matriz = [[0 for _ in range(16)] for _ in range(16)]
        self.color_actual = "White"
        self.símbolo_actual = None
        self.número_actual = "0"

        self.edición = CTkTabview(self, width=600, height=600, command= lambda: self.cambiar_a_símbolos(self.color_actual))
        self.edición.pack()

        self.edición.add('Edición clásica')
        self.edición.add('Edición con números')
        self.edición.add('Edición con símbolos')
        self.edición.set('Edición clásica')
        
        self.contenedor_selección_color = Canvas(self)
        self.contenedor_selección_color.place(x=50, y=50)
        self.colors = ["#000000", "#ff0000", "#ff7700", "#ffe600", "#00ff0d", "#00ffee", "#0011ff", "#7b00ff", "#ff00fb", "#FFFFFF"]
        self.botón1_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[0], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[0]))
        self.botón1_sel_color.pack()

        self.botón2_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[1], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[1]))
        self.botón2_sel_color.pack()

        self.botón3_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[2], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[2]))
        self.botón3_sel_color.pack()

        self.botón4_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[3], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[3]))
        self.botón4_sel_color.pack()

        self.botón5_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[4], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[4]))
        self.botón5_sel_color.pack()

        self.botón6_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[5], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[5]))
        self.botón6_sel_color.pack()

        self.botón7_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[6], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[6]))
        self.botón7_sel_color.pack()

        self.botón8_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[7], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[7]))
        self.botón8_sel_color.pack()

        self.botón9_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[8], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[8]))
        self.botón9_sel_color.pack()

        self.botón10_sel_color = CTkButton(self.contenedor_selección_color, bg_color= "#c4c4c4",fg_color=self.colors[9], width=50, height=50, text = "", command=lambda: self.seleccionar_color(self.colors[9]))
        self.botón10_sel_color.pack()

        self.tabla_clásica = CTkTable(master=self.edición.tab("Edición clásica"), row=16, column=16, command=self.cambiar_color, padx=2, pady=2, colors=["white", "white"], width=50, height=50, corner_radius=0)
        self.tabla_clásica.pack()

        self.tabla_símbolos = CTkTable(master=self.edición.tab("Edición con símbolos"), row=16, column=16, command=self.cambiar_símbolo, padx=2, pady=2, colors=["white", "white"], width=50, height=50, corner_radius=0)
        self.tabla_símbolos.pack()

        self.tabla_números = CTkTable(master=self.edición.tab("Edición con números"), row=16, column=16, command=self.cambiar_número, padx=2, pady=2, colors=["white", "white"], width=50, height=50, corner_radius=0)
        self.tabla_números.pack()   
    
    def seleccionar_color(self, color):
        self.color_actual = color

    def cambiar_a_símbolos(self, color):
        if self.edición.get() == "Edición con símbolos":
            for fila in range(16):
                for columna in range(16):
                    if self.matriz[fila][columna] == 1:
                        self.tabla_símbolos.frame[fila, columna].configure(text="@")
            self.símbolo_actual = "@"
        elif self.edición.get() == "Edición clásica":
            self.color_actual = color
            for fila in range(16):
                for columna in range(16):
                    if self.matriz[fila][columna] == 1:
                        self.tabla_clásica.insert(fila, columna, "", fg_color="black", bg_color="black")
        elif self.edición.get() == "Edición con números":
            self.número_actual = "0"
            for fila in range(16):
                for columna in range(16):
                    if self.matriz[fila][columna] == 1:
                        self.tabla_números.frame[fila, columna].configure(text="0")

    def cambiar_color(self, value):
        columna = value["column"]
        fila = value["row"]
        self.tabla_clásica.insert(fila, columna, 1, fg_color=self.color_actual, bg_color=self.color_actual)
        self.matriz[fila][columna] = 1
        print(self.matriz)
        self.tabla_clásica.frame[fila, columna].configure(text="")

    def cambiar_símbolo(self, value):
        columna = value["column"]
        fila = value["row"]
        self.matriz[fila][columna] = 1
        print(self.matriz)
        self.tabla_símbolos.frame[fila, columna].configure(text="@")

    def cambiar_número(self, value):
        columna = value["column"]
        fila = value["row"]
        self.matriz[fila][columna] = 1
        print(self.matriz)
        self.tabla_números.frame[fila, columna].configure(text="1")

root = root()
root.mainloop()