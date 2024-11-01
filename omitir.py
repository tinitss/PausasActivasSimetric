import tkinter as tk

class omitir(tk.Frame):
    def __init__(self, panel_principal, callback_volver):
        super().__init__(panel_principal)
        self.panel_principal = panel_principal
        self.callback_volver = callback_volver
        self.interfaz()
 

 ####REVISAR OMITIR
    def interfaz(self):
        mensaje = tk.StringVar()
        mensaje.set("¿Está segur@ que desea salir de la pausa activa??")

        label_mensaje = tk.Label(self, textvariable=mensaje, font=("Arial", 16))
        label_mensaje.pack(pady=20)

        btn_si = tk.Button(self, text="Sí", command=self.cerrar_ventana)
        btn_si.pack(side="left", padx=20, pady=10)

        btn_no = tk.Button(self, text="No", command=self.callback_volver)
        btn_no.pack(side="right", padx=20, pady=10)

    def cerrar_programa(self):
        self.panel_principal.quit()  # Cierra todo el programa