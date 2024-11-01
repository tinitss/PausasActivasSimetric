import tkinter as tk
import customtkinter
from datetime import datetime
from ejercicios import Clase_ejercicios
from omitir import omitir

customtkinter.set_appearance_mode("System") 

class FormularioInfoDesign(tk.Frame):  
    def __init__(self, panel_principal, maestro):
        super().__init__(panel_principal)
        self.panel_principal = panel_principal
        self.maestro = maestro
        self.crear_interfaz()
        
    def crear_interfaz(self):
        tk.Label(self, text="PAUSAS ACTIVAS", font=("Trebuchet MS", 30)).pack(pady=1)

        # Hora de inicio
        tk.Label(self, text="Hora de inicio:").pack(pady=5)
        hora_inicio = tk.Label(self, text=datetime.now().strftime("%H:%M") + " AM")
        hora_inicio.pack(pady=10)

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

        self.ejercicio_seleccionado = tk.StringVar(value="Selecciona un ejercicio:")
        tk.OptionMenu(self, self.ejercicio_seleccionado, *ejercicios).pack(pady=10)

        self.mensaje = tk.StringVar()
        self.mensaje.set("Por favor, presiona 'Aceptar' para comenzar.")
        tk.Label(self, textvariable=self.mensaje).pack(pady=20)

        tk.Button(self, text="Iniciar", command=self.aceptar).pack(pady=10)
        tk.Button(self, text="Omitir", command=self.omitirr).pack(pady=10)

        self.pack(fill='both', expand=True)

    def aceptar(self):
        seleccion = self.ejercicio_seleccionado.get()

        # Verifica si se seleccionó un ejercicio
        if seleccion == "Selecciona un ejercicio:":
            self.mensaje.set("Es obligatorio seleccionar un ejercicio.")
            return  # Mantiene al usuario en la misma ventana

        # Limpia el panel principal
        self.maestro.limpiar_panel(self.panel_principal)

        # Diccionario que mapea los ejercicios a sus respectivos tipos y a la clase
        ejercicios_dict = {
            "Pausas saludables - Abdomen y espalda": ("abdomen", Clase_ejercicios),
            "Pausas saludables - Caderas": ("cadera", Clase_ejercicios),
            "Pausas saludables - Manos y codos": ("manos", Clase_ejercicios),
            "Pausas saludables - Cuello": ("cuello", Clase_ejercicios),
            "Pausa saludable para los ojos": ("ojos", Clase_ejercicios),
            "Pausa saludable para la voz": ("voz", Clase_ejercicios),
            "Pausa saludable - Hombros": ("hombros", Clase_ejercicios),
            "Hábitos seguros - Ergonomía": ("ergonomia", Clase_ejercicios)
        }

        # Obtiene el tipo de ejercicio y la clase del diccionario
        tipo_ejercicio, clase_ejercicio = ejercicios_dict.get(seleccion, (None, None))

        if tipo_ejercicio:  # Verifica si el tipo de ejercicio existe
            ejercicio = clase_ejercicio(self.panel_principal, self.volver_a_formulario, tipo_ejercicio)
            ejercicio.pack(fill='both', expand=True)
        else:
            self.mensaje.set("Selecciona un ejercicio válido.")

    def omitirr(self):
        self.maestro.limpiar_panel(self.panel_principal)
        omitir_panel = omitir(self.panel_principal, self.volver_a_formulario)
        omitir_panel.pack(fill='both', expand=True)

    def volver_a_formulario(self):
        self.maestro.limpiar_panel(self.panel_principal)
        self.__init__(self.panel_principal, self.maestro)