import customtkinter as ctk
from config import COLOR_CUERPO_PRINCIPAL

class FormularioConfiguracion(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master, fg_color=COLOR_CUERPO_PRINCIPAL)
        self.app = app  # Referencia a la app principal
        
        self.grid(row=0, column=0, sticky="nsew")
        
        self.titulo = ctk.CTkLabel(self, text="TEMA:")
        self.titulo.grid(row=0, column=0, pady=10)

        self.switch = ctk.CTkSwitch(self, text="Light/Dark", command=self.Cambio_Tema)
        self.switch.grid(row=1, column=0, pady=20)
        
        self.mode = "dark"

    def Cambio_Tema(self):

        if self.mode == "dark":
            ctk.set_appearance_mode("light")
            self.mode = "light"
            
            # Intercambiar colores entre barra superior y cuerpo principal
            color_barra = self.app.barra_superior.cget("fg_color")
            color_cuerpo = self.app.cuerpo_principal.cget("fg_color")
            
            self.app.barra_superior.configure(fg_color=color_cuerpo)
            self.app.cuerpo_principal.configure(fg_color=color_barra)
            
            # Cambiar colores de texto: barra superior -> negro, cuerpo -> blanco
            for widget in self.app.barra_superior.winfo_children():
                if isinstance(widget, (ctk.CTkLabel, ctk.CTkButton)):
                    widget.configure(text_color="black")
            for widget in self.app.cuerpo_principal.winfo_children():
                if isinstance(widget, (ctk.CTkLabel, ctk.CTkButton)):
                    widget.configure(text_color="white")
            
            self.titulo.configure(text_color="black")
            self.switch.configure(text_color="black")
            
        else:
            ctk.set_appearance_mode("dark")
            self.mode = "dark"
            
            color_barra = self.app.barra_superior.cget("fg_color")
            color_cuerpo = self.app.cuerpo_principal.cget("fg_color")
            
            self.app.barra_superior.configure(fg_color=color_cuerpo)
            self.app.cuerpo_principal.configure(fg_color=color_barra)
            
            # Barra superior: texto blanco, cuerpo: texto negro
            for widget in self.app.barra_superior.winfo_children():
                if isinstance(widget, (ctk.CTkLabel, ctk.CTkButton)):
                    widget.configure(text_color="white")
            for widget in self.app.cuerpo_principal.winfo_children():
                if isinstance(widget, (ctk.CTkLabel, ctk.CTkButton)):
                    widget.configure(text_color="black")
            
            self.titulo.configure(text_color="white")
            self.switch.configure(text_color="white")
