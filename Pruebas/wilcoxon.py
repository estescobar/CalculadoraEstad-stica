# wilcoxon_test_calculator.py
import tkinter as tk
from tkinter import messagebox
from scipy import stats

class WilcoxonTestCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Prueba de Wilcoxon")

        self.instruction_label = tk.Label(master, text="Ingrese dos conjuntos de datos separados por comas:", font=("Arial", 14))
        self.instruction_label.pack(pady=10)

        self.data1_label = tk.Label(master, text="Conjunto de Datos 1:")
        self.data1_label.pack(pady=5)
        self.data1_entry = tk.Entry(master, width=50)
        self.data1_entry.pack(pady=5)

        self.data2_label = tk.Label(master, text="Conjunto de Datos 2:")
        self.data2_label.pack(pady=5)
        self.data2_entry = tk.Entry(master, width=50)
        self.data2_entry.pack(pady=5)

        self.calculate_button = tk.Button(master, text="Calcular Prueba de Wilcoxon", command=self.calculate_wilcoxon)
        self.calculate_button.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def calculate_wilcoxon(self):
        data1 = self.data1_entry.get()
        data2 = self.data2_entry.get()

        try:
            x = list(map(float, data1.split(','))) 
            y = list(map(float, data2.split(',')))
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos separados por comas.")
            return

        if len(x) != len(y):
            messagebox.showerror("Error", "Ambos conjuntos de datos deben tener la misma longitud.")
            return

        stat, p_value = stats.wilcoxon(x, y)

        self.result_label.config(text=f"Estadística W: {stat:.4f}, p-valor: {p_value:.4f}")
