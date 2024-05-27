import tkinter as tk
from tkinter import Menu
import customtkinter as ctk

# Crear ventana principal
root = ctk.CTk()
root.title("Aplicación de Pantalla Completa")
root.attributes('-fullscreen', True)

# Variable global para el color del mouse
Color_Mouse = tk.IntVar(value=0)

# Funciones de menú
def cargar():
    print("Cargar")

def guardar():
    print("Guardar")

def cerrar():
    root.quit()

def a_color():
    print("A color")

def numerica():
    print("Numérica")

def ascii_art():
    print("ASCII-Art")

def rotar_derecha():
    print("Rotar derecha")

def rotar_izquierda():
    print("Rotar izquierda")

def reflejar_horizontal():
    print("Reflejar horizontal")

def reflejar_vertical():
    print("Reflejar vertical")

def negativo():
    print("Negativo")

def zoom_in():
    print("Zoom In")

def zoom_out():
    print("Zoom Out")

# Crear barra de menú
menu_bar = Menu(root)

# Menú Archivo
archivo_menu = Menu(menu_bar, tearoff=0)
archivo_menu.add_command(label="Cargar", command=cargar)
archivo_menu.add_command(label="Guardar", command=guardar)
archivo_menu.add_command(label="Cerrar", command=cerrar)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

# Menú Ver
ver_menu = Menu(menu_bar, tearoff=0)
ver_menu.add_command(label="A color", command=a_color)
ver_menu.add_command(label="Numérica", command=numerica)
ver_menu.add_command(label="ASCII-Art", command=ascii_art)
menu_bar.add_cascade(label="Ver", menu=ver_menu)

# Menú Transformar
transformar_menu = Menu(menu_bar, tearoff=0)
transformar_menu.add_command(label="Rotar derecha", command=rotar_derecha)
transformar_menu.add_command(label="Rotar izquierda", command=rotar_izquierda)
transformar_menu.add_command(label="Reflejar horizontal", command=reflejar_horizontal)
transformar_menu.add_command(label="Reflejar vertical", command=reflejar_vertical)
transformar_menu.add_command(label="Negativo", command=negativo)
menu_bar.add_cascade(label="Transformar", menu=transformar_menu)

# Menú Zoom
zoom_menu = Menu(menu_bar, tearoff=0)
zoom_menu.add_command(label="Zoom In", command=zoom_in)
zoom_menu.add_command(label="Zoom Out", command=zoom_out)
menu_bar.add_cascade(label="Zoom", menu=zoom_menu)

# Configurar barra de menú
root.config(menu=menu_bar)

# Crear marco principal
frame = ctk.CTkFrame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Crear cuadrícula de etiquetas (16x16)
grid_frame = ctk.CTkFrame(frame)
grid_frame.grid(row=0, column=0, padx=10, pady=10)

for i in range(16):
    for j in range(16):
        label = ctk.CTkLabel(grid_frame, text="", width=30, height=30, fg_color="white")
        label.grid(row=i, column=j, padx=1, pady=1)

# Crear ventana lateral con botones de colores
color_frame = ctk.CTkFrame(frame)
color_frame.grid(row=0, column=1, padx=10, pady=10, sticky='n')

# Lista de colores y funciones de asignación
colores = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF", "#C0C0C0", "#800000", "#808000", "#008080"]

def cambiar_color(index):
    Color_Mouse.set(index)
    print(f"Color seleccionado: {index}")

for i, color in enumerate(colores):
    button = ctk.CTkButton(color_frame, text="", width=30, height=30, fg_color=color, command=lambda i=i: cambiar_color(i))
    button.grid(row=i, column=0, padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()
