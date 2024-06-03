from tkinter import *
from CTkTable import *
from customtkinter import *
from clase_editor import Editor
import json
from PIL import Image
class root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Pyint-2D")
        self.state('zoomed')
        self.config(bg="#c4c4c4")
        set_appearance_mode("light")
        self.resizable(False, False)

        self.matriz = [[0 for _ in range(16)] for _ in range(16)]
        self.color_actual = "White"
        self.símbolo_actual = None
        self.número_actual = "0"

        self.main_contenedor = Frame(self, bg="#c4c4c4", width=1920, height=1080)
        self.main_contenedor.pack()

        self.contenedor_edición = Canvas(self.main_contenedor, bg="#c4c4c4",bd=0, highlightthickness=0)
        self.contenedor_edición.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.edición = CTkTabview(self.contenedor_edición, width=600, height=600, command = self.cambiar_a_símbolos)
        self.edición.pack(pady=50)

        self.edición.add('Edición clásica')
        self.edición.add('Edición con números')
        self.edición.add('Edición con símbolos')
        self.edición.set('Edición clásica')

        self.contenedor_selección_color = Canvas(self.main_contenedor, bg="#c4c4c4",bd=0, highlightthickness=0)
        self.contenedor_selección_color.place(relx=0.8, rely=0.5, anchor=CENTER)

        self.icono_borrar = CTkImage(light_image=Image.open("iconos/borrar.png"), dark_image=Image.open("iconos/borrar.png"), size=(50, 50))
        self.botón_borrar = CTkButton(self.contenedor_selección_color, text="", image=self.icono_borrar, bg_color="#c4c4c4", fg_color="#c4c4c4", command = self.borrar)
        self.botón_borrar.pack()

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

        self.tabla_clásica = CTkTable(master=self.edición.tab("Edición clásica"), row=16, column=16, command=self.cambiar_color, padx=2, pady=2, colors=["white", "white"], width=50, height=50, corner_radius=0)
        self.tabla_clásica.pack(pady=2)

        self.tabla_símbolos = CTkTable(master=self.edición.tab("Edición con símbolos"), row=16, column=16, command=self.cambiar_símbolo, padx=2, pady=2, colors=["white", "white"], width=50, height=50, corner_radius=0)
        self.tabla_símbolos.pack(pady=2)

        self.tabla_números = CTkTable(master=self.edición.tab("Edición con números"), row=16, column=16, command=self.cambiar_número, padx=2, pady=2, colors=["white", "white"], width=50, height=50, corner_radius=0)
        self.tabla_números.pack(pady=2)   

        self.contenedor_menu = Canvas(self.main_contenedor, bg="#c4c4c4",bd=0, highlightthickness=0)
        self.contenedor_menu.place(relx=0.20, rely=0.5, anchor=CENTER)

        self.botón_guardar = CTkButton(self.contenedor_menu, text="Guardar", command= self.guardar_matriz, height=50)
        self.botón_guardar.pack(pady=2)  

        self.botón_abrir = CTkButton(self.contenedor_menu, text="Abrir", command= self.abrir_matriz, height=50)
        self.botón_abrir.pack(pady=2)  

        self.botón_rotar_de = CTkButton(self.contenedor_menu, text="Rotar Derecha", command=self.transformar, height=50)
        self.botón_rotar_de.pack(pady=2)  

        self.botón_rotar_iz = CTkButton(self.contenedor_menu, text="Rotar Izquierda", command=self.transformar, height=50)
        self.botón_rotar_iz.pack(pady=2)  

        self.botón_reflejar_h = CTkButton(self.contenedor_menu, text="Reflejo Horizontal", command=self.transformar, height=50)
        self.botón_reflejar_h.pack(pady=2)  

        self.botón_reflejar_v = CTkButton(self.contenedor_menu, text="Reflejo Vertical", command=self.transformar, height=50)
        self.botón_reflejar_v.pack(pady=2)  

        self.botón_negativo = CTkButton(self.contenedor_menu, text="Negativo", command=self.transformar, height=50)
        self.botón_negativo.pack(pady=2)  

        self.botón_alto_contraste = CTkButton(self.contenedor_menu, text="Alto Contraste", command=self.transformar, height=50)
        self.botón_alto_contraste.pack(pady=2)  

    def transformar(self):
        pass

    def seleccionar_color(self, color, número_de_color, símbolo):
        self.color_actual = color
        self.número_actual = número_de_color
        self.símbolo_actual = símbolo
    
    def borrar(self):
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

    def cambiar_a_símbolos(self):
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

    def cambiar_color(self, value):
        columna = value["column"]
        fila = value["row"]
        self.tabla_clásica.insert(fila, columna, self.número_actual, fg_color=self.color_actual, bg_color=self.color_actual)
        self.matriz[fila][columna] = self.número_actual
        print(self.matriz)
        self.tabla_clásica.frame[fila, columna].configure(text="")

    def cambiar_símbolo(self, value):
        columna = value["column"]
        fila = value["row"]
        self.matriz[fila][columna] = self.número_actual
        print(self.matriz)
        self.tabla_símbolos.frame[fila, columna].configure(text= self.símbolo_actual)

    def cambiar_número(self, value):
        columna = value["column"]
        fila = value["row"]
        self.matriz[fila][columna] = self.número_actual
        print(self.matriz)
        self.tabla_números.frame[fila, columna].configure(text= str(self.número_actual))

    def guardar_matriz(self):
        nombre_archivo = filedialog.asksaveasfilename(defaultextension=".Pyint", filetypes=[("Pyint files", "*.Pyint")])
        if nombre_archivo:
            with open(nombre_archivo, 'w') as f:
                json.dump(self.matriz, f)

    def abrir_matriz(self):
        nombre_archivo = filedialog.askopenfilename(defaultextension=".Pyint", filetypes=[("Pyint files", "*.Pyint")])
        if nombre_archivo:
            with open(nombre_archivo, 'r') as f:
                self.matriz = json.load(f)
            self.cambiar_a_símbolos()


root = root()
root.mainloop()