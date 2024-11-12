import customtkinter as ctk
from config import COLOR_CUERPO_PRINCIPAL
from tkinter import END  # Import END from tkinter

class FormularioSitioConstruccionDesign(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COLOR_CUERPO_PRINCIPAL)
        
        # Set layout configuration
        self.grid(row=0, column=0, sticky="nsew")

        # Title label
        self.titulo = ctk.CTkLabel(self, text="TEMA:")
        self.titulo.grid(row=0, column=0, pady=10)

        # Light/Dark toggle button
        self.switch = ctk.CTkSwitch(self, text="Light/Dark", command=self.Cambio_Tema)
        self.switch.grid(row=2, column=0, pady=20)

    # Set initial mode as "dark"
    mode = "dark"
    
    # Theme change function
    def Cambio_Tema(self):
        if self.mode == "dark":
            ctk.set_appearance_mode("light")
            self.mode = "light"
            self.titulo.configure(text_color="black")
            self.switch.configure(text_color="black")
            
            # Additional elements, like text in Textbox, can be updated here.
        else:
            ctk.set_appearance_mode("dark")
            self.mode = "dark"
            self.titulo.configure(text_color="black")
            self.switch.configure(text_color="black")
            
            # Update additional elements for dark mode as needed.
