import customtkinter as ctk
import re
from customtkinter import CTkFont
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_MENU_LATERAL
import util.util_imagenes as util_img
from formularios.form_info_design import FormularioInfoDesign
from formularios.form_sitio_construccion import FormularioSitioConstruccionDesign
from formularios.form_graficas_design import FormularioGraficasDesign
#from formularios.principal import DatosPersonales


class FormularioMaestroDesign(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.Simetric_logo = util_img.leer_imagen("./imagenes/Simetric_logo.jpg", (100, 100))
        self.Perfil2 = util_img.leer_imagen("./imagenes/Perfil2.png", (100, 100))
        self.Salud = util_img.leer_imagen("./imagenes/Salud.jpg", (100, 100))
        self.logica()

    def logica(self):
        def paneles():
            self.barra_superior = ctk.CTkFrame(self, fg_color=COLOR_BARRA_SUPERIOR, height=100)
            self.barra_superior.pack(side=ctk.TOP, fill='x')
            self.barra_superior.pack_propagate(False)

            self.menu_lateral = ctk.CTkFrame(self, fg_color=COLOR_MENU_LATERAL, width=20)
            self.menu_lateral.pack(side=ctk.LEFT, fill='both', expand=False)

            self.cuerpo_principal = ctk.CTkFrame(self, fg_color=COLOR_CUERPO_PRINCIPAL)
            self.cuerpo_principal.pack(side=ctk.RIGHT, fill='both', expand=True)

        def controles_barra_superior():
            #font_awesome = CTkFont(family="Kaboom", size=12)

            self.buttonMenuLateral = ctk.CTkButton(self.barra_superior, text="\uf0c9",
                command=self.toggle_panel, fg_color=COLOR_BARRA_SUPERIOR, text_color="white", width=50, height=45)
            self.buttonMenuLateral.pack(side=ctk.LEFT, padx=10)

            self.labelTitulo = ctk.CTkLabel(self.barra_superior, text="SIMETRIC", text_color="white", font=CTkFont(family="Kaboom", size=45, weight="bold"))
            self.labelTitulo.pack(side=ctk.LEFT, padx=5)

            self.labelEmail = ctk.CTkLabel(self.barra_superior, text="atencionalcliente@simetric.com.co", text_color="white", font=CTkFont(family="Questrial", size=17, weight="bold"))
            self.labelEmail.pack(side=ctk.RIGHT, padx=20)

        def controles_menu_lateral():
            ancho_menu = 225
            alto_menu = 45
            font_awesome = CTkFont(family="Questrial", size=20)

            self.labelPerfil = ctk.CTkLabel(self.menu_lateral, image=self.Perfil2, text="")
            self.labelPerfil.pack(side=ctk.TOP, pady=10, anchor="center")

            self.buttonPausas = ctk.CTkButton(self.menu_lateral)
            self.buttonConfig = ctk.CTkButton(self.menu_lateral)
            self.buttonAyuda = ctk.CTkButton(self.menu_lateral)

            buttons_info = [
                ("Pausas", "\uf109", self.buttonPausas, self.abrir_panel_info),
                ("Configuración", "\uf007", self.buttonConfig, self.abrir_panel_en_construccion),
                ("Ayuda", "\uf03e", self.buttonAyuda, self.abrir_panel_graficas)
            ]

            for text, icon, button, comando in buttons_info:
                self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu, comando)

        def controles_cuerpo():
            font_negrilla = ctk.CTkFont(weight="bold", size=17, family="Questrial")
            font_bienvenida = ctk.CTkFont(family="Kaboom", size=70)

            self.labelTitulo = ctk.CTkLabel(self.cuerpo_principal, text="BIENVENIDO", font=font_bienvenida)
            self.labelTitulo.grid(row=0, column=0, columnspan=3, pady=65, padx=60, sticky="n")

            contenedor = ctk.CTkFrame(self.cuerpo_principal, fg_color=COLOR_CUERPO_PRINCIPAL)
            contenedor.grid(row=0, column=0, padx=110, pady=180, sticky="nsew")
            contenedor.columnconfigure(0, weight=1)
            contenedor.columnconfigure(1, weight=1)
            contenedor.columnconfigure(2, weight=1)

            # Create a StringVar for the entry field
            self.nombre_var = ctk.StringVar()

            # Add a trace to convert text to uppercase
            self.nombre_var.trace_add("write", lambda *args: self.nombre_var.set(self.nombre_var.get().upper()))

            # Label and Entry for the name input
            self.labelNombre = ctk.CTkLabel(contenedor, text="NOMBRE", font=font_negrilla)
            self.labelNombre.grid(row=0, column=1, pady=5, padx=60, sticky="n")

            self.entryNombre = ctk.CTkEntry(
                contenedor,
                placeholder_text="Escribe tu nombre",
                textvariable=self.nombre_var,  # Set the variable to the entry field
                width=210,
                height=40,
                font=font_negrilla
            )
            self.entryNombre.grid(row=1, column=1, padx=(10, 110), sticky="w")


            self.labelEspecialidad = ctk.CTkLabel(contenedor, text="ESPECIALIDAD", font=font_negrilla)
            self.labelEspecialidad.grid(row=0, column=2, pady=5, padx=10, sticky="e")

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

                # Limpia el panel antes de abrir el siguiente formulario
                self.limpiar_panel(self.cuerpo_principal)
                self.abrir_panel_info(nombre)  # Aquí se debe abrir el formulario de información


            ctk.CTkButton(contenedor, text="Iniciar", command=aceptar, font=font_negrilla, fg_color=COLOR_BARRA_SUPERIOR, hover_color=COLOR_MENU_LATERAL,
                          text_color="white", width=120, height=40).grid(row=2, column=0, columnspan=3, pady=20, padx=200)

        paneles()
        controles_barra_superior()
        controles_menu_lateral()
        controles_cuerpo()

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
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=ctk.LEFT, fill='both', expand=False)

    def abrir_panel_info(self, nombre):
        formulario = FormularioInfoDesign(self.cuerpo_principal, self, nombre)
        formulario.pack(fill="both", expand=True)
        

    def abrir_panel_en_construccion(self):
        formulario_sitio = FormularioSitioConstruccionDesign(self.cuerpo_principal)
        formulario_sitio.pack(fill="both", expand=True)

    def abrir_panel_graficas(self):
        formulario_graficas = FormularioGraficasDesign(self.cuerpo_principal)
        formulario_graficas.pack(fill="both", expand=True)

    def limpiar_panel(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

