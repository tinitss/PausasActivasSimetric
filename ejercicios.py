import tkinter as tk
from PIL import Image, ImageTk
import cv2
import imutils
class Clase_ejercicios(tk.Frame):
    def __init__(self, panel_principal, callback_volver, tipo_ejercicio, *args, **kwargs):
        super().__init__(panel_principal, *args, **kwargs)
        self.panel_principal = panel_principal
        self.callback_volver = callback_volver
        self.tipo_ejercicio = tipo_ejercicio
        self.cap = None  
        self.is_paused = False  
        self.crear_interfaz()

    def crear_interfaz(self):
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
            self.voz()
        elif self.tipo_ejercicio == "ergonomia":
            self.ergonomia()

        tk.Button(self, text="Volver", command=self.volver).pack(pady=10)

    def inicializar_video(self, video_path):
        self.cap = cv2.VideoCapture(video_path)
        self.video()  # Llama al método para iniciar la reproducción del video

    # Método para crear los elementos de la interfaz relacionados con el video
    def crear_elementos_video(self):
        self.lblInfoVideoPath = tk.Label(self)
        self.lblInfoVideoPath.pack()
        self.lblVideo = tk.Label(self)
        self.lblVideo.pack()
        self.lblVideo.bind("<Button-1>", self.toggle_play_pause)

    # Método para configurar y reproducir el video de abdomen
    def abdomen(self):
        tk.Label(self, text="Pausas saludables - Abdomen y espalda", font=("Trebuchet MS", 20)).pack(pady=5)
        
        # Crear elementos de video y configurarlo
        self.crear_elementos_video()
        self.inicializar_video("./videos/Abdomen.mp4")
        
    # Método para configurar y reproducir el video de cadera
    def cadera(self):
        tk.Label(self, text="Pausas saludables - Caderas", font=("Trebuchet MS", 20)).pack(pady=5)
        
        # Crear elementos de video y configurarlo (puedes asignar otro video si es necesario)
        self.crear_elementos_video()
        self.inicializar_video("./videos/Cadera.mp4") 

    def manos(self):
        tk.Label(self, text="Pausas saludables - Manos y codos", font=("Trebuchet MS", 20)).pack(pady=5)
        
        # Crear elementos de video y configurarlo (puedes asignar otro video si es necesario)
        self.crear_elementos_video()
        self.inicializar_video("./videos/Manos.mp4") 

    def cuello(self):
        tk.Label(self, text="Pausas saludables - Cuellos", font=("Trebuchet MS", 20)).pack(pady=5)
        
        # Crear elementos de video y configurarlo (puedes asignar otro video si es necesario)
        self.crear_elementos_video()
        self.inicializar_video("./videos/Cuello.mp4")

    def ojos(self):
        tk.Label(self, text="Pausa saludable para los ojos", font=("Trebuchet MS", 20)).pack(pady=5)
        
        # Crear elementos de video y configurarlo (puedes asignar otro video si es necesario)
        self.crear_elementos_video()
        self.inicializar_video("./videos/Ojos.mp4") 

    def voz(self):
        tk.Label(self, text="Pausa saludable para la voz", font=("Trebuchet MS", 20)).pack(pady=5)
        
        # Crear elementos de video y configurarlo (puedes asignar otro video si es necesario)
        self.crear_elementos_video()
        self.inicializar_video("./videos/Voz.mp4") 

    def hombros(self):
        tk.Label(self, text="Pausa saludable - Hombros", font=("Trebuchet MS", 20)).pack(pady=5)
        
        # Crear elementos de video y configurarlo (puedes asignar otro video si es necesario)
        self.crear_elementos_video()
        self.inicializar_video("./videos/Hombros.mp4")

    def ergonomia(self):
        tk.Label(self, text="Hábitos seguros - Ergonomía", font=("Trebuchet MS", 20)).pack(pady=5)
        
        # Crear elementos de video y configurarlo (puedes asignar otro video si es necesario)
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

    def toggle_play_pause(self, event):
        if self.is_paused:
            self.is_paused = False
            self.video()
        else:
            self.is_paused = True

    def volver(self):
        if self.callback_volver:
            self.callback_volver()
        self.destroy()