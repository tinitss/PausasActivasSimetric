import tkinter as tk
from config import COLOR_CUERPO_PRINCIPAL

class FormularioSitioConstruccionDesign():

    def __init__(self, panel_principal, Simetric_logo):
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)


        self.labelTitulo = tk.Label(
            self.barra_superior, text="Página en construcción")
        self.labelTitulo.config( font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)
        
        self.labelImagen = tk.Label(self.barra_inferior, image=Simetric_logo)   
        self.labelImagen.place(x=0, y=0, relwidth=1, relheight=1)
        self.labelImagen.config(fg="#fff", font=("Roboto", 10), bg=COLOR_CUERPO_PRINCIPAL)
        