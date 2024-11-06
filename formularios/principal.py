import customtkinter as ctk
from config import COLOR_CUERPO_PRINCIPAL

class DatosPersonales(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.inicio()

    def inicio(self):
            contenedor = ctk.CTkFrame(self.cuerpo_principal, fg_color=COLOR_CUERPO_PRINCIPAL)
            contenedor.pack(side=ctk.TOP, pady=20)
            
            # Label y entrada de nombre centrados
            self.labelPerfil = ctk.CTkLabel(contenedor, text="NOMBRE:")
            self.labelPerfil.pack(side=ctk.TOP, pady=10, expand=False)

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
