from customtkinter import * 

app = CTk()
app.title("Pyint-2D")
app.attributes("-fullscreen", True)

edición = CTkTabview(app)
edición.place(x=10, y=10)

edición.add('tab 1')  # add tab at the end
edición.add('tab 2')  # add tab at the end
edición.set('tab 1')  # set currently visible tab


app.mainloop()