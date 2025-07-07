import customtkinter as ctk
from customtkinter import CTkFont
from datetime import datetime
from ejercicios import Clase_ejercicios
from omitir import omitir
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_LATERAL


class FormularioInformacion(ctk.CTkFrame):  
    def __init__(self, panel_principal, maestro, nombre):
        super().__init__(panel_principal)
        self.panel_principal = panel_principal
        self.maestro = maestro
        self.nombre = nombre

        # Usa grid para centrar esta vista
        self.grid(row=0, column=0, sticky="nsew")
        self.panel_principal.grid_rowconfigure(0, weight=1)
        self.panel_principal.grid_columnconfigure(0, weight=1)
        
        self.crear_interfaz()
        
    def limpiar_panel(self):
        for widget in self.panel_principal.winfo_children():
            widget.grid_forget()

    def crear_interfaz(self):
        # Configura este frame principal (self) para centrar
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Cuerpo centrado
        cuerpo_centrado = ctk.CTkFrame(self, fg_color=COLOR_CUERPO_PRINCIPAL)
        cuerpo_centrado.grid(row=0, column=0, sticky="nsew")
        cuerpo_centrado.grid_rowconfigure(0, weight=1)
        cuerpo_centrado.grid_columnconfigure(0, weight=1)

        # Contenedor con contenido
        contenedor = ctk.CTkFrame(cuerpo_centrado, fg_color=COLOR_CUERPO_PRINCIPAL)
        contenedor.grid(row=0, column=0, sticky="nsew", pady=(35, 0))
        contenedor.columnconfigure((0, 1, 2), weight=1)

        # Fuentes
        font_nombre = CTkFont(family="Kaboom", size=50)
        font_info = CTkFont(family="Kaboom", size=40)
        font_negrilla = CTkFont(weight="bold", size=17, family="Questrial")

        # Nombre
        self.labelNombre = ctk.CTkLabel(contenedor, text=self.nombre, font=font_nombre, wraplength=500)
        self.labelNombre.grid(row=0, column=0, columnspan=3, pady=(10, 30), sticky="n")

        # Subtítulo
        self.labelPausas = ctk.CTkLabel(contenedor, text="ES MOMENTO DE HACER \n PAUSAS ACTIVAS", font=font_info)
        self.labelPausas.grid(row=1, column=0, columnspan=3, pady=10, sticky="n")

        

        # Menú de ejercicios
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
        self.ejercicio_seleccionado = ctk.StringVar(value="Selecciona un ejercicio:")
        ejercicio_menu = ctk.CTkOptionMenu(
            contenedor,
            variable=self.ejercicio_seleccionado,
            values=ejercicios,
            width=250,
            height=40,
            font=font_negrilla,
            dropdown_fg_color="lightblue",
            dropdown_text_color="black",
            button_color=COLOR_BARRA_SUPERIOR,
            button_hover_color=COLOR_MENU_LATERAL
        )
        ejercicio_menu.grid(row=3, column=0, columnspan=3, pady=10)

        # Mensaje
        self.mensaje = ctk.StringVar(value="Por favor, presiona 'Iniciar' para comenzar.")
        self.labelMensaje = ctk.CTkLabel(contenedor, textvariable=self.mensaje, font=font_negrilla)
        self.labelMensaje.grid(row=4, column=0, columnspan=3, pady=10)

        # Botones
        ctk.CTkButton(contenedor, text="Volver", command=self.volver_a_formulario, font=font_negrilla,
                      fg_color=COLOR_BARRA_SUPERIOR, hover_color=COLOR_MENU_LATERAL,
                      text_color="white", width=120, height=40).grid(row=5, column=0, pady=10)
        
        ctk.CTkButton(contenedor, text="Iniciar", command=self.aceptar, font=font_negrilla,
                      fg_color=COLOR_BARRA_SUPERIOR, hover_color=COLOR_MENU_LATERAL,
                      text_color="white", width=120, height=40).grid(row=5, column=1, pady=10)
        
        ctk.CTkButton(contenedor, text="Omitir", command=self.omitir_pausa, font=font_negrilla,
                      fg_color="#c0002b", text_color="white", width=120, height=40).grid(row=5, column=2, pady=10)
        
        
        # Hora de inicio (etiqueta vacía al inicio)
        self.hora_inicio = ctk.CTkLabel(contenedor, text="", font=font_negrilla)
        self.hora_inicio.grid(row=6, column=0, columnspan=3, pady=(80, 0))

        # Inicia el reloj en tiempo real
        self.actualizar_hora()
        
    def actualizar_hora(self):
        hora_actual = datetime.now().strftime("%H:%M:%S")
        self.hora_inicio.configure(text="Hora de inicio: " + hora_actual)
        self.after(1000, self.actualizar_hora)


    def aceptar(self):
        seleccion = self.ejercicio_seleccionado.get()

        if seleccion == "Selecciona un ejercicio:":
            self.mensaje.set("Es obligatorio seleccionar un ejercicio")
            self.labelMensaje.configure(text_color="#c0002b")
            return

        # Limpia el panel principal y carga el ejercicio
        self.maestro.limpiar_panel(self.panel_principal)
        tipo_ejercicio, clase_ejercicio = {
            "Pausas saludables - Abdomen y espalda": ("abdomen", Clase_ejercicios),
            "Pausas saludables - Caderas": ("cadera", Clase_ejercicios),
            "Pausas saludables - Manos y codos": ("manos", Clase_ejercicios),
            "Pausas saludables - Cuello": ("cuello", Clase_ejercicios),
            "Pausa saludable para los ojos": ("ojos", Clase_ejercicios),
            "Pausa saludable para la voz": ("voz", Clase_ejercicios),
            "Pausa saludable - Hombros": ("hombros", Clase_ejercicios),
            "Hábitos seguros - Ergonomía": ("ergonomia", Clase_ejercicios)
        }.get(seleccion, (None, None))

        if tipo_ejercicio:
            ejercicio = clase_ejercicio(self.panel_principal, self.volver_a_formulario, tipo_ejercicio, self.maestro, self.nombre)
            ejercicio.grid(row=5, column=0, columnspan=3, pady=10)
        else:
            self.mensaje.set("Selecciona un ejercicio válido.")

    def omitir_pausa(self):
        self.maestro.limpiar_panel(self.panel_principal)
        omitir_panel = omitir(self.panel_principal, self.volver_a_formulario)
        omitir_panel.grid(row=5, column=0, columnspan=3, pady=10)

    def volver_a_formulario(self):
        self.maestro.abrir_panel_inicio()
