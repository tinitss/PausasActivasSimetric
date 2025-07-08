import customtkinter as ctk
from customtkinter import CTkFont
from config import *

class FormularioAyuda(ctk.CTkFrame):
    def __init__(self, panel_principal):
        super().__init__(panel_principal)

        # Configurar expansión para centrar el texto
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        label = ctk.CTkLabel(
            self,
            text="FORMULARIO EN PROCESO",
            font=CTkFont(family="Kaboom", size=50, weight="bold"),
            text_color="black", bg_color=COLOR_CUERPO_PRINCIPAL
        )
        label.grid(row=0, column=0, sticky="nsew")
        
    
    
