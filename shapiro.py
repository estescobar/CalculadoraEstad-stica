# shapiro_wilk_test_calculator.py
import tkinter as tk
from tkinter import messagebox
from scipy import stats

class ShapiroWilkTestCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Prueba de Shapiro-Wilk")

        self.instruction_label = tk.Label(master, text="Ingrese un conjunto de datos separado por comas:", font=("Arial", 14))
        self.instruction_label.pack(pady=10)

        self.data_label = tk.Label(master, text="Conjunto de Datos:")
        self.data_label.pack(pady=5)
        self.data_entry = tk.Entry(master, width=50)
        self.data_entry.pack(pady=5)

        self.calculate_button = tk.Button(master, text="Calcular Prueba de Shapiro-Wilk", command=self.calculate_shapiro_wilk)
        self.calculate_button.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def calculate_shapiro_wilk(self):
        data = self.data_entry.get()

        try:
            data = list(map(float, data.split(',')))
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos separados por comas.")
            return

        stat, p_value = stats.shapiro(data)

        self.result_label.config(text=f"Estadística W: {stat:.4f}, p-valor: {p_value:.4f}")
