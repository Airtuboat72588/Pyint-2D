from customtkinter import * 

app = CTk()
app.title("Pyint-2D")

def optionmenu_callback(choice):
    print('optionmenu dropdown clicked:', choice)

optionmenu_var = StringVar(value='option 2')
optionmenu = CTkOptionMenu(app,values=['option 1', 'option 2'], width=140, height=28, command=optionmenu_callback, variable=optionmenu_var)
optionmenu.place(x=10, y=10)

app.mainloop()