import customtkinter as ctk
import re
from customtkinter import CTkFont
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_MENU_LATERAL
import util.util_imagenes as util_img
from formularios.form_info_design import FormularioInfoDesign
from formularios.form_sitio_construccion import FormularioSitioConstruccionDesign
from formularios.form_graficas_design import FormularioGraficasDesign


class FormularioMaestroDesign(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.MinisterioTrabajo = util_img.leer_imagen("./imagenes/MinisterioTrabajo.jpg", (100, 100))
        self.Perfil2 = util_img.leer_imagen("./imagenes/Perfil2.png", (180, 100))
        self.Salud = util_img.leer_imagen("./imagenes/Salud.jpg", (100, 100))
        self.logica()

    def logica(self):
        def paneles():
            self.grid_columnconfigure(0, weight=0)  # Columna del menú lateral
            self.grid_columnconfigure(1, weight=1)  # Columna del cuerpo principal
            self.grid_rowconfigure(1, weight=1)

            self.barra_superior = ctk.CTkFrame(self, fg_color=COLOR_BARRA_SUPERIOR, height=100)
            self.barra_superior.grid(row=0, column=0, columnspan=2, sticky="nsew")
            self.barra_superior.grid_propagate(False)

            self.menu_lateral = ctk.CTkFrame(self, fg_color=COLOR_MENU_LATERAL, width=225)
            self.menu_lateral.grid(row=1, column=0, sticky="nsew")

            self.cuerpo_principal = ctk.CTkFrame(self, fg_color=COLOR_CUERPO_PRINCIPAL)
            self.cuerpo_principal.grid(row=1, column=1, sticky="nsew")

        def controles_barra_superior():
            self.buttonMenuLateral = ctk.CTkButton(self.barra_superior, text="\uf0c9",
                command=self.toggle_panel, fg_color=COLOR_BARRA_SUPERIOR, text_color="white", width=50, height=45)
            self.buttonMenuLateral.pack(side=ctk.LEFT, padx=10)

            self.labelTitulo = ctk.CTkLabel(self.barra_superior, text="PAUSAS ACTIVAS", text_color="white",
                                            font=CTkFont(family="Kaboom", size=45, weight="bold"))
            self.labelTitulo.pack(side=ctk.LEFT, padx=5)

            self.labelEmail = ctk.CTkLabel(self.barra_superior, text="atencionalcliente@mintrabajo.com.co",
                                           text_color="white", font=CTkFont(family="Questrial", size=17, weight="bold"))
            self.labelEmail.pack(side=ctk.RIGHT, padx=20)

        def controles_menu_lateral():
            ancho_menu = 225
            alto_menu = 80
            font_awesome = CTkFont(family="Questrial", size=20)

            self.labelPerfil = ctk.CTkLabel(self.menu_lateral, image=self.Perfil2, text="")
            self.labelPerfil.pack(side=ctk.TOP, pady=10, anchor="center")

            self.buttonPausas = ctk.CTkButton(self.menu_lateral)
            self.buttonConfig = ctk.CTkButton(self.menu_lateral)
            self.buttonAyuda = ctk.CTkButton(self.menu_lateral)

            buttons_info = [
                ("Inicio", "\uf03e", self.buttonPausas, self.abrir_panel_inicio),
                ("Configuración", "\uf03e", self.buttonConfig, self.abrir_panel_en_construccion),
                ("Ayuda", "\uf03e", self.buttonAyuda, self.abrir_panel_graficas)
            ]

            for text, icon, button, comando in buttons_info:
                self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu, comando)

        paneles()
        controles_barra_superior()
        controles_menu_lateral()
        self.controles_cuerpo()

    def controles_cuerpo(self):
        font_negrilla = ctk.CTkFont(weight="bold", size=17, family="Questrial")
        font_bienvenida = ctk.CTkFont(family="Kaboom", size=70)

        # Aseguramos que el contenido de cuerpo_principal se centre horizontalmente
        self.cuerpo_principal.grid_columnconfigure(0, weight=1)
        self.cuerpo_principal.grid_rowconfigure(0, weight=1)

        self.labelTitulo = ctk.CTkLabel(self.cuerpo_principal, text="BIENVENIDO", font=font_bienvenida)
        self.labelTitulo.grid(row=0, column=0, pady=(80, 0))

        # Frame intermedio que centra el contenido
        frame_centrador = ctk.CTkFrame(self.cuerpo_principal, fg_color=COLOR_BARRA_SUPERIOR)
        frame_centrador.grid(row=1, column=0, sticky="nsew", pady=(0, 100))
        self.cuerpo_principal.grid_rowconfigure(1, weight=1)
        self.cuerpo_principal.grid_columnconfigure(0, weight=1)
        frame_centrador.grid_columnconfigure(0, weight=1)

        contenedor = ctk.CTkFrame(frame_centrador, fg_color=COLOR_CUERPO_PRINCIPAL)
        contenedor.grid(row=0, column=0)

        contenedor.columnconfigure(0, weight=1)
        contenedor.columnconfigure(1, weight=0)
        contenedor.columnconfigure(2, weight=0)

        self.nombre_var = ctk.StringVar()
        self.nombre_var.trace_add("write", lambda *args: self.nombre_var.set(self.nombre_var.get().upper()))

        self.labelNombre = ctk.CTkLabel(contenedor, text="NOMBRE", font=font_negrilla)
        self.labelNombre.grid(row=0, column=1, padx=(20, 0))

        self.entryNombre = ctk.CTkEntry(
            contenedor, placeholder_text="Escribe tu nombre",
            textvariable=self.nombre_var, width=210, height=40, font=font_negrilla
        )
        self.entryNombre.grid(row=1, column=1, padx=(10, 110), sticky="w")

        self.labelEspecialidad = ctk.CTkLabel(contenedor, text="ESPECIALIDAD", font=font_negrilla)
        self.labelEspecialidad.grid(row=0, column=2, pady=5, padx=30, sticky="e")

        especialidad = ["MEDICINA", "OPTO", "FONO", "PSICO"]
        self.especialidad_seleccionada = ctk.StringVar(value="Selecciona una \n especialidad:")

        especialidad_menu = ctk.CTkOptionMenu(
            contenedor,
            variable=self.especialidad_seleccionada,
            values=especialidad,
            width=170,
            height=40,
            font=font_negrilla,
            dropdown_fg_color="lightblue",
            dropdown_text_color="black",
            button_color=COLOR_BARRA_SUPERIOR,
            button_hover_color=COLOR_MENU_LATERAL
        )
        especialidad_menu.grid(row=1, column=2, padx=10, sticky="w")

        self.labelFeedback = ctk.CTkLabel(contenedor, text="", font=font_negrilla, text_color="#c0002b")
        self.labelFeedback.grid(row=3, column=0, columnspan=3, pady=10)

        def aceptar():
            seleccion = self.especialidad_seleccionada.get()
            nombre = self.entryNombre.get()

            if not nombre:
                self.labelFeedback.configure(text="El nombre es obligatorio.")
                return

            if not re.match(r"^[A-Za-zñÑ\s]+$", nombre):
                self.labelFeedback.configure(text="El nombre solo puede contener letras.")
                return

            if seleccion == "Selecciona una \n especialidad:":
                self.labelFeedback.configure(text="Es obligatorio seleccionar una especialidad.")
                return

            self.limpiar_panel(self.cuerpo_principal)
            self.abrir_panel_info(nombre)

        ctk.CTkButton(
            contenedor, text="Iniciar", command=aceptar, font=font_negrilla,
            fg_color=COLOR_BARRA_SUPERIOR, hover_color=COLOR_MENU_LATERAL,
            text_color="white", width=120, height=40
        ).grid(row=2, column=0, columnspan=3, pady=20, padx=200)


    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.configure(text=f" {icon}  {text}", anchor="center", font=font_awesome,
                         fg_color=COLOR_MENU_LATERAL, text_color="white", width=ancho_menu, height=alto_menu,
                         command=comando)
        button.pack(side=ctk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.configure(fg_color=COLOR_MENU_CURSOR_ENCIMA)

    def on_leave(self, event, button):
        button.configure(fg_color=COLOR_MENU_LATERAL)

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.grid_forget()
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
        else:
            self.menu_lateral.grid(row=1, column=0, sticky="nsew")
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)

    def abrir_panel_inicio(self):
        self.limpiar_panel(self.cuerpo_principal)
        self.controles_cuerpo()
        
    def abrir_panel_info(self, nombre):
        self.limpiar_panel(self.cuerpo_principal)
        formulario = FormularioInfoDesign(self.cuerpo_principal, self, nombre)  
        formulario.grid(row=0, column=0, sticky="nsew")


    def abrir_panel_en_construccion(self):
        formulario_sitio = FormularioSitioConstruccionDesign(self.cuerpo_principal)
        formulario_sitio.grid(row=0, column=0, sticky="nsew")

    def abrir_panel_graficas(self):
        formulario_graficas = FormularioGraficasDesign(self.cuerpo_principal)
        formulario_graficas.grid(row=0, column=0, sticky="nsew")

    def limpiar_panel(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
