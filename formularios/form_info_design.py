import tkinter as tk
import util.util_ventana as util_ventana
from datetime import datetime

class FormularioInfoDesign(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.config_windows()
        self.contruirWidget()


    def config_windows(self):
        self.title("SIMETRIC | PAUSAS ACTIVAS")
        self.iconbitmap("./imagenes/Simetric_logo.ico")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    def contruirWidget(self):
        self.labelVersion = tk.Label(self, text="Version : 1.0")
        self.labelVersion.config(fg="#000000", font=(
            "Roboto", 15), pady=10, width=20)
        #self.labelAutor.pack()

    def mostrar_popup():
        popup = tk.Toplevel()
        popup.title("PAUSAS ACTIVAS")
        tk.Label(popup, text="PAUSAS ACTIVAS").pack(pady=30)
        popup.geometry("1200x800") 

        tk.Label(popup, text="Hora de inicio:").pack(pady=20)
        hora_inicio = tk.Entry(popup)
        hora_inicio.insert(0, datetime.now().strftime("%H:%M"))  
        hora_inicio.pack(pady=10)

        tk.Label(popup, text="Hora de fin:").pack(pady=20)
        hora_fin = tk.Entry(popup)
        hora_fin.pack(pady=10)

        tk.Label(popup, text="Ejercicios:").pack(pady=20)
        ejercicios = ["1| Mover las muñecas de adentro hacia afuera"]
        for ejercicio in ejercicios:
            tk.Label(popup, text=ejercicio).pack(pady=5)

        # Lista de ejercicios
        ejercicios = ["1| Mover las muñecas de adentro hacia afuera", 
                    "2| Estiramiento de brazos",
                    "3| Flexiones de piernas",
                    "4| Rotaciones de cuello"]
        
        # Variable para almacenar la opción seleccionada
        ejercicio_seleccionado = tk.StringVar()
        ejercicio_seleccionado.set(ejercicios[0])  # Opción predeterminada

        tk.Label(popup, text="Selecciona un ejercicio:").pack(pady=20)

        mensaje = tk.StringVar()
        mensaje.set("Por favor, presiona 'Aceptar' para comenzar.")
        tk.Label(popup, textvariable=mensaje).pack(pady=20)


        def aceptar():
            mensaje.set("BIENVENIDO, ESTÁS POR EMPEZAR")
            popup.destroy() 

            nueva_ventana = tk.Toplevel()
            nueva_ventana.title("INICIANDO")
            nueva_ventana.geometry("1200x800")

            tk.Label(nueva_ventana, text="Has comenzado las pausas activas").pack(pady=20)
            tk.Label(nueva_ventana, text=f"Ejercicio seleccionado: {ejercicio_seleccionado.get()}").pack(pady=20)

            

        # Botón "Volver" para regresar a la ventana anterior
            tk.Button(nueva_ventana, text="Volver", command=lambda: volver(nueva_ventana, popup)).pack(pady=10)

        tk.Button(popup, text="Aceptar", command=aceptar).pack(pady=10)
        tk.Button(popup, text="Cancelar", command=popup.destroy).pack(pady=10)

        def volver(nueva_ventana, popup):
            nueva_ventana.destroy()  # Cierra la ventana "INICIANDO"
            popup.deiconify()  # Muestra la ventana "PAUSAS ACTIVAS"
            def __init__(self) -> None:
                super().__init__()  


    