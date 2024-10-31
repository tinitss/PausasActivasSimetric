import tkinter as tk

class ejercicioss(tk.Frame):
    def __init__(self, panel_principal, callback_volver, tipo_ejercicio):
        super().__init__(panel_principal)
        self.panel_principal = panel_principal
        self.callback_volver = callback_volver
        self.tipo_ejercicio = tipo_ejercicio
        self.crear_interfaz()

    def crear_interfaz(self):
        if self.tipo_ejercicio == "abdomen":
            self.abdomen()
        elif self.tipo_ejercicio == "cadera":
            self.cadera()

        # Button to return to the previous menu
        tk.Button(self, text="Volver", command=self.volver).pack(pady=10)

    def abdomen(self):
        tk.Label(self, text="Ejercicio de Abdomen", font=("Trebuchet MS", 20)).pack(pady=10)
        tk.Label(self, text="Realiza ejercicios de estiramiento para el abdomen.").pack(pady=20)

    def cadera(self):
        tk.Label(self, text="Ejercicio de Cadera", font=("Trebuchet MS", 20)).pack(pady=10)
        tk.Label(self, text="Realiza ejercicios de estiramiento para el cadera.").pack(pady=20)

    def volver(self):
        if self.callback_volver:
            self.callback_volver()
        self.destroy()





