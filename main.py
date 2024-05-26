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

tabla_clásica = CTkTable(master = edición.tab("Edición clásica"),row=12, column=12)
tabla_clásica.pack()

def on_click(event):
    # Obtén el cuadro que fue clickeado
    cuadro = tabla_clásica.identify(event.x, event.y)
    
    # Imprime las coordenadas del cuadro
    print(f"Cuadro clickeado: {cuadro}")

# Vincula el evento de clic del ratón a la función on_click
tabla_clásica.bind("<Button-1>", on_click)


root.mainloop()