
# En este archivo se va a desarrollar la Clase Editor en la que va a estar basado todo el proyecto.#


# Clase Editor #

class Editor: 

    # Constructor #
    def __init__(self, Matriz, Creador, EstadoPrograma):
        self.Matriz = Matriz
        self.Creador = Creador
        self.EstadoPrograma = EstadoPrograma

    # Funcion para imprimir atributos del objeto creado #

    def atributos(self):
        print("Matriz: ", self.Matriz)
        print("Creador: ", self.Creador)
        print("Estado del Programa: ", self.EstadoPrograma)

    # Métodos #

    # Guardar: va a guardar la imagen (matriz numérica) en formato .json #
    def guardar_img(self):
        print("Hello World!")

    # Cargar: va a cargar la imagen (matriz numérica) en formato .json y desplegar por default la imagen en color #
    def cargar_img(self):
        pass

    # Editar: va a permitir editar la imagen (matriz numérica) en color #
    def editar_img(self):
        pass

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
        pass

    # Rotar Izquierda: va a permitir rotar la imagen 90 grados a la izquierda, es decir convierte las filas en columnas y viseversa de manera que... #
    # ... la ultima fila será la última columna, la primer columna será la ultima fila, la primera fila será la primera columna y la ultima columna será la última fila #
    def rotar_izquierda_img(self):
        pass

    # Espejo Horizontal: va a permitir hacer un espejo horizontal de la imagen de manera que...#
    # ... la primera fila será la ultima fila, la segunda fila será la penultima fila y así sucesivamente #
    def espejo_horizontal(self):
        pass

    # Espejo Vertical: va a permitir hacer un espejo vertical de la imagen de manera que...#
    # ... la primera columna será la última columna, la segunda columna será la penultima columna y así sucesivamente #
    def espejo_vertical(self):
        pass

    # Escala de Grises: va a permitir convertir la imagen a escala de grises de manera que los colores más cercanos al 0 seran 0 y...#
    # ... los colores más cercanos al 9 seran 9 #
    def alto_contraste(self):
        pass

    # Negativo: va a permitir convertir la imagen a negativo de manera que los colores más cercanos al 0 (de 0 a 5) seran su contraparte más cercano al 9 (de 5 a 9) #
    def negativo(self):
        pass

    # ASCII_Art: Este hace cumplir una tabla en la que cada número va a tener un simbolo asignado de la siguiente manera: #
    # 0: " ", 1: ".", 2: ":", 3: "-", 4: "=", 5: "¡", 6: "&", 7: "$", 8: "%", 9: "@" #
    def ASCII_Art(self):
        pass


# Con esto concluimos nuestra clase de hoy #