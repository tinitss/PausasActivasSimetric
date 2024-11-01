import tkinter as tk
from tkinter import ttk
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

        # Botón de retorno
        tk.Button(self, text="Volver", command=self.volver).pack(pady=10)

    def inicializar_video(self, video_path):
        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():  
            self.lblInfoVideoPath.config(text="Error: no se pudo cargar el video.")
        else:
            self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.frame_rate = int(self.cap.get(cv2.CAP_PROP_FPS))
            self.total_seconds = self.total_frames / self.frame_rate
            self.update_time_label()
            self.video()

    def crear_elementos_video(self):
        self.lblInfoVideoPath = tk.Label(self)
        self.lblInfoVideoPath.pack()

        self.lblVideo = tk.Label(self)
        self.lblVideo.pack()

        # Controles de video estilo YouTube
        controls_frame = tk.Frame(self)
        controls_frame.pack()

        # Botón de pausa/play
        self.btn_play_pause = tk.Button(controls_frame, text="⏯", command=self.toggle_play_pause)
        self.btn_play_pause.pack(side="left")

        # Barra de progreso
        self.scale_progress = ttk.Scale(controls_frame, orient="horizontal", length=500, from_=0, to=100, command=self.update_frame)
        self.scale_progress.pack(side="left", padx=10)

        # Tiempo transcurrido / Total
        self.time_label = tk.Label(controls_frame, text="00:00 / 00:00")
        self.time_label.pack(side="left")

    def abdomen(self):
        tk.Label(self, text="Pausas saludables - Abdomen y espalda", font=("Trebuchet MS", 20)).pack(pady=5)
        self.crear_elementos_video()
        self.inicializar_video("./videos/Abdomen.mp4")

    # Métodos de cada ejercicio omitiendo por simplicidad...

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

                current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
                self.scale_progress.set(current_frame)
                self.update_time_label()
                self.lblVideo.after(10, self.video)
            else:
                self.lblInfoVideoPath.config(text="Fin del video")
                self.cap.release()

    def toggle_play_pause(self):
        self.is_paused = not self.is_paused
        if not self.is_paused:
            self.video()

    def update_frame(self, event):
        if self.is_paused and self.cap:
            frame_number = int(self.scale_progress.get())
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            ret, frame = self.cap.read()
            if ret:
                frame = imutils.resize(frame, width=640)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                im = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=im)
                self.lblVideo.configure(image=img)
                self.lblVideo.image = img
            self.update_time_label()

    def update_time_label(self):
        if self.cap:
            current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            elapsed_seconds = current_frame / self.frame_rate
            elapsed_time = self.format_time(elapsed_seconds)
            total_time = self.format_time(self.total_seconds)
            self.time_label.config(text=f"{elapsed_time} / {total_time}")

    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02}:{seconds:02}"

    def volver(self):
        if self.callback_volver:
            self.callback_volver()
        self.destroy()
