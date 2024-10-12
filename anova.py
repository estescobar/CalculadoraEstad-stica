# anova_calculator.py
import tkinter as tk
from tkinter import messagebox
from scipy import stats

class ANOVACalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de ANOVA")

        # Etiqueta para instrucciones
        self.instruction_label = tk.Label(master, text="Ingrese los datos separados por comas (un grupo por línea):", font=("Arial", 14))
        self.instruction_label.pack(pady=10)

        # Cuadro de entrada para los grupos de datos
        self.data_label = tk.Label(master, text="Datos (un grupo por línea):")
        self.data_label.pack(pady=5)
        self.data_entry = tk.Text(master, width=50, height=10)
        self.data_entry.pack(pady=5)

        # Botón para calcular ANOVA
        self.calculate_button = tk.Button(master, text="Calcular ANOVA", command=self.calculate_anova)
        self.calculate_button.pack(pady=20)

        # Área para mostrar el resultado
        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def calculate_anova(self):
        # Obtener datos de las entradas
        data = self.data_entry.get("1.0", tk.END).strip().splitlines()

        # Convertir las entradas a listas de números
        try:
            groups = [list(map(float, group.split(','))) for group in data if group]  # Ignorar líneas vacías
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos separados por comas.")
            return

        # Realizar la prueba ANOVA
        f_stat, p_value = stats.f_oneway(*groups)  # ANOVA de un solo factor
        self.result_label.config(text=f"Estadístico F: {f_stat:.4f}, p-valor: {p_value:.4f}")
