import tkinter as tk
from tkinter import messagebox
from scipy import stats

class TTestCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Prueba t de Student")
        
        self.instruction_label = tk.Label(master, text="Ingrese los datos separados por comas:", font=("Arial", 14))
        self.instruction_label.pack(pady=10)

        self.data1_label = tk.Label(master, text="Conjunto de Datos 1:")
        self.data1_label.pack(pady=5)
        self.data1_entry = tk.Entry(master, width=50)
        self.data1_entry.pack(pady=5)

        self.data2_label = tk.Label(master, text="Conjunto de Datos 2:")
        self.data2_label.pack(pady=5)
        self.data2_entry = tk.Entry(master, width=50)
        self.data2_entry.pack(pady=5)

        self.calculate_button = tk.Button(master, text="Calcular Prueba t", command=self.calculate_t_test)
        self.calculate_button.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
        
        self.quit_button = tk.Button(master, text="Salir", command=master.quit)
        self.quit_button.pack(pady=20)
        

    def calculate_t_test(self):
        data1 = self.data1_entry.get()
        data2 = self.data2_entry.get()

        try:
            data1 = list(map(float, data1.split(',')))
            data2 = list(map(float, data2.split(',')))
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos separados por comas.")
            return

        t_stat, p_value = stats.ttest_ind(data1, data2) 
        self.result_label.config(text=f"Estadístico t: {t_stat:.4f}, p-valor: {p_value:.4f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TTestCalculator(root)
    root.mainloop()
