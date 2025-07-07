import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FormularioAyuda():

    def __init__(self, panel_principal):
        figura = Figure(figsize=(8,6), dpi=100)
        ax1 = figura.add_subplot(211)
        ax2 = figura.add_subplot(212)
        
        figura.subplots_adjust(hspace=0.4)
        self.grafico1(ax1)
        self.grafico2(ax2)

        canvas = FigureCanvasTkAgg(figura, master=panel_principal)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")


    def grafico1(self, ax):
       x = [1, 2, 3, 4, 5]
       y = [2, 4, 6, 8, 10]

       ax.bar(x, y, label="Grafico 1", color="blue", alpha=0.7)

       ax.set_title("Gráfico 1 - Gráfico de barras")
       ax.set_xlabel("Eje X")
       ax.set_ylabel("Eje Y")
       ax.legend()

       for i, v in enumerate(y):
        ax.text(x[i] - 0.1, v + 0.1, str(v), color="black")

       ax.grid(axis="y", linestyle="--", alpha=0.7)

    def grafico2(self, ax):
       x = [1, 2, 3, 4, 5]
       y = [1, 2, 1, 2, 1]

       ax.plot(x, y, label="Gráfico 2", color="red")
       ax.set_title("Gráfico 2",)
       ax.set_xlabel("Eje X", fontsize=12)
       ax.set_ylabel("Eje Y", fontsize=12)
       ax.plot(x, y, label="Gráfico 2", color="red", linestyle="--", marker="o")
       ax.annotate("Punto importante", xy=(3, 1), xytext=(3.5, 1.5),
                   arrowprops=dict(facecolor="black", shrink=0.05))
       ax.set_xlim(0, 6)
       ax.set_ylim(0, 3)
       ax.grid(True, linestyle="--", alpha=0.6)
       ax.legend()
                   