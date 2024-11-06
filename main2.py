import customtkinter as ctk
from CustomTkinter import FormularioMaestroDesign

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = FormularioMaestroDesign()

app.title("PAUSAS ACTIVAS | SIMETRIC")
app.iconbitmap("./imagenes/Simetric_logo.ico")
app.geometry("1024x600")

# Establecer tamaño máximo y mínimo de la ventana
app.maxsize(1024, 600)
app.minsize(1024, 600)

# Función para centrar la ventana
def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()  # Corregido el nombre
    x = int((pantalla_ancho / 2) - (aplicacion_ancho / 2))
    y = int((pantalla_largo / 2) - (aplicacion_largo / 2))
    ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")  # Corregida la sintaxis de geometry

# Centrar la ventana al iniciar
centrar_ventana(app, 1024, 600)

# Función para manejar el evento de maximización
def no_mover_ventana():
    centrar_ventana(app, 1024, 600)

# Vincular el evento de maximización para restablecer la posición
app.bind("<Configure>", no_mover_ventana)

app.mainloop()
