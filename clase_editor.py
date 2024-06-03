
# En este archivo se va a desarrollar la Clase Editor en la que va a estar basado todo el proyecto.#
from tkinter import filedialog, messagebox
import json

# Clase Editor #

class Editor: 

    # Constructor #
    def __init__(self, Matriz):
        self.Matriz = Matriz
        self.Creador = "Grupo: Josue e Ian"
        self.EstadoPrograma = "Numerico"

    # Funcion para imprimir atributos del objeto creado #

    def atributos(self):
        print("Matriz: ", self.Matriz)
        print("Creador: ", self.Creador)
        print("Estado del Programa: ", self.EstadoPrograma)

    # Métodos #

    # Guardar: va a guardar la imagen (matriz numérica) en formato .json #
    def guardar_img(self):
        
        Matriz = self.Matriz.copy()

        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])

        if not file_path:
            return "No se seleccionó ningún archivo"
        
        try:
            with open(file_path, 'w') as file:
                json.dump(Matriz, file)
            return "La matriz se ha guardado exitosamente"
        except Exception as e:
            return f"No se pudo guardar el archivo JSON: {e}"


    # Cargar: va a cargar la imagen (matriz numérica) en formato .json y desplegar por default la imagen en color #
    def cargar_img(self):
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

    # Editar: va a permitir editar la imagen (matriz numérica) en color #
    def editar_img(self):
        # Open a dialog to select a file
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])

        if not file_path:
            return "No se seleccionó ningún archivo"

        try:
            # Load the matrix from the JSON file
            with open(file_path, 'r') as file:
                Matriz = json.load(file)

            # Perform an edit (in this case, we'll just transpose the matrix)
            Matriz = list(map(list, zip(*Matriz)))

            # Save the changes back to the original file
            with open(file_path, 'w') as file:
                json.dump(Matriz, file)

            return "La matriz se ha editado exitosamente"
        except Exception as e:
            return f"No se pudo editar el archivo JSON: {e}"

    # Ver: va a permitir ver la imagen (matriz numérica) en color #
    def ver_img(self):
        pass

    # Ver Matriz: va a permitir ver la imagen en formato de matriz numérica #
    def ver_matriz(self):
        pass

    # Cerrar: va a limpiar el lienzo para crear una imagen más #
    def cerrar_img(self):
        pass

    # Mostrar: va mostrar la imagen a color (es muy similar a "cargar", pero esta va a funcionar para volver a ver la img a color despues de ver_matriz u otra) #
    def mostrar_img(self):
        pass

    # Zoom_In: va a permitir hacer zoom in a la imagen por cuadrantes (4 cuadrantes) #
    def zoom_in(self):
        pass

    # Zoom_Out: va a permitir hacer zoom out (devuelve a tamaño convensional) #
    def zoom_out(self):
        pass
    
    # Rotar Derecha: va a permitir rotar la imagen 90 grados a la derecha, es decir convierte las filas en columnas y viseversa de manera que... #
    # ... la ultima fila será la primera columna, la primer columna será, la primera fila será la ultima columna y la ultima columna será la última fila #
    def rotar_derecha_img(self):
        
        Matriz = self.Matriz.copy()

        n = len(Matriz)
        
        Matriz_aux = Matriz.copy()

        for i in range(n):
            for j in range(n):
                Matriz_aux[j][i] = Matriz[i][j] 

        return Matriz_aux

    # Rotar Izquierda: va a permitir rotar la imagen 90 grados a la izquierda, es decir convierte las filas en columnas y viseversa de manera que... #
    # ... la ultima fila será la última columna, la primer columna será la ultima fila, la primera fila será la primera columna y la ultima columna será la última fila #
    def rotar_izquierda_img(self):
        Matriz = self.Matriz.copy()
        n = len(Matriz)
        
        Matriz_aux = Matriz.copy()

        for i in range(n):
            for j in range(n):
                Matriz_aux[j][i] = Matriz[i][n-j-1] 

        return Matriz_aux

    # Espejo Horizontal: va a permitir hacer un espejo horizontal de la imagen de manera que...#
    # ... la primera fila será la ultima fila, la segunda fila será la penultima fila y así sucesivamente #
    def espejo_horizontal(self):
        Matriz = self.Matriz
        n = len(Matriz)
        Matriz_aux = Matriz.copy()

        for i in range(n):
            for j in range(n):
                
                Matriz_aux[i][j] = Matriz[n-i-1][j]



        return Matriz_aux

    # Espejo Vertical: va a permitir hacer un espejo vertical de la imagen de manera que...#
    # ... la primera columna será la última columna, la segunda columna será la penultima columna y así sucesivamente #
    def espejo_vertical(self):
        
        Matriz = self.Matriz.copy()

        n = len(Matriz)
        Matriz_aux = Matriz.copy()

        for i in range(n):
            for j in range(n):
                Matriz_aux[i][j] = Matriz[i][n-j-1]

        return Matriz_aux
                

    # Escala de Grises: va a permitir convertir la imagen a escala de grises de manera que los colores más cercanos al 0 seran 0 y...#
    # ... los colores más cercanos al 9 seran 9 #
    def alto_contraste(self):
        Matriz = self.Matriz.copy()
        
        n = len(Matriz)

        for i in range(n):
            for j in range(n):
                if Matriz[i][j] == 0:
                    Matriz[i][j] = 0
                elif 0 < Matriz[i][j] < 4:
                    Matriz[i][j] = 10
                elif 4 <= Matriz[i][j] < 7:
                    Matriz[i][j] = 11
                elif 7 <= Matriz[i][j] < 10:
                    Matriz[i][j] = 12
                elif 10 <= Matriz[i][j] < 13:
                    return "Matriz ya esta en escala de grises"
        
        return Matriz

    # Negativo: va a permitir convertir la imagen a negativo de manera que los colores más cercanos al 0 (de 0 a 5) seran su contraparte más cercano al 9 (de 5 a 9) #
    def negativo(self):

        Matriz = self.Matriz.copy()

        n = len(Matriz)

        for i in range(n):
            for j in range(n):

                match Matriz[i][j]:
                    case 0:
                        Matriz[i][j] = 9
                    case 1:
                        Matriz[i][j] = 8
                    case 2:
                        Matriz[i][j] = 7
                    case 3:
                        Matriz[i][j] = 6
                    case 4:
                        Matriz[i][j] = 5
                    case 5:
                        Matriz[i][j] = 4
                    case 6:
                        Matriz[i][j] = 3
                    case 7:
                        Matriz[i][j] = 2
                    case 8:
                        Matriz[i][j] = 1
                    case 9:
                        Matriz[i][j] = 0
        
        return Matriz


    # ASCII_Art: Este hace cumplir una tabla en la que cada número va a tener un simbolo asignado de la siguiente manera: #
    # 0: " ", 1: ".", 2: ":", 3: "-", 4: "=", 5: "¡", 6: "&", 7: "$", 8: "%", 9: "@" #
    def ASCII_Art(self):
        
        Matriz = self.Matriz.copy()

        n = len(Matriz)

        for i in range(n):
            for j in range(n):    
                match Matriz[i][j]:
                    case 0:
                        Matriz[i][j] = " "
                    case 1:
                        Matriz[i][j] = "."
                    case 2:
                        Matriz[i][j] = ":"
                    case 3:
                        Matriz[i][j] = "-"
                    case 4:
                        Matriz[i][j] = "="
                    case 5:
                        Matriz[i][j] = "¡"
                    case 6:
                        Matriz[i][j] = "&"
                    case 7:
                        Matriz[i][j] = "$"
                    case 8:
                        Matriz[i][j] = "%"
                    case 9:
                        Matriz[i][j] = "@"
        
        return Matriz


# Con esto concluimos nuestra clase de hoy #