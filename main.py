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

tabla_clásica = CTkTable(master = edición.tab("Edición clásica"),row=16, column=16)
tabla_clásica.pack()

root.mainloop()