
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
