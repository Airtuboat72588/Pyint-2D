from customtkinter import * 

root = CTk()
root.title('Custom Tkinter')

Helloword = CTkLabel(root, text='Hello Word', width=40, height=28, fg_color='transparent')
Helloword.place(x=10, y=10)

root.mainloop()