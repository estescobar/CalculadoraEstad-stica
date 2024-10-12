# pearson_correlation_calculator.py
import tkinter as tk
from tkinter import messagebox
from scipy import stats

class PearsonCorrelationCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Correlación de Pearson")

        # Etiqueta para instrucciones
        self.instruction_label = tk.Label(master, text="Ingrese dos conjuntos de datos separados por comas:", font=("Arial", 14))
        self.instruction_label.pack(pady=10)

        # Cuadro de entrada para el primer conjunto de datos
        self.data1_label = tk.Label(master, text="Conjunto de Datos 1:")
        self.data1_label.pack(pady=5)
        self.data1_entry = tk.Entry(master, width=50)
        self.data1_entry.pack(pady=5)

        # Cuadro de entrada para el segundo conjunto de datos
        self.data2_label = tk.Label(master, text="Conjunto de Datos 2:")
        self.data2_label.pack(pady=5)
        self.data2_entry = tk.Entry(master, width=50)
        self.data2_entry.pack(pady=5)

        # Botón para calcular la correlación de Pearson
        self.calculate_button = tk.Button(master, text="Calcular Correlación de Pearson", command=self.calculate_pearson_correlation)
        self.calculate_button.pack(pady=20)

        # Área para mostrar el resultado
        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def calculate_pearson_correlation(self):
        # Obtener datos de las entradas
        data1 = self.data1_entry.get()
        data2 = self.data2_entry.get()

        # Convertir las entradas a listas de números
        try:
            data1 = list(map(float, data1.split(',')))
            data2 = list(map(float, data2.split(',')))
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos separados por comas.")
            return

        # Verificar que los dos conjuntos de datos tengan la misma longitud
        if len(data1) != len(data2):
            messagebox.showerror("Error", "Ambos conjuntos de datos deben tener la misma longitud.")
            return

        # Realizar la correlación de Pearson
        correlation_coefficient, p_value = stats.pearsonr(data1, data2)
        self.result_label.config(text=f"Coeficiente de Correlación: {correlation_coefficient:.4f}, p-valor: {p_value:.4f}")
