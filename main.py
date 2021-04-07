import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk

from Transferencia_calor import * 
from Nuss import *
from Reynold import *
from Radiation import *
from Convec_tub_ext import *
from Matriz_orientacion import *

class GUI(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # create the button and set the command
        self.radiacion = ttk.Button(self, text="Radiacion", command=self.window_radia)
        self.reynolds = ttk.Button(self, text="Reynolds", command=self.window_reynolds)
        self.nusselt = ttk.Button(self, text="Nusselt", command=self.window_nusselt)
        self.ext_tub = ttk.Button(self, text="Tubo_ext", command=self.window_ext_tub)
        self.matriz_ = ttk.Button(self, text="Tabla-orientacion", command=self.Matriz)
        self.quit = ttk.Button(self, text="Salir", command=self.master.destroy)
        # Grid the buttons
        self.Grid_set()

    def Grid_set(self):
        self.radiacion.grid(row=0, column=0)
        self.reynolds.grid(row=1, column=0)
        self.nusselt.grid(row=2, column=0)
        self.ext_tub.grid(row=3, column=0)
        self.matriz_.grid(row=4, column=0)
        self.quit.grid(row=5, column=0)

    
    def window_radia(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('250x250')
        self.app = window_Radia(self.newWindow)

    def window_reynolds(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Reynolds')
        self.newWindow.geometry('500x500')
        self.app = Reynolds_class(self.newWindow)
    def window_nusselt(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt')
        self.newWindow.geometry('400x550')
        self.app = window_Nusselt(self.newWindow)
    def window_ext_tub(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('C.Empirica tub ext')
        self.newWindow.geometry('300x300')
        self.app = conve_ext_tub(self.newWindow)
    def Matriz(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('C.Empirica tub ext')
        self.newWindow.geometry('800x800')
        self.app = Tablas_transfe(self.newWindow)

class window_Radia(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # create the buttons and set the command
        self.forradiacion = ttk.Button(self, text="Formula-Radicion", command=self.managed_windows)
        self.radbblack = ttk.Button(self, text="Radiacion de cuerpo negro", command=self.body_black_radiation)
        self.velocidad_luz = ttk.Button(self,text="Velocidad de la luz",command=self.velocidad_luz_radiation)
        self.energia_cuantos= ttk.Button(self, text="Energia de los cuantos",command=self.energia_cuantos_radiation)
        self.mam = ttk.Button(self, text="Masa y momento de las particulas",command = self.mam_radiation)
        self.deno = ttk.Button(self, text="Densidad de energia de la onda",command = self.deno_radiation)
        self.lBB = ttk.Button(self, text="Energia por longitud de onda B.B",command = self.BB_radiation)
        self.quit = ttk.Button(self, text="Quit", command=self.master.destroy)
        # Grid the buttons
        self.forradiacion.grid(row=0, column=0)
        self.radbblack.grid(row=1, column=0)
        self.velocidad_luz.grid(row=2, column=0)
        self.energia_cuantos.grid(row=3, column=0)
        self.mam.grid(row=4,column=0)
        self.deno.grid(row=5, column=0)
        self.lBB.grid(row=6,column=0)
        self.quit.grid(row=7, column=0)
    def managed_windows(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Radiacion')
        self.newWindow.geometry('600x500')
        self.app = window_radiacion(self.newWindow)
    def body_black_radiation(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Cuerpo-negro')
        self.newWindow.geometry('600x500')
        self.app = cuerpo_negro(self.newWindow)
    def velocidad_luz_radiation(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Velocidad de la luz')
        self.newWindow.geometry('600x500')
        self.app = light_speed(self.newWindow)
    def energia_cuantos_radiation(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Energia de los cuantos discretos')
        self.newWindow.geometry('600x500')
        self.app = energia_cuantos(self.newWindow)
    def mam_radiation(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Masa y momento de las particulas')
        self.newWindow.geometry('600x500')
        self.app = mam_particulas(self.newWindow)
    def deno_radiation(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Densidad de energia de la onda')
        self.newWindow.geometry('600x500')
        self.app = densidade_onda(self.newWindow)
    def BB_radiation(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Energia por longitud de onda B.B')
        self.newWindow.geometry('600x500')
        self.app = energy_lenght_BB(self.newWindow)
class window_Nusselt(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.images()
        ttk.Label(self, image=self.nuss_3img).grid(row=0, column=1)
        # create the buttons and set the command
        self.var_1 = ttk.Button(self, text="Nusselt-1", command=self.nuss_1)
        self.var_2 = ttk.Button(self, text="Nusselt-2", command=self.nuss_2)
        self.var_3 = ttk.Button(self, text="Nusselt-3", command=self.nuss_3)
        self.var_4 = ttk.Button(self, text="Nusselt-4", command=self.nuss_4)
        self.var_5 = ttk.Button(self, text="Nusselt-5", command=self.nuss_5)
        self.var_6 = ttk.Button(self, text="Nusselt-6", command=self.nuss_6)
        self.var_7 = ttk.Button(self, text="Tablas", command=self.Tablas_emp)
        self.quit = ttk.Button(self, text="Salir", command=self.master.destroy)
        # Grid the buttons
        self.var_1.grid(row=1, column=1)
        self.var_2.grid(row=2, column=1)
        self.var_3.grid(row=3, column=1)
        self.var_4.grid(row=4, column=1)
        self.var_5.grid(row=5, column=1)
        self.var_6.grid(row=6, column=1)
        self.var_7.grid(row=7, column=1)
        self.quit.grid(row=8, column=1)
    def images(self):
        self.nuss_3img = Image.open("images\\nuss_3.PNG")
        self.nuss_3img = self.nuss_3img.resize((300, 300))
        self.nuss_3img = ImageTk.PhotoImage(self.nuss_3img)


    def nuss_1(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-1')
        self.newWindow.geometry('600x300')
        self.app = Nusselt_1(self.newWindow)
    def nuss_2(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-2')
        self.newWindow.geometry('700x450')
        self.app = Nusselt_2(self.newWindow)
    def nuss_3(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-3')
        self.newWindow.geometry('700x450')
        self.app = Nusselt_3(self.newWindow)
    def nuss_4(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-4')
        self.newWindow.geometry('700x550')
        self.app = Nusselt_4(self.newWindow)
    def nuss_5(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-5')
        self.newWindow.geometry('700x450')
        self.app = Nusselt_5(self.newWindow)
    def nuss_6(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-6')
        self.newWindow.geometry('800x500')
        self.app = Nusselt_6(self.newWindow)
    def Tablas_emp(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Tablas empirico')
        self.newWindow.geometry('1000x800')
        self.app = Tablas(self.newWindow)


class conve_ext_tub(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # create the buttons and set the command
        self.var_1 = ttk.Button(self, text="Fuerza de arrastre", command=self.fuerza_arr)
        self.quit = ttk.Button(self, text="Salir", command=self.master.destroy)
        # Grid the buttons
        self.var_1.grid(row=1, column=1)
        self.quit.grid(row=7, column=1)

    def fuerza_arr(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Fuerza de arrastre')
        self.newWindow.geometry('600x600')
        self.app = fuerza_arrastre(self.newWindow)


master = ThemedTk(themebg=True)
#ubuntu
master.set_theme('breeze')
master.geometry('200x200')
app = GUI(master=master)
app.mainloop()