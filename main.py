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
from conve_h import *

from q_transferencia import *
from conveccion_analitica import *




class GUI(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # create the button and set the command
        self.radiacion = ttk.Button(self, text="Radiacion", command=self.window_radia)
        self.conva = ttk.Button(self,text='Conveccion analitica',command=self.window_cova)
        self.reynolds = ttk.Button(self, text="Reynolds", command=self.window_reynolds)
        self.nusselt = ttk.Button(self, text="Tub-int", command=self.window_nusselt)
        self.ext_tub = ttk.Button(self, text="Tubo_ext", command=self.window_ext_tub)
        self.matriz_ = ttk.Button(self, text="Tabla-orientacion", command=self.Matriz)
        self.propiedades = ttk.Button(self, text="Propiedades-aire-agua-K", command=self.tabla_pro)
        self.propiedades_c = ttk.Button(self, text="Propiedades-aire-agua-°C", command=self.tabla_pro_c)
        self.h_convec = ttk.Button(self, text="h_conveccion", command=self.h_conve)
        self.q_h = ttk.Button(self, text="q con h", command=self.q_coeficiente)
        self.q_masico = ttk.Button(self, text="q-flujo masico", command=self.q_masic)
        self.quit = ttk.Button(self, text="Salir", command=self.master.destroy)
        # Grid the buttons
        self.Grid_set()

    def Grid_set(self):
        self.radiacion.grid(row=0, column=0)
        self.conva.grid(row=1,column=0)
        self.reynolds.grid(row=2, column=0)
        self.nusselt.grid(row=3, column=0)
        self.ext_tub.grid(row=4, column=0)
        self.matriz_.grid(row=5, column=0)
        self.propiedades.grid(row=6, column=0)
        self.propiedades_c.grid(row=7, column=0)
        self.h_convec.grid(row=8, column=0)
        self.q_h.grid(row=9, column=0)
        self.q_masico.grid(row=10, column=0)
        self.quit.grid(row=11, column=0)
    
    def window_radia(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('300x300')
        self.app = window_Radia(self.newWindow)
    
    def window_cova(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('200x200')
        self.app = window_convecion_anal(self.newWindow)  
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
        self.newWindow.geometry('600x700')
        self.app = conve_ext_tub(self.newWindow)
    def Matriz(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('C.Empirica tub ext')
        self.newWindow.geometry('800x800')
        self.app = Tablas_transfe(self.newWindow)
    def tabla_pro(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Tablas-Propiedades-k')
        self.newWindow.geometry('900x550')
        self.app = propiedades_flujo(self.newWindow)
    def h_conve(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('h-conveccion')
        self.newWindow.geometry('500x500')
        self.app = h_conveccion(self.newWindow)
    def tabla_pro_c(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Tablas_Propiedades-°C')
        self.newWindow.geometry('1300x900')
        self.app = propiedades_flujo_c(self.newWindow)
    def q_coeficiente(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('600x450')
        self.app = q_coefic(self.newWindow)
    def q_masic(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('600x400')
        self.app = q_masic(self.newWindow)
class window_convecion_anal(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # create the buttons and set the command
        self.rflujo = ttk.Button(self, text="Rapidez de masa de flujo", command=self.managed_windows_flujo)
        self.rflujo.grid(row=0, column=0)
    def managed_windows_flujo(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Rapidez de masa de flujo')
        self.newWindow.geometry('600x500')
        self.app = rap_masa_flujo(self.newWindow)
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
        self.eeo = ttk.Button(self, text="Energia entre longitudes de onda",command = self.eeo_radiation)
        self.quit = ttk.Button(self, text="Quit", command=self.master.destroy)
        # Grid the buttons
        self.forradiacion.grid(row=0, column=0)
        self.radbblack.grid(row=1, column=0)
        self.velocidad_luz.grid(row=2, column=0)
        self.energia_cuantos.grid(row=3, column=0)
        self.mam.grid(row=4,column=0)
        self.deno.grid(row=5, column=0)
        self.lBB.grid(row=6,column=0)
        self.eeo.grid(row=7, column=0)
        self.quit.grid(row=8, column=0)
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

    def eeo_radiation(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Energia entre longitudes de onda')
        self.newWindow.geometry('600x500')
        self.app = energia_entre_ondas(self.newWindow)

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
        self.images()
        ttk.Label(self, image=self.ext_1).grid(row=0, column=1)
        # create the buttons and set the command
        self.var_1 = ttk.Button(self, text="Fuerza de arrastre", command=self.fuerza_arr)
        self.var_2 = ttk.Button(self, text="Nusselt-1", command=self.nuss_1_ext)
        self.var_3 = ttk.Button(self, text="Nusselt-2", command=self.nuss_2_ext)
        self.var_4 = ttk.Button(self, text="Nusselt-3", command=self.nuss_3_ext)
        self.var_5 = ttk.Button(self, text="Nusselt-4", command=self.nuss_4_ext)
        self.var_6 = ttk.Button(self, text="Nusselt-5", command=self.nuss_5_ext)
        self.var_7 = ttk.Button(self, text="Nusselt-6", command=self.nuss_6_ext)
        self.var_8 = ttk.Button(self, text="Nusselt-7", command=self.nuss_7_ext)
        self.var_9 = ttk.Button(self, text="Bancos", command=self.nuss_bancos)
        self.quit = ttk.Button(self, text="Salir", command=self.master.destroy)
        # Grid the buttons
        self.var_1.grid(row=1, column=1)
        self.var_2.grid(row=2, column=1)
        self.var_3.grid(row=3, column=1)
        self.var_4.grid(row=4, column=1)
        self.var_5.grid(row=5, column=1)
        self.var_6.grid(row=6, column=1)
        self.var_7.grid(row=7, column=1)
        self.var_8.grid(row=8, column=1)
        self.var_9.grid(row=9, column=1)
        self.quit.grid(row=10, column=1)
    def images(self):
        self.ext_1 = Image.open("images\\ext_tub.PNG")
        self.ext_1 = self.ext_1.resize((400, 400))
        self.ext_1 = ImageTk.PhotoImage(self.ext_1)

    def fuerza_arr(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Fuerza de arrastre')
        self.newWindow.geometry('600x600')
        self.app = fuerza_arrastre(self.newWindow)
    def nuss_1_ext(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-1')
        self.newWindow.geometry('700x500')
        self.app = Nusselt_1_ext(self.newWindow)
    def nuss_2_ext(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-2')
        self.newWindow.geometry('700x350')
        self.app = Nusselt_2_ext(self.newWindow)
    def nuss_3_ext(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-3')
        self.newWindow.geometry('700x450')
        self.app = Nusselt_3_ext(self.newWindow)
    def nuss_4_ext(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-4')
        self.newWindow.geometry('700x550')
        self.app = Nusselt_4_ext(self.newWindow)
    def nuss_5_ext(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-5')
        self.newWindow.geometry('700x450')
        self.app = Nusselt_5_ext(self.newWindow)
    def nuss_6_ext(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-6')
        self.newWindow.geometry('800x500')
        self.app = Nusselt_6_ext(self.newWindow)
    def nuss_7_ext(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-6')
        self.newWindow.geometry('800x500')
        self.app = Nusselt_7_ext(self.newWindow)
    def nuss_bancos(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-6')
        self.newWindow.geometry('800x500')
        self.app = bancos_ext(self.newWindow)
    # def Tablas_emp(self):
    #     self.newWindow = tk.Toplevel(self.master)
    #     self.newWindow.title('Tablas empirico')
    #     self.newWindow.geometry('1000x800')
    #     self.app = Tablas(self.newWindow)

class propiedades_flujo(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.images()
        # Images
        ttk.Label(self, image=self.pro_1).grid(row=1, column=0)
        ttk.Label(self, image=self.pro_2).grid(row=1, column=1)

    def images(self):
        # image 1
        self.pro_1 = Image.open("images\\Pro_aire.PNG")
        self.pro_1 = self.pro_1.resize((450, 450))
        self.pro_1 = ImageTk.PhotoImage(self.pro_1)
        # image 2
        self.pro_2 = Image.open("images\\Pro_agua.PNG")
        self.pro_2 = self.pro_2.resize((450, 450))
        self.pro_2 = ImageTk.PhotoImage(self.pro_2)

class propiedades_flujo_c(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.images()
        # Images
        ttk.Label(self, image=self.proc_1).grid(row=1, column=0)
        ttk.Label(self, image=self.proc_2).grid(row=1, column=1)

    def images(self):
        # image 1
        self.proc_1 = Image.open("images\\tabl_1_cn.PNG")
        self.proc_1 = self.proc_1.resize((600, 700))
        self.proc_1 = ImageTk.PhotoImage(self.proc_1)
        # image 2
        self.proc_2 = Image.open("images\\tabl_2_cn.PNG")
        self.proc_2 = self.proc_2.resize((600, 700))
        self.proc_2 = ImageTk.PhotoImage(self.proc_2)




master = ThemedTk(themebg=True)
#ubuntu
master.set_theme('breeze')
master.geometry('350x400')
app = GUI(master=master)
app.mainloop()