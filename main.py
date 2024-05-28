from tkinter import *
from CTkTable import *
from customtkinter import *
from clase_editor import Editor
class root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Pyint-2D")
        self.state('zoomed')
        set_appearance_mode("light")

        self.matriz = [[0 for _ in range(16)] for _ in range(16)]
        self.color_actual = "Black"
        self.símbolo_actual = None
        self.número_actual = None

        self.edición = CTkTabview(self, width=600, height=600, command=self.cambiar_a_símbolos)
        self.edición.pack()

        self.edición.add('Edición clásica')
        self.edición.add('Edición con números')
        self.edición.add('Edición con símbolos')
        self.edición.set('Edición clásica')

        self.tabla_clásica = CTkTable(master=self.edición.tab("Edición clásica"), row=16, column=16, command=self.cambiar_color, padx=2, pady=2, colors=["white", "white"], width=50, height=50, corner_radius=0)
        self.tabla_clásica.pack()

        self.tabla_símbolos = CTkTable(master=self.edición.tab("Edición con símbolos"), row=16, column=16, command=self.cambiar_símbolo, padx=2, pady=2, colors=["white", "white"], width=50, height=50, corner_radius=0)
        self.tabla_símbolos.pack()

        self.tabla_números = CTkTable(master=self.edición.tab("Edición con números"), row=16, column=16, command=self.cambiar_número, padx=2, pady=2, colors=["white", "white"], width=50, height=50, corner_radius=0)
        self.tabla_números.pack()

        self.selección_de_color = "black"

    def cambiar_a_símbolos(self):
        if self.edición.get() == "Edición con símbolos":
            for fila in range(16):
                for columna in range(16):
                    if self.matriz[fila][columna] == 1:
                        self.tabla_símbolos.frame[fila, columna].configure(text="@")
            self.símbolo_actual = "@"
        elif self.edición.get() == "Edición clásica":
            self.color_actual = "black"
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