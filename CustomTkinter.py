import customtkinter as ctk
from customtkinter import CTkFont  # Importa CTkFont en lugar de tkinter.font.Font
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_MENU_LATERAL
import util.util_imagenes as util_img
from formularios.form_info_design import FormularioInfoDesign
from formularios.form_sitio_construccion import FormularioSitioConstruccionDesign
from formularios.form_graficas_design import FormularioGraficasDesign

class FormularioMaestroDesign(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.Simetric_logo = util_img.leer_imagen("./imagenes/Simetric_logo.jpg", (100, 100))
        self.Perfil = util_img.leer_imagen("./imagenes/Perfil.png", (100, 100))
        self.Salud = util_img.leer_imagen("./imagenes/Salud.jpg", (100, 100))
        self.logica()

    def logica(self):
        def paneles():
            self.barra_superior = ctk.CTkFrame(self, fg_color=COLOR_BARRA_SUPERIOR, height=30)
            self.barra_superior.pack(side=ctk.TOP, fill='both')

            self.menu_lateral = ctk.CTkFrame(self, fg_color=COLOR_MENU_LATERAL, width=50)
            self.menu_lateral.pack(side=ctk.LEFT, fill='both', expand=True) 

            self.cuerpo_principal = ctk.CTkFrame(self, fg_color=COLOR_CUERPO_PRINCIPAL)
            self.cuerpo_principal.pack(side=ctk.RIGHT, fill='both', expand=True)

        def controles_barra_superior():
            font_awesome = CTkFont(family="FontAwesome", size=12)  # Cambiar a CTkFont

            self.labelTitulo = ctk.CTkLabel(self.barra_superior, text="SIMETRIC", text_color="white")
            self.labelTitulo.configure(font=CTkFont(family="Roboto", size=15), height=50)  # Cambiar a CTkFont
            self.labelTitulo.pack(side=ctk.LEFT)

            self.buttonMenuLateral = ctk.CTkButton(self.barra_superior, text="\uf0c9", font=font_awesome,
                                                   command=self.toggle_panel, fg_color=COLOR_BARRA_SUPERIOR, text_color="white")
            self.buttonMenuLateral.pack(side=ctk.LEFT)

            self.labelEmail = ctk.CTkLabel(self.barra_superior, text="atencionalcliente@simetric.com.co", text_color="white")
            self.labelEmail.configure(font=CTkFont(family="Roboto", size=10), padx=32, width=25)  # Cambiar a CTkFont
            self.labelEmail.pack(side=ctk.RIGHT)

        def controles_menu_lateral():
            ancho_menu =150
            alto_menu = 50
            font_awesome = CTkFont(family="Questrial", size=20) 

            self.labelPerfil = ctk.CTkLabel(self.menu_lateral, image=self.Perfil)
            self.labelPerfil.pack(side=ctk.TOP, pady=10)

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
            label = ctk.CTkLabel(self.cuerpo_principal, image=self.Simetric_logo)
            label.place(x=0, y=0, relwidth=1, relheight=1)

        paneles()
        controles_barra_superior()
        controles_menu_lateral()
        controles_cuerpo()

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.configure(text=f" {icon}  {text}", anchor="w", font=font_awesome,
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

