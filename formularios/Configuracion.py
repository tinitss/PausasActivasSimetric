import customtkinter as ctk
from customtkinter import CTkFont
from config import *

class FormularioConfiguracion(ctk.CTkFrame):
    def __init__(self, master, app, tema_actual):
        super().__init__(master, fg_color=COLOR_CUERPO_PRINCIPAL)
        self.app = app 
        self.tema_actual = tema_actual
        
        self.grid(row=0, column=0, sticky="nsew")
        
        self.titulo = ctk.CTkLabel(self, text="TEMA:", font=CTkFont(family="Kaboom", size=50, weight="bold"),
                                   text_color="black", bg_color=COLOR_CUERPO_PRINCIPAL)
        self.titulo.grid(row=0, column=0, pady=10)

        self.switch = ctk.CTkSwitch(self, text="Dark/Light", command=self.Cambio_Tema)
        self.switch.grid(row=1, column=0, pady=20)

        # Modo inicial según estado global
        ctk.set_appearance_mode(self.tema_actual)
        if self.tema_actual == "light":
            self.switch.select()  # El switch está encendido en light
        else:
            self.switch.deselect()
        self.actualizar_colores(self.tema_actual)


    def Cambio_Tema(self):
        if self.switch.get():  # True => modo LIGHT
            self.tema_actual = "light"
            ctk.set_appearance_mode("light")
            self.app.tema_actual = "light"  # 👈 actualiza también en app principal
            self.actualizar_colores("light")
        else:
            self.tema_actual = "dark"
            ctk.set_appearance_mode("dark")
            self.app.tema_actual = "dark"
            self.actualizar_colores("dark")
        

    def actualizar_colores(self, modo):
        if modo == "light":
            self.app.barra_superior.configure(fg_color=COLOR_BARRA_SUPERIOR)
            self.app.cuerpo_principal.configure(fg_color=COLOR_CUERPO_PRINCIPAL)

            for widget in self.app.barra_superior.winfo_children():
                if isinstance(widget, (ctk.CTkLabel, ctk.CTkButton)):
                    widget.configure(text_color="white")
            for widget in self.app.cuerpo_principal.winfo_children():
                if isinstance(widget, ctk.CTkFrame):
                    widget.configure(fg_color=COLOR_CUERPO_PRINCIPAL)
                elif isinstance(widget, (ctk.CTkLabel, ctk.CTkButton)):
                    widget.configure(text_color="black")

            self.titulo.configure(text_color="black")
            self.switch.configure(text_color="black")

            # ✅ actualiza color del botón del menú hamburguesa
            self.app.buttonMenuLateral.configure(fg_color=COLOR_BARRA_SUPERIOR, text_color="white")

        else:  # dark
            self.app.barra_superior.configure(fg_color=COLOR_CUERPO_PRINCIPAL)
            self.app.cuerpo_principal.configure(fg_color=COLOR_BARRA_SUPERIOR)

            for widget in self.app.barra_superior.winfo_children():
                if isinstance(widget, ctk.CTkFrame):
                    widget.configure(fg_color=COLOR_CUERPO_PRINCIPAL)
                elif isinstance(widget, (ctk.CTkLabel, ctk.CTkButton)):
                    widget.configure(text_color="black")
            for widget in self.app.cuerpo_principal.winfo_children():
                if isinstance(widget, ctk.CTkFrame):
                    widget.configure(fg_color=COLOR_BARRA_SUPERIOR)
                elif isinstance(widget, (ctk.CTkLabel, ctk.CTkButton)):
                    widget.configure(text_color="white")

            self.titulo.configure(text_color="white")
            self.switch.configure(text_color="white")

            # ✅ actualiza color del botón del menú hamburguesa
            self.app.buttonMenuLateral.configure(fg_color=COLOR_CUERPO_PRINCIPAL, text_color="black")

