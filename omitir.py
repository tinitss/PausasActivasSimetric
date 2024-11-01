import tkinter as tk

class omitir(tk.Frame):
    def __init__(self, panel_principal, callback_volver):
        super().__init__(panel_principal)
        self.panel_principal = panel_principal
        self.callback_volver = callback_volver
        self.interfaz()

    def interfaz(self):
        mensaje = tk.StringVar()
        mensaje.set("¿Está segur@ que desea salir de la pausa activa??")

        # Etiqueta para mostrar el mensaje
        label_mensaje = tk.Label(self, textvariable=mensaje, font=("Arial", 16))
        label_mensaje.pack(pady=20)

        # Botón para volver
        btn_volver = tk.Button(self, text="Volver", command=self.callback_volver)
        btn_volver.pack(pady=10)