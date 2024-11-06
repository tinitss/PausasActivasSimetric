import customtkinter as ctk
from customtkinter import CTkFont
from datetime import datetime
from ejercicios import Clase_ejercicios
from omitir import omitir

class FormularioInfoDesign(ctk.CTkFrame):  
    def __init__(self, panel_principal, maestro):
        super().__init__(panel_principal)
        self.panel_principal = panel_principal
        self.maestro = maestro
        self.crear_interfaz()

    def crear_interfaz(self):
        # Título
        ctk.CTkLabel(self, text="PAUSAS ACTIVAS", font=CTkFont(family="Trebuchet MS", size=30)).pack(pady=1)

        # Hora de inicio
        ctk.CTkLabel(self, text="Hora de inicio:").pack(pady=5)
        hora_inicio = ctk.CTkLabel(self, text=datetime.now().strftime("%H:%M") + " AM")
        hora_inicio.pack(pady=10)

        # Lista de ejercicios
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

        # Menú de opciones de ejercicios
        self.ejercicio_seleccionado = ctk.StringVar(value="Selecciona un ejercicio:")
        ejercicio_menu = ctk.CTkOptionMenu(self, variable=self.ejercicio_seleccionado, values=ejercicios)
        ejercicio_menu.pack(pady=10)

        # Mensaje inicial
        self.mensaje = ctk.StringVar(value="Por favor, presiona 'Aceptar' para comenzar.")
        ctk.CTkLabel(self, textvariable=self.mensaje).pack(pady=20)

        # Botones de "Iniciar" y "Omitir"
        ctk.CTkButton(self, text="Iniciar", command=self.aceptar).pack(pady=10)
        ctk.CTkButton(self, text="Omitir", command=self.omitirr).pack(pady=10)

        self.pack(fill='both', expand=True)

    def aceptar(self):
        seleccion = self.ejercicio_seleccionado.get()

        # Verifica si se seleccionó un ejercicio
        if seleccion == "Selecciona un ejercicio:":
            self.mensaje.set("Es obligatorio seleccionar un ejercicio.")
            return

        # Limpia el panel principal
        self.maestro.limpiar_panel(self.panel_principal)

        # Diccionario de ejercicios
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

        # Obtiene el tipo de ejercicio y la clase correspondiente
        tipo_ejercicio, clase_ejercicio = ejercicios_dict.get(seleccion, (None, None))

        if tipo_ejercicio:
            ejercicio = clase_ejercicio(self.panel_principal, self.volver_a_formulario, tipo_ejercicio)
            ejercicio.pack(fill='both', expand=True)
        else:
            self.mensaje.set("Selecciona un ejercicio válido.")

    def omitirr(self):
        # Limpia el panel principal y muestra el panel de omitir
        self.maestro.limpiar_panel(self.panel_principal)
        omitir_panel = omitir(self.panel_principal, self.volver_a_formulario)
        omitir_panel.pack(fill='both', expand=True)

    def volver_a_formulario(self):
        # Restaura el formulario principal
        self.maestro.limpiar_panel(self.panel_principal)
        self.__init__(self.panel_principal, self.maestro)
