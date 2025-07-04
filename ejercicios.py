import tkinter as tk
import customtkinter as ctk
from customtkinter import *
from PIL import Image, ImageTk
import cv2  
import imutils
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_LATERAL

class Clase_ejercicios(tk.Frame):
    def __init__(self, panel_principal, callback_volver, tipo_ejercicio, maestro, nombre, *args, **kwargs):
        super().__init__(panel_principal, *args, **kwargs)
        self.panel_principal = panel_principal
        self.callback_volver = callback_volver
        self.tipo_ejercicio = tipo_ejercicio
        self.maestro = maestro
        self.nombre = nombre
        self.cap = None  
        self.is_paused = False  
        self.crear_interfaz()


    def crear_interfaz(self):
        font_negrilla = CTkFont(weight="bold", size=17, family="Questrial")
        
        self.contenedor_margen = ctk.CTkFrame(self, fg_color=COLOR_CUERPO_PRINCIPAL)
        self.contenedor_margen.pack(expand=True, fill='both')
        
        self.cuerpo_principal = ctk.CTkFrame(self.contenedor_margen, fg_color=COLOR_CUERPO_PRINCIPAL, width=800, height=600)
        self.cuerpo_principal.pack(padx=80, pady=5)  # Ajusta padx para desplazar hacia la derecha

        if self.tipo_ejercicio == "abdomen":
            self.abdomen()
        elif self.tipo_ejercicio == "cadera":
            self.cadera()
        elif self.tipo_ejercicio == "manos":
            self.manos()
        elif self.tipo_ejercicio == "cuello":
            self.cuello()
        elif self.tipo_ejercicio == "ojos":
            self.ojos()
        elif self.tipo_ejercicio == "voz":
            self.voz()  
        elif self.tipo_ejercicio == "hombros":
            self.hombros()
        elif self.tipo_ejercicio == "ergonomia":
            self.ergonomia()

        self.boton_volver = ctk.CTkButton(self.cuerpo_principal, text="Volver", command=self.volver, font=font_negrilla, 
                                    fg_color=COLOR_BARRA_SUPERIOR, hover_color=COLOR_MENU_LATERAL, 
                                    text_color="white", width=80, height=30)
        self.boton_volver.pack(pady=5)  

    def inicializar_video(self, video_path):
        self.cap = cv2.VideoCapture(video_path)
        self.video()  # Llama al método para iniciar la reproducción del video

    def crear_elementos_video(self):
                # Etiqueta para mostrar la ruta del video
        self.lblInfoVideoPath = tk.Label(self.cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.lblInfoVideoPath.pack()

        # Etiqueta para el video sin margen extra
        self.lblVideo = tk.Label(self.cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.lblVideo.pack(pady=(0, 0))  # Ajusta el padding a (0, 0) para eliminar espacio adicional

        # Hacer que el video se centre y se ajuste con el resto de los elementos
        self.lblVideo.bind("<Button-1>", self.toggle_play_pause)


    def crear_titulo(self, texto):
        titulo = ctk.CTkFont(weight="bold", size=30, family="Kaboom")
        tk.Label(self.cuerpo_principal, text=texto, font=titulo, bg=COLOR_CUERPO_PRINCIPAL).pack(pady=5)

    def abdomen(self):
        self.crear_titulo("Pausas saludables - Abdomen y espalda")
        self.crear_elementos_video()
        self.inicializar_video("./videos/Abdomen.mp4")

    def cadera(self):
        self.crear_titulo("Pausas saludables - Caderas")
        self.crear_elementos_video()
        self.inicializar_video("./videos/Cadera.mp4") 

    def manos(self):
        self.crear_titulo("Pausas saludables - Manos y codos")
        self.crear_elementos_video()
        self.inicializar_video("./videos/Manos.mp4") 

    def cuello(self):
        self.crear_titulo("Pausas saludables - Cuello")
        self.crear_elementos_video()
        self.inicializar_video("./videos/Cuello.mp4")

    def ojos(self):
        self.crear_titulo("Pausa saludable para los ojos")
        self.crear_elementos_video()
        self.inicializar_video("./videos/Ojos.mp4") 

    def voz(self):
        self.crear_titulo("Pausa saludable para la voz")
        self.crear_elementos_video()
        self.inicializar_video("./videos/Voz.mp4") 

    def hombros(self):
        self.crear_titulo("Pausa saludable - Hombros")
        self.crear_elementos_video()
        self.inicializar_video("./videos/Hombros.mp4")

    def ergonomia(self):
        self.crear_titulo("Hábitos seguros - Ergonomía")
        self.crear_elementos_video()
        self.inicializar_video("./videos/Ergonomia.mp4")


    # Método para reproducir el video
    def video(self):
        if self.cap is not None and not self.is_paused:
            ret, frame = self.cap.read()
            if ret:
                frame = imutils.resize(frame, width=640)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                im = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=im)
                self.lblVideo.configure(image=img)
                self.lblVideo.image = img
                self.lblVideo.after(10, self.video)
            else:
                self.lblInfoVideoPath.config(text="Fin del video")
                self.cap.release()

    # Método para pausar y reanudar el video
    def toggle_play_pause(self, event):
        if self.is_paused:
            self.is_paused = False
            self.video()
        else:
            self.is_paused = True

    def volver(self):
        self.maestro.abrir_panel_info(self.nombre)




