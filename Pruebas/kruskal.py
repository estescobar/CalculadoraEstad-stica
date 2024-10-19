# kruskal_wallis_test_calculator.py
import tkinter as tk
from tkinter import messagebox
from scipy import stats

class KruskalWallisTestCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Prueba de Kruskal-Wallis")

        self.instruction_label = tk.Label(master, text="Ingrese los conjuntos de datos separados por comas:", font=("Arial", 14))
        self.instruction_label.pack(pady=10)

        self.data_label = tk.Label(master, text="Conjuntos de Datos (separados por punto y coma):")
        self.data_label.pack(pady=5)
        self.data_entry = tk.Entry(master, width=50)
        self.data_entry.pack(pady=5)

        self.calculate_button = tk.Button(master, text="Calcular Prueba de Kruskal-Wallis", command=self.calculate_kruskal_wallis)
        self.calculate_button.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def calculate_kruskal_wallis(self):
        data = self.data_entry.get()

        try:
            groups = [list(map(float, group.split(','))) for group in data.split(';')]  
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos separados por comas y puntos y coma.")
            return

        stat, p_value = stats.kruskal(*groups)

        self.result_label.config(text=f"Estadística H: {stat:.4f}, p-valor: {p_value:.4f}")
