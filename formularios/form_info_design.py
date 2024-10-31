import tkinter as tk
import customtkinter
from datetime import datetime
from ejercicios.ejercicios import abdomen


customtkinter.set_appearance_mode("System") 

class FormularioInfoDesign(tk.Frame):  
    def __init__(self, panel_principal, maestro):
        super().__init__(panel_principal)
        self.panel_principal = panel_principal
        self.maestro = maestro
        self.crear_interfaz()
        

    def crear_interfaz(self):
        # Título de la ventana de pausas activas
        tk.Label(self, text="PAUSAS ACTIVAS", font=("Trebuchet MS", 30)).pack(pady=1)

        # Hora de inicio
        tk.Label(self, text="Hora de inicio:").pack(pady=5)
        hora_inicio = tk.Label(self, text=datetime.now().strftime("%H:%M") + " AM")
        hora_inicio.pack(pady=10)

        # Hora de fin
        #tk.Label(self, text="Hora de fin:").pack(pady=10)
        #hora_fin = tk.Entry(self)
        #zhora_fin.pack(pady=10)

        # Ejercicios
        ejercicios = [
            "Pausas saludables - Abdomen y espalda",
            "Pausas saludables - Caderas",
            "Pausas saludables - Manos y codos",
            "Pausas saludables - Cuello",
            "Pausa saludable para los ojos",
            "Pausa saludable para la voz",
            "Pausa saludable - Hombros",
            "Hábitos seguros - Ergonomía"
        ]

        ejercicio_seleccionado = tk.StringVar(value="Selecciona un ejercicio:")
        tk.OptionMenu(self, ejercicio_seleccionado, *ejercicios).pack(pady=10)

        mensaje = tk.StringVar()
        mensaje.set("Por favor, presiona 'Aceptar' para comenzar.")
        tk.Label(self, textvariable=mensaje).pack(pady=20)

        def aceptar():
            if ejercicio_seleccionado.get() == "Pausas saludables - Abdomen y espalda":
                self.maestro.limpiar_panel(self.panel_principal)  
                ejercicio_abdomen = abdomen(self.panel_principal)  
                ejercicio_abdomen.pack(fill='both', expand=True)
            else:
                mensaje.set("Seleccione un ejercicio válido para continuar.")

        def cancelar():
            mensaje.set("VAS A SALIR DEL SISTEMA")


        tk.Button(self, text="Aceptar", command=aceptar).pack(pady=10)
        tk.Button(self, text="Cancelar", command=cancelar).pack(pady=10)

        self.pack(fill='both', expand=True)


