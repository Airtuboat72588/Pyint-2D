# Imports #

# Importamos las clases necesarias
from clase_editor import Editor

# Importamos las librerías necesarias
from customtkinter import * 
from tkinter import *
from CTkTable import *

# Inicio #

# Crear una Ventana Nueva de Tkinter #
root = Tk()
# Configuración de la Ventana #
root.title("Pyint-2D")
# Maximizar la Ventana #
root.state('zoomed')
# Cambiar el Fondo de la Ventana a brillante #
set_appearance_mode("light")

# Agregar un nuevo Tabview a la Ventana #
edición = CTkTabview(root, width=600, height=600)
edición.pack()

# Agregar pestañas al Tabview #
edición.add('Edición clásica')
edición.add('Edición con números')
edición.add('Edición con símbolos')
edición.set('Edición clásica')


# Tabla Clásica que nos ayudará para mostrara la matriz (lienzo) #
tabla_clásica = CTkTable(master = edición.tab("Edición clásica"),row=12, column=12, values = [[f"{i+1},{j+1}" for j in range(10)] for i in range(10)])
tabla_clásica.pack()


root.mainloop()