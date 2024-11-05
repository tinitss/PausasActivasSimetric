import customtkinter as ctk
from CustomTkinter import FormularioMaestroDesign

ctk.set_appearance_mode("system") 
ctk.set_default_color_theme("blue")  

app = FormularioMaestroDesign()

app.title("HOLA MUNDO")
app.iconbitmap("./imagenes/Simetric_logo.ico")
app.geometry("1024x600")

app.mainloop()
