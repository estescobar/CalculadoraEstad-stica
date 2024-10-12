# spearman_correlation_calculator.py
import tkinter as tk
from tkinter import messagebox
from scipy import stats
import numpy as np

class SpearmanCorrelationCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Correlación de Spearman")

        self.instruction_label = tk.Label(master, text="Ingrese dos conjuntos de datos:", font=("Arial", 14))
        self.instruction_label.pack(pady=10)

        self.data1_label = tk.Label(master, text="Conjunto de Datos 1 (separados por comas):")
        self.data1_label.pack(pady=5)
        self.data1_entry = tk.Entry(master, width=50)
        self.data1_entry.pack(pady=5)

        self.data2_label = tk.Label(master, text="Conjunto de Datos 2 (separados por comas):")
        self.data2_label.pack(pady=5)
        self.data2_entry = tk.Entry(master, width=50)
        self.data2_entry.pack(pady=5)

        self.calculate_button = tk.Button(master, text="Calcular Correlación de Spearman", command=self.calculate_spearman)
        self.calculate_button.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def calculate_spearman(self):
        data1 = self.data1_entry.get()
        data2 = self.data2_entry.get()

        try:
            data1 = list(map(float, data1.split(','))) 
            data2 = list(map(float, data2.split(',')))  

            if len(data1) != len(data2):
                raise ValueError("Los conjuntos de datos deben tener la misma longitud.")

            correlation, p_value = stats.spearmanr(data1, data2)

            self.result_label.config(text=f"Coeficiente de Correlación de Spearman: {correlation:.4f}, p-valor: {p_value:.4f}")

        except ValueError as e:
            messagebox.showerror("Error", str(e))
