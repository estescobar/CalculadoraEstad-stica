# main.py
import tkinter as tk
from chi_squared import ChiSquaredTestCalculator
from kruskal import KruskalWallisTestCalculator
from mann_whitney import MannWhitneyTestCalculator
from shapiro import ShapiroWilkTestCalculator
from spearman_correl import SpearmanCorrelationCalculator
from t_test import TTestCalculator 
from anova import ANOVACalculator  # Importa la clase ANOVACalculator
from pearson import PearsonCorrelationCalculator
from wilcoxon import WilcoxonTestCalculator  # Importa la clase PearsonCorrelationCalculator

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Estadística")
        self.create_main_menu()

    def create_main_menu(self):
        # Limpiar el contenido de la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Título
        self.title_label = tk.Label(self.root, text="Selecciona una calculadora estadística", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Títulos de las columnas
        self.parametric_label = tk.Label(self.root, text="Paramétrico", font=("Arial", 14))
        self.parametric_label.grid(row=1, column=0, pady=(10, 0))

        self.non_parametric_label = tk.Label(self.root, text="No Paramétricos", font=("Arial", 14))
        self.non_parametric_label.grid(row=1, column=1, pady=(10, 0))

        # Crear botones para cada calculadora
        self.create_buttons()

        # Salir
        self.quit_button = tk.Button(self.root, text="Salir", command=self.root.quit)
        self.quit_button.grid(row=10, column=0, columnspan=2, pady=20)

    def create_buttons(self):
        # Definir configuraciones de botones
        parametric_tests = [
            ("Prueba t de Student", self.open_t_test_calculator),
            ("ANOVA", self.open_anova_calculator),
            ("Correlación de Pearson", self.open_pearson_calculator),
            ("Prueba de Shapiro-Wilk", self.open_shapiro_calculator),
        ]

        non_parametric_tests = [
            ("Prueba de Wilcoxon", self.open_wilcoxon_calculator),
            ("Prueba de Mann-Whitney", self.open_mann_whitney_calculator),
            ("Prueba de Kruskal-Wallis", self.open_kruskal_wallis_calculator),
            ("Prueba Chi-Cuadrado", self.open_chi_squared_calculator),
            ("Correlación de Spearman", self.open_spearman_calculator),
        ]

        # Colocar botones de tests paramétricos en la primera columna
        for i, (text, command) in enumerate(parametric_tests):
            button = tk.Button(self.root, text=text, command=command)
            button.grid(row=i + 2, column=0, pady=5, padx=5)

        # Colocar botones de tests no paramétricos en la segunda columna
        for i, (text, command) in enumerate(non_parametric_tests):
            button = tk.Button(self.root, text=text, command=command)
            button.grid(row=i + 2, column=1, pady=5, padx=5)

    def open_calculator(self, calculator_class):
        # Cierra la ventana actual y abre la calculadora
        self.root.withdraw()  # Oculta la ventana principal
        new_window = tk.Toplevel(self.root)
        calculator = calculator_class(new_window)
        new_window.protocol("WM_DELETE_WINDOW", self.on_calculator_close)
        
    def on_calculator_close(self):
        self.root.deiconify()  # Vuelve a mostrar la ventana principal
        self.create_main_menu()  # Opcional: reinicia el menú

    def open_t_test_calculator(self):
        self.open_calculator(TTestCalculator)

    def open_anova_calculator(self):
        self.open_calculator(ANOVACalculator)

    def open_pearson_calculator(self):
        self.open_calculator(PearsonCorrelationCalculator)

    def open_shapiro_calculator(self):
        self.open_calculator(ShapiroWilkTestCalculator)

    def open_wilcoxon_calculator(self):
        self.open_calculator(WilcoxonTestCalculator)

    def open_mann_whitney_calculator(self):
        self.open_calculator(MannWhitneyTestCalculator)

    def open_kruskal_wallis_calculator(self):
        self.open_calculator(KruskalWallisTestCalculator)

    def open_chi_squared_calculator(self):
        self.open_calculator(ChiSquaredTestCalculator)

    def open_spearman_calculator(self):
        self.open_calculator(SpearmanCorrelationCalculator)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
