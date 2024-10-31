import tkinter as tk
from datetime import datetime

class FormularioInfoDesign(tk.Frame):  
    def __init__(self, panel_principal):
        super().__init__(panel_principal)
        self.panel_principal = panel_principal
        self.crear_interfaz()

    def crear_interfaz(self):
        # Título de la ventana de pausas activas
        tk.Label(self, text="PAUSAS ACTIVAS", font=("Roboto", 20)).pack(pady=30)

        # Hora de inicio
        tk.Label(self, text="Hora de inicio:").pack(pady=10)
        hora_inicio = tk.Label(self, text=datetime.now().strftime("%H:%M") + " AM")
        hora_inicio.pack(pady=10)

        # Hora de fin
        tk.Label(self, text="Hora de fin:").pack(pady=10)
        hora_fin = tk.Entry(self)
        hora_fin.pack(pady=10)

        # Ejercicios
        ejercicios = [
            "1| Mover las muñecas de adentro hacia afuera",
            "2| Estiramiento de brazos",
            "3| Flexiones de piernas",
            "4| Rotaciones de cuello"
        ]
        
        tk.Label(self, text="Ejercicios Disponibles:").pack(pady=10)
        for ejercicio in ejercicios:
            tk.Label(self, text=ejercicio).pack(pady=5)

        # Selector de ejercicio
        ejercicio_seleccionado = tk.StringVar(value=ejercicios[0])
        tk.Label(self, text="Selecciona un ejercicio:").pack(pady=10)
        tk.OptionMenu(self, ejercicio_seleccionado, *ejercicios).pack(pady=10)

        # Mensaje inicial
        mensaje = tk.StringVar()
        mensaje.set("Por favor, presiona 'Aceptar' para comenzar.")
        tk.Label(self, textvariable=mensaje).pack(pady=20)

        # Botón Aceptar
        def aceptar():
            mensaje.set("BIENVENIDO, ESTÁS POR EMPEZAR")

            # Actualizar el texto con el ejercicio seleccionado
            tk.Label(self, text=f"Ejercicio seleccionado: {ejercicio_seleccionado.get()}").pack(pady=20)

        tk.Button(self, text="Aceptar", command=aceptar).pack(pady=10)
        tk.Button(self, text="Cancelar", command=self.destroy).pack(pady=10)

        self.pack(fill='both', expand=True)
