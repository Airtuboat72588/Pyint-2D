from customtkinter import * 

app = CTk()
app.title("Pyint-2D")

tabview = CTkTabview(app)
tabview.place(x=10, y=10)

tabview.add('tab 1')  # add tab at the end
tabview.add('tab 2')  # add tab at the end
tabview.set('tab 2')  # set currently visible tab

button = CTkButton(master=tabview.tab('tab 1'))
button.place(x=10, y=10)

app.mainloop()