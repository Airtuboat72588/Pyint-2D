import tkinter as tk
from tkinter import filedialog, messagebox
import json

def select_file():
    # Abrir el cuadro de diálogo para seleccionar un archivo
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    
    if not file_path:
        return  # Si no se selecciona ningún archivo, salir de la función
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Asumimos que el contenido del archivo es una matriz
        if isinstance(data, list) and all(isinstance(row, list) for row in data):
            print("Contenido de la matriz:", data)
            messagebox.showinfo("Archivo JSON", f"Contenido de la matriz:\n{data}")
        else:
            messagebox.showerror("Error", "El archivo JSON no contiene una matriz válida")
    
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo JSON: {e}")

def save_matrix():
    # Definir la matriz que se desea guardar
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Abrir el cuadro de diálogo para seleccionar la ubicación y nombre del archivo
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    
    if not file_path:
        return  # Si no se selecciona ningún archivo, salir de la función
    
    try:
        with open(file_path, 'w') as file:
            json.dump(matrix, file)
        
        messagebox.showinfo("Éxito", "La matriz se ha guardado exitosamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo JSON: {e}")

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Gestión de archivos JSON")

# Crear y configurar el botón para seleccionar un archivo
btn_select_file = tk.Button(root, text="Seleccionar archivo JSON", command=select_file)
btn_select_file.pack(pady=10)

# Crear y configurar el botón para guardar la matriz en un archivo
btn_save_matrix = tk.Button(root, text="Guardar matriz en archivo JSON", command=save_matrix)
btn_save_matrix.pack(pady=10)

# Iniciar el bucle principal de Tkinter
root.mainloop()
