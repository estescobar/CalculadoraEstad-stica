# chi_squared_test_calculator.py
import tkinter as tk
from tkinter import messagebox
from scipy import stats
import numpy as np

class ChiSquaredTestCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Prueba de Chi-Cuadrado")

        self.instruction_label = tk.Label(master, text="Ingrese los datos en una tabla de contingencia:", font=("Arial", 14))
        self.instruction_label.pack(pady=10)

        self.data_label = tk.Label(master, text="Datos (filas separados por punto y coma; columnas por comas):")
        self.data_label.pack(pady=5)
        self.data_entry = tk.Entry(master, width=50)
        self.data_entry.pack(pady=5)

        self.calculate_button = tk.Button(master, text="Calcular Prueba de Chi-Cuadrado", command=self.calculate_chi_squared)
        self.calculate_button.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def calculate_chi_squared(self):
        data = self.data_entry.get()

        try:
            contingency_table = [list(map(int, row.split(','))) for row in data.split(';')] 
            contingency_table = np.array(contingency_table)  
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos como enteros.")
            return

        stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)

        self.result_label.config(text=f"Estadística Chi-cuadrado: {stat:.4f}, p-valor: {p_value:.4f}, Grados de libertad: {dof}")
