import tkinter as tk

class abdomen(tk.Frame):
    def __init__(self, panel_principal):
        super().__init__(panel_principal)
        self.panel_principal = panel_principal
        self.crear_interfaz()

    def crear_interfaz(self):
        # Aquí puedes personalizar la interfaz para el ejercicio de abdomen
        tk.Label(self, text="Ejercicio de Abdomen", font=("Trebuchet MS", 20)).pack(pady=10)
        tk.Label(self, text="Realiza ejercicios de estiramiento para el abdomen.").pack(pady=20)

        # Aquí puedes añadir más elementos relacionados con el ejercicio

        tk.Button(self, text="Cerrar", command=self.destroy).pack(pady=10)


