import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_MENU_LATERAL
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from formularios.form_info_design import FormularioInfoDesign
from formularios.form_sitio_construccion import FormularioSitioConstruccionDesign
from formularios.form_graficas_design import FormularioGraficasDesign

class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()
        self.Simetric_logo = util_img.leer_imagen("./imagenes/Simetric_logo.jpg", (560, 136))
        self.Perfil = util_img.leer_imagen("./imagenes/Perfil.png", (100, 100))
        self.Salud = util_img.leer_imagen("./imagenes/Salud.jpg", (100, 100))
        self.config_window()
        self.logica()  

    def config_window(self):
        self.title("SIMETRIC | PAUSAS ACTIVAS")
        self.iconbitmap("./imagenes/Simetric_logo.ico")
        w, h = 1024, 600

    def logica(self):
        def paneles():
            self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
            self.barra_superior.pack(side=tk.TOP, fill='both')

            self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
            self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

            self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
            self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

        def controles_barra_superior():
            font_awesome = font.Font(family="FontAwesome", size=12)

            self.labelTitulo = tk.Label(self.barra_superior, text="SIMETRIC")
            self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
            self.labelTitulo.pack(side=tk.LEFT)

            self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                                command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
            self.buttonMenuLateral.pack(side=tk.LEFT)

            self.labelEmail = tk.Label(self.barra_superior, text="atencionalcliente@simetric.com.co")
            self.labelEmail.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=28, width=20)
            self.labelEmail.pack(side=tk.RIGHT)

        def controles_menu_lateral():
            ancho_menu = 20
            alto_menu = 2
            font_awesome = font.Font(family="FontAwesome", size=15)

            self.labelPerfil = tk.Label(self.menu_lateral, image=self.Perfil, bg=COLOR_MENU_LATERAL)
            self.labelPerfil.pack(side=tk.TOP, pady=10)

            self.buttonPausas = tk.Button(self.menu_lateral)
            self.buttonConfig = tk.Button(self.menu_lateral)
            self.buttonAyuda = tk.Button(self.menu_lateral)

            buttons_info = [
                ("Pausas", "\uf109", self.buttonPausas, self.abrir_panel_info),
                ("Configuración", "\uf007", self.buttonConfig, self.abrir_panel_en_construccion),
                ("Ayuda", "\uf03e", self.buttonAyuda, self.abrir_panel_graficas)
            ]

            for text, icon, button, comando in buttons_info:
                self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu, comando)

        def controles_cuerpo():
            label = tk.Label(self.cuerpo_principal, image=self.Simetric_logo, bg=COLOR_CUERPO_PRINCIPAL)
            label.place(x=0, y=0, relwidth=1, relheight=1)

        paneles()
        controles_barra_superior()
        controles_menu_lateral()
        controles_cuerpo()

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f" {icon}  {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                      command=comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg="white")

    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg="white")

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

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
    