from customtkinter import * 
from tkinter import *

root = Tk()
app = CTk(root)
app.title("Pyint-2D")
root.state('zoomed')

edición = CTkTabview(app)
edición.place(x=10, y=10)

edición.add('tab 1')  # add tab at the end
edición.add('tab 2')  # add tab at the end
edición.set('tab 1')  # set currently visible tab


root.mainloop()