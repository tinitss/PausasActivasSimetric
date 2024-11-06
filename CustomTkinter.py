import customtkinter as ctk
import re
from customtkinter import CTkFont  
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_MENU_LATERAL
import util.util_imagenes as util_img
from formularios.form_info_design import FormularioInfoDesign
from formularios.form_sitio_construccion import FormularioSitioConstruccionDesign
from formularios.form_graficas_design import FormularioGraficasDesign
from formularios.principal import DatosPersonales


class FormularioMaestroDesign(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.Simetric_logo = util_img.leer_imagen("./imagenes/Simetric_logo.jpg", (100, 100))
        self.Perfil2 = util_img.leer_imagen("./imagenes/Perfil2.png", (100, 100))
        self.Salud = util_img.leer_imagen("./imagenes/Salud.jpg", (100, 100))
        self.logica()   

    def logica(self):
        def paneles():
            self.barra_superior = ctk.CTkFrame(self, fg_color=COLOR_BARRA_SUPERIOR, height=100)  # Ajusta la altura deseada aquí
            self.barra_superior.pack(side=ctk.TOP, fill='x')
            self.barra_superior.pack_propagate(False)  # Evita que la barra ajuste su tamaño al contenido

            self.menu_lateral = ctk.CTkFrame(self, fg_color=COLOR_MENU_LATERAL, width=20)
            self.menu_lateral.pack(side=ctk.LEFT, fill='both', expand=False)

            self.cuerpo_principal = ctk.CTkFrame(self, fg_color=COLOR_CUERPO_PRINCIPAL)
            self.cuerpo_principal.pack(side=ctk.RIGHT, fill='both', expand=True)

        def controles_barra_superior():
            font_awesome = CTkFont(family="Helvetica", size=12)  # Cambiar a CTkFont

            #Botón
            self.buttonMenuLateral = ctk.CTkButton(self.barra_superior, text="\uf0c9", font=font_awesome,
                command=self.toggle_panel, fg_color=COLOR_BARRA_SUPERIOR, text_color="white", width=50, height=45)
            self.buttonMenuLateral.pack(side=ctk.LEFT, padx=10)

            #Título
            self.labelTitulo = ctk.CTkLabel(self.barra_superior, text="SIMETRIC", text_color="white", font=CTkFont(family="Helvetica", size=25, weight="bold"))
            self.labelTitulo.pack(side=ctk.LEFT, padx=10) 

            #Email
            self.labelEmail = ctk.CTkLabel(self.barra_superior, text="atencionalcliente@simetric.com.co", text_color="white", font=CTkFont(family="Helvetica", size=17, weight="bold"))
            self.labelEmail.pack(side=ctk.RIGHT, padx=20)

        def controles_menu_lateral():
            ancho_menu =225
            alto_menu = 45
            font_awesome = CTkFont(family="Questrial", size=20) 

            self.labelPerfil = ctk.CTkLabel(self.menu_lateral, image=self.Perfil2, text="")
            self.labelPerfil.pack(side=ctk.TOP, pady=10,  anchor="center")


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
            contenedor = ctk.CTkFrame(self.cuerpo_principal, fg_color=COLOR_CUERPO_PRINCIPAL)
            contenedor.pack(side=ctk.TOP, pady=20)
            
            # Label y entrada de nombre centrados
            self.labelNombre = ctk.CTkLabel(contenedor, text="NOMBRE:")
            self.labelNombre.pack(side=ctk.TOP, pady=10, expand=False)

            self.entryNombre = ctk.CTkEntry(contenedor, placeholder_text="Escribe tu nombre", width=202)  # Añadir un width fijo
            self.entryNombre.pack(side=ctk.TOP, pady=10, padx=20)

            # Label y menú de especialidad centrado
            self.labelEspecialidad = ctk.CTkLabel(contenedor, text="ESPECIALIDAD:")
            self.labelEspecialidad.pack(side=ctk.TOP, pady=10)
            
            especialidad = [
                "MEDICINA",
                "OPTO",
                "FONO",
                "PSICO"
            ]
            
            # Menú de opciones de especialidad
            self.especialidad_seleccionada = ctk.StringVar(value="Selecciona una especialidad:")
            especialidad_menu = ctk.CTkOptionMenu(contenedor, variable=self.especialidad_seleccionada, values=especialidad)
            especialidad_menu.pack(pady=10, padx=20, expand=True)
            
            ctk.CTkButton(contenedor, text="Iniciar", command=self.aceptar).pack(pady=10)
        
        paneles()
        controles_barra_superior()
        controles_menu_lateral()
        controles_cuerpo()
        
    
            
    def aceptar(self):
        seleccion = self.especialidad_seleccionada.get()
        nombre = self.entryNombre.get()  # Obtener el valor del campo de nombre

        # Validar que el campo de nombre no esté vacío
        if not nombre:
            self.mensaje.configure(text="El nombre es obligatorio.")
            return

        # Validar que el nombre solo contenga letras (y espacios si lo permites)
        if not re.match("^[A-Za-z\s]+$", nombre):  # Solo letras y espacios
            self.mensaje.configure(text="El nombre solo puede contener letras.")
            return

        # Verifica si se seleccionó una especialidad
        if seleccion == "Selecciona una especialidad:":
            self.mensaje.configure(text="Es obligatorio seleccionar una especialidad.")
            return

        # Si todo es correcto, limpia el mensaje y realiza la acción deseada
        self.limpiar_panel(self.cuerpo_principal)

        # Crear y mostrar el formulario de información
        self.abrir_panel_info()

            

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
            self.menu_lateral.pack(side=ctk.LEFT, fill='y')
    
    def abrir_panel_principal(self):
        self.limpiar_panel(self.cuerpo_principal)
        info_form = DatosPersonales(self.cuerpo_principal, maestro=self)  # Pasar solo el contenedor
        info_form.pack(fill='both', expand=True)

    
    def abrir_panel_info(self):
        self.limpiar_panel(self.cuerpo_principal)
        info_form = FormularioInfoDesign(self.cuerpo_principal, maestro=self)
        info_form.pack(fill='both', expand=True)

    def abrir_panel_en_construccion(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioSitioConstruccionDesign(self.cuerpo_principal, self.Salud)

    def abrir_panel_graficas(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioGraficasDesign(self.cuerpo_principal)

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()

