def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()  # Corregido el nombre
    x = int((pantalla_ancho / 2) - (aplicacion_ancho / 2))
    y = int((pantalla_largo / 2) - (aplicacion_largo / 2))
    ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")  # Corregida la sintaxis de geometry
