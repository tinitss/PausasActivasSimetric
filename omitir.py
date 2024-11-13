import tkinter as tk

class omitir(tk.Frame):
    def __init__(self, panel_principal, callback_volver):
        super().__init__(panel_principal)
        self.panel_principal = panel_principal
        self.callback_volver = callback_volver
        self.interfaz()

    def interfaz(self):
        mensaje = tk.StringVar()
        mensaje.set("¿Está segur@ que desea salir de la pausa activa?")

        label_mensaje = tk.Label(self, textvariable=mensaje, font=("Arial", 16))
        label_mensaje.pack(pady=20)

        # Botón No que vuelve al formulario anterior
        btn_no = tk.Button(self, text="No", command=self.volver_a_formulario)
        btn_no.pack(side="right", padx=20, pady=10)

    def volver_a_formulario(self):
        self.panel_principal.limpiar_panel(self)  
        self.crear_interfaz(self)  

