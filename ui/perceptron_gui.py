import tkinter as tk
from controller.perceptron_controller import PerceptronController

class PerceptronGUI:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Perceptron - Sistema de Calificación Automática")
        self.controller = controller
        self.puntos = tk.StringVar(value="0")
        self.ausencias = tk.StringVar(value="0")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Puntos:").grid(row=0, column=0)
        puntos_entry = tk.Entry(self.root, textvariable=self.puntos)
        puntos_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Ausencias:").grid(row=1, column=0)
        ausencias_entry = tk.Entry(self.root, textvariable=self.ausencias)
        ausencias_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Verificar", command=self.verificar_paso).grid(row=2, column=0, columnspan=2)
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.grid(row=3, column=0, columnspan=2)

    def verificar_paso(self):
        puntos = self.puntos.get()
        ausencias = self.ausencias.get()
        result = self.controller.verificar_paso(puntos, ausencias)

        if result is None:
            return

        puntos, ausencias, resultado = result
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Resultados para puntos = {puntos}, ausencias = {ausencias}:\n")
        self.output_text.insert(tk.END, f"Predicción: {resultado}\n")
