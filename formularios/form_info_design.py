import customtkinter as ctk
from customtkinter import CTkFont
from datetime import datetime
from ejercicios import Clase_ejercicios
from omitir import omitir
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_LATERAL


class FormularioInfoDesign(ctk.CTkFrame):  
    def __init__(self, panel_principal, maestro, nombre):
        super().__init__(panel_principal)
        self.panel_principal = panel_principal
        self.maestro = maestro
        self.nombre = nombre
        self.crear_interfaz()
        
    def limpiar_panel(self):
        for widget in self.panel_principal.winfo_children():
            widget.grid_forget()

    def crear_interfaz(self):
        # Configuración del área principal
        self.cuerpo_principal = ctk.CTkFrame(self, fg_color=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=ctk.RIGHT, fill='both', expand=True)
        
        self.omitir_panel = omitir(self.panel_principal, self.volver_a_formulario)
        
        font_bienvenida = CTkFont(family="Kaboom", size=70)
        font_nombre = CTkFont(family="Kaboom", size=40)  # Fuente para el nombre
        font_negrilla = CTkFont(weight="bold", size=17, family="Questrial")

        # Título principal "HOLA"
        self.labelTitulo = ctk.CTkLabel(self.cuerpo_principal, text="HOLA", font=font_bienvenida)
        self.labelTitulo.grid(row=0, column=0, columnspan=3, pady=(4, 10), padx=20, sticky="n")

        # Nombre en un tamaño de fuente diferente
        self.labelNombre = ctk.CTkLabel(
            self.cuerpo_principal,
            text=self.nombre,
            font=font_nombre,
            wraplength=320  # Ajusta este valor según el ancho que prefieras
        )
        self.labelNombre.grid(row=1, column=0, columnspan=3, pady=(0, 0), padx=20, sticky="n")
        
        
        # Contenedor de elementos
        contenedor = ctk.CTkFrame(self.cuerpo_principal, fg_color=COLOR_CUERPO_PRINCIPAL)
        contenedor.grid(row=1, column=0, padx=20, pady=90, sticky="nsew")
        contenedor.columnconfigure(0, weight=1)
        contenedor.columnconfigure(1, weight=1)
        contenedor.columnconfigure(2, weight=1)

        # Subtítulo "Pausas Activas"
        self.labelPausas = ctk.CTkLabel(contenedor, text="ES MOMENTO DE HACER \n PAUSAS ACTIVAS", font=CTkFont(family="Kaboom", size=45))
        self.labelPausas.grid(row=0, column=1, pady=10, padx=20, sticky="n")

        # Mostrar la hora de inicio
        self.hora_inicio = ctk.CTkLabel(contenedor, text="Hora de inicio: " + datetime.now().strftime("%H:%M"), font=font_negrilla)
        self.hora_inicio.grid(row=1, column=1, pady=5, padx=60, sticky="n")

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
                width=170,
                height=40,
                font=font_negrilla,
                dropdown_fg_color="lightblue",
                dropdown_text_color="black",
                button_color=COLOR_BARRA_SUPERIOR,
                button_hover_color=COLOR_MENU_LATERAL)
            
        ejercicio_menu.grid(row=1, column=1, padx=10, sticky="n")

        # Mensaje de retroalimentación
        self.mensaje = ctk.StringVar(value="Por favor, presiona 'Iniciar' para comenzar.")
        self.labelMensaje = ctk.CTkLabel(contenedor, textvariable=self.mensaje, font=font_negrilla)
        self.labelMensaje.grid(row=3, column=0, columnspan=3, pady=20)

        # Botones "Iniciar" y "Omitir"
        ctk.CTkButton(contenedor, text="Iniciar", command=self.aceptar, font=font_negrilla, fg_color=COLOR_BARRA_SUPERIOR, 
                      hover_color=COLOR_MENU_LATERAL, text_color="white", width=120, height=40).grid(row=4, column=0, pady=10, padx=20)
        ctk.CTkButton(contenedor, text="Volver", command=self.volver_a_formulario, font=font_negrilla, fg_color=COLOR_BARRA_SUPERIOR, 
                      hover_color=COLOR_MENU_LATERAL, text_color="white", width=120, height=40).grid(row=4, column=1, pady=10, padx=20)
        ctk.CTkButton(contenedor, text="Omitir", command=self.omitir_pausa, font=font_negrilla, fg_color="#c0002b",
                      text_color="white", width=120, height=40).grid(row=4, column=2, pady=10, padx=20)

        # Configurar grid en lugar de pack para el contenedor principal
        self.grid(row=0, column=0, sticky="nsew")

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
        


