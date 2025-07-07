import customtkinter as ctk
from Inicio import FormularioInicio

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = FormularioInicio()

app.title("PAUSAS ACTIVAS")  
app.iconbitmap("./imagenes/MinisterioTrabajo.ico")
app.geometry("1024x600")

# Establecer tamaño máximo y mínimo de la ve-ntana
app.maxsize(1024, 600)
app.minsize(1024, 600)

# Función para centrar la ventana
def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()  
    x = int((pantalla_ancho / 2) - (aplicacion_ancho / 2))
    y = int((pantalla_largo / 2) - (aplicacion_largo / 2))
    ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")  

# Centrar la ventana al iniciar
centrar_ventana(app, 1024, 600)

app.mainloop()
