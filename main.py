from tkinter import *
from customtkinter import CTkTable
from customtkinter import CTkTabview

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

tabla_clásica = CTkTable(master = edición.tab("Edición clásica"),row=12, column=12, values = [[f"{i+1},{j+1}" for j in range(10)] for i in range(10)])
tabla_clásica.pack()


root.mainloop()