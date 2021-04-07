import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk

from Transferencia_calor import * 
class energy_lenght_BB(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.imagenes_BB()
        # Widgets
        self.labels_BB()
        self.Entradas_BB()
        self.Botones_BB()
    def Entradas_BB(self):
     # labels for entries
        self.EBB = ttk.Entry(self)
        self.EBB.grid(row=3, column=1, columnspan=2)
        self.londa = ttk.Entry(self)
        self.londa.grid(row=4, column=1, columnspan=2) 
        self.T = ttk.Entry(self)
        self.T.grid(row=5,column=1,columnspan=2)  
    def labels_BB(self):
         # Title
        ttk.Label(self, text='Energia por longitud de onda de BB').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.eb).grid(row=1, column=0, columnspan=3)
        #Variables
        ttk.Label(self, text='Energia').grid(row=3, column=0)
        ttk.Label(self, text='Longitud de onda [micrometros]').grid(row=4, column=0) 
        ttk.Label(self, text='Temperatura [K]').grid(row=5, column=0)   
    def Botones_BB(self):
        save = ttk.Button(self, text='Guardar',command=self.obtener_entradas_BB)
        show = ttk.Button(self, text='Calcular', command=self.mostrar_BB)
        quit1 = ttk.Button(self, text="Salir", command=self.master.destroy)
        save.grid(row=10, column=1)
        show.grid(row=10, column=2)
        quit1.grid(row=10, column=3)  
    def imagenes_BB(self):
        # image 1
        self.eb = Image.open("images\\eb.JPG")
        self.eb = self.eb.resize((250, 150))
        self.eb = ImageTk.PhotoImage(self.eb)  

    def obtener_entradas_BB(self):
        self.dictBB_entries = {'EBB': self.EBB.get(),'londa': self.londa.get(), 'T': self.T.get()}
        for item, value in self.dictBB_entries.items():
            if value == 'None':
                self.dictBB_entries[item] = None
            elif type(value) is str:
                self.dictBB_entries[item] = float(value)
        self.BB_ecu(**self.dictBB_entries)

    def BB_ecu(self,EBB, londa, T):
        self.Energy_BB = longitud_energia_onda(EBB=EBB,londa=londa, T=T)

    def mostrar_BB(self):
        ttk.Label(self, text=f'{self.Energy_BB.solucion()}').grid(row=11, column=1)

class densidade_onda(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.imagenes_donda()
        # Widgets
        self.labels_donda()
        self.Entradas_donda()
        self.Botones_donda()
    def Entradas_donda(self):
     # labels for entries
        self.densidad = ttk.Entry(self)
        self.densidad.grid(row=3, column=1, columnspan=2)
        self.fr = ttk.Entry(self)
        self.fr.grid(row=4, column=1, columnspan=2)    
        self.T = ttk.Entry(self)
        self.T.grid(row=5,column=1,columnspan=2)    
    def labels_donda(self):
         # Title
        ttk.Label(self, text='Densidad de energia de la onda').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.deo).grid(row=1, column=0, columnspan=3)
        #Variables
        ttk.Label(self, text='Densidad [(W·m-2)·m-1]').grid(row=3, column=0)
        ttk.Label(self, text='Longitud de onda [m]').grid(row=4, column=0) 
        ttk.Label(self, text='Temperatura [K]').grid(row=5, column=0)   
    def Botones_donda(self):
        save = ttk.Button(self, text='Guardar',command=self.obtener_entradas_deo)
        show = ttk.Button(self, text='Calcular', command=self.mostrar_deo)
        quit1 = ttk.Button(self, text="Salir", command=self.master.destroy)
        save.grid(row=10, column=1)
        show.grid(row=10, column=2)
        quit1.grid(row=10, column=3)  
    def imagenes_donda(self):
        # image 1
        self.deo = Image.open("images\\deo.JPG")
        self.deo = self.deo.resize((250, 150))
        self.deo = ImageTk.PhotoImage(self.deo)  

    def obtener_entradas_deo(self):
        self.dictdeo_entries = {'densidad': self.densidad.get(), 'fr': self.fr.get(), 'T': self.T.get()}
        for item, value in self.dictdeo_entries.items():
            if value == 'None':
                self.dictdeo_entries[item] = None
            elif type(value) is str:
                self.dictdeo_entries[item] = float(value)
        self.deo_ecu(**self.dictdeo_entries)

    def deo_ecu(self, densidad, fr, T):
        self.Energy_mam = densidad_energia_onda(densidad=densidad, fr=fr, T=T)

    def mostrar_deo(self):
        ttk.Label(self, text=f'{self.Energy_mam.solucion()}').grid(row=11, column=1)

class mam_particulas(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.imagenes_mam()
        # Widgets
        self.labels_mam()
        self.Entradas_mam()
        self.Botones_mam()
    def Entradas_mam(self):
     # labels for entries
        self.m = ttk.Entry(self)
        self.m.grid(row=3, column=1, columnspan=2)
        self.fr = ttk.Entry(self)
        self.fr.grid(row=4, column=1, columnspan=2) 
    def labels_mam(self):
         # Title
        ttk.Label(self, text='Masa y momento de las particulas').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.mam).grid(row=1, column=0, columnspan=3)
        #Variables
        ttk.Label(self, text='Masa [kg]').grid(row=3, column=0)
        ttk.Label(self, text='Frecuencia [v] [1/s]').grid(row=4, column=0)

    def Botones_mam(self):
        save = ttk.Button(self, text='Guardar',command=self.obtener_entradas_mam)
        show = ttk.Button(self, text='Calcular', command=self.mostrar_mam)
        quit1 = ttk.Button(self, text="Salir", command=self.master.destroy)
        save.grid(row=10, column=1)
        show.grid(row=10, column=2)
        quit1.grid(row=10, column=3)
    def imagenes_mam(self):
        # image 1
        self.mam = Image.open("images\\mam.JPG")
        self.mam = self.mam.resize((250, 150))
        self.mam = ImageTk.PhotoImage(self.mam)

    def obtener_entradas_mam(self):
        self.dictm_entries = {'m': self.m.get(), 'fr': self.fr.get()}
        for item, value in self.dictm_entries.items():
            if value == 'None':
                self.dictm_entries[item] = None
            elif type(value) is str:
                self.dictm_entries[item] = float(value)
        self.mam_ecu(**self.dictm_entries)

    def mam_ecu(self, m, fr):
        self.Energy_mam = masam_particulas(m=m, fr=fr)

    def mostrar_mam(self):
        ttk.Label(self, text=f'{self.Energy_mam.solucion()}').grid(row=11, column=1)

class energia_cuantos(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.imagenes_cuantos()
        # Widgets
        self.labels_cuantos()
        self.Entradas_cuantos()
        self.Botones_cuantos()
    def Entradas_cuantos(self):
     # labels for entries
        self.E = ttk.Entry(self)
        self.E.grid(row=3, column=1, columnspan=2)
        self.fr = ttk.Entry(self)
        self.fr.grid(row=4, column=1, columnspan=2) 
    def labels_cuantos(self):
         # Title
        ttk.Label(self, text='Energia de los cuantos discretos').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.ecd).grid(row=1, column=0, columnspan=3)
        #Variables
        ttk.Label(self, text='Energia [J]').grid(row=3, column=0)
        ttk.Label(self, text='Frecuencia [v] [1/s]').grid(row=4, column=0)
    def Botones_cuantos(self):
        save = ttk.Button(self, text='Guardar',command=self.obtener_entradas_cenergy)
        show = ttk.Button(self, text='Calcular', command=self.mostrar_cenergy)
        quit1 = ttk.Button(self, text="Salir", command=self.master.destroy)
        save.grid(row=10, column=1)
        show.grid(row=10, column=2)
        quit1.grid(row=10, column=3)
    def imagenes_cuantos(self):
        # image 1
        self.ecd = Image.open("images\\ecd.JPG")
        self.ecd = self.ecd.resize((250, 150))
        self.ecd = ImageTk.PhotoImage(self.ecd)

    def obtener_entradas_cenergy(self):
        self.dictc_entries = {'E': self.E.get(), 'fr': self.fr.get()}
        for item, value in self.dictc_entries.items():
            if value == 'None':
                self.dictc_entries[item] = None
            elif type(value) is str:
                self.dictc_entries[item] = float(value)
        self.cuantos_energy(**self.dictc_entries)

    def cuantos_energy(self, E, fr):
        self.Energy_c = Energia_cuantos_discretos(E=E, fr=fr)

    def mostrar_cenergy(self):
        ttk.Label(self, text=f'{self.Energy_c.solucion()}').grid(row=11, column=1)

class light_speed(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.imagenes_luz()
        # Widgets
        self.labels()
        self.Entradas_luz()
        self.Botones_luz()

    def Entradas_luz(self):
        # labels for entries
        self.lamb = ttk.Entry(self)
        self.lamb.grid(row=3, column=1, columnspan=2)

        self.v = ttk.Entry(self)
        self.v.grid(row=4, column=1, columnspan=2)
    
    def labels(self):
        # Title
        ttk.Label(self, text='Velocidad de la luz').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.luz).grid(row=1, column=0, columnspan=3)
        #Variables
        ttk.Label(self, text='Longitud de onda [lambda] [cm]').grid(row=3, column=0)
        ttk.Label(self, text='Frecuencia [v] [1/s]').grid(row=4, column=0)

    def Botones_luz(self):
        save = ttk.Button(self, text='Guardar',command=self.obtener_entradas_luz)
        show = ttk.Button(self, text='Calcular', command=self.mostrar_luz)
        quit1 = ttk.Button(self, text="Salir", command=self.master.destroy)
        save.grid(row=10, column=1)
        show.grid(row=10, column=2)
        quit1.grid(row=10, column=3)

    def imagenes_luz(self):
        # image 1
        self.luz = Image.open("images\\luz.JPG")
        self.luz = self.luz.resize((250, 200))
        self.luz = ImageTk.PhotoImage(self.luz)

    def obtener_entradas_luz(self):
        self.dict2_entries = {'lamb': self.lamb.get(), 'v': self.v.get()}
        for item, value in self.dict2_entries.items():
            if value == 'None':
                self.dict2_entries[item] = None
            elif type(value) is str:
                self.dict2_entries[item] = float(value)
        self.vel_light(**self.dict2_entries)

    def vel_light(self, lamb, v):
        self.Radia_light = Radiacion_formula_luz(lamb=lamb, v=v)

    def mostrar_luz(self):
        ttk.Label(self, text=f'{self.Radia_light.solucion()}').grid(row=11, column=1)
 

class cuerpo_negro(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.imagenes()
        # Widgets
        self.labels_imagenes()
        self.Entradas()
        self.Botones()
    def labels_imagenes(self):
        # Title
        ttk.Label(self, text='Radiacion').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.radia4).grid(row=1, column=0, columnspan=2)
        ttk.Label(self, image=self.radia5).grid(row=1, column=2, columnspan=2)
        #Variables
        ttk.Label(self, text='Reflectividad [p]').grid(row=3, column=0)
        ttk.Label(self, text='Absorbencia [o]').grid(row=4, column=0)
        ttk.Label(self, text='Transmisividad [t]').grid(row=5, column=0)

    def Entradas(self):
        # labels for entries
        self.p = ttk.Entry(self)
        self.p.grid(row=3, column=1, columnspan=2)

        self.o = ttk.Entry(self)
        self.o.grid(row=4, column=1, columnspan=2)

        self.t = ttk.Entry(self)
        self.t.grid(row=5, column=1, columnspan=2)

    def Botones(self):
        save = ttk.Button(self, text='Guardar',command=self.obtener_entradas)
        show = ttk.Button(self, text='Calcular', command=self.mostrar)
        quit3 = ttk.Button(self, text="Salir", command=self.master.destroy)
        save.grid(row=10, column=1)
        show.grid(row=10, column=2)
        quit3.grid(row=10, column=3)

    def imagenes(self):
        # image 1
        self.radia4 = Image.open("images\\radia4.JPG")
        self.radia4 = self.radia4.resize((250, 200))
        self.radia4 = ImageTk.PhotoImage(self.radia4)
        # Image 2
        self.radia5 = Image.open("images\\radia5.JPG")
        self.radia5 = self.radia5.resize((150, 200))
        self.radia5 = ImageTk.PhotoImage(self.radia5)

    def obtener_entradas(self):
        self.dict1_entries = {'p': self.p.get(), 'o': self.o.get(), 't': self.t.get()}
        for item, value in self.dict1_entries.items():
            if value == 'None':
                self.dict1_entries[item] = None
            elif type(value) is str:
                self.dict1_entries[item] = float(value)
        self.radiacion_termica(**self.dict1_entries)

    def radiacion_termica(self, p, o, t):
        self.Radia_2 = Radiacion_formula_2(p=p, o=o, t=t)

    def mostrar(self):
        ttk.Label(self, text=f'{self.Radia_2.solucion()}').grid(row=11, column=1)

class window_radiacion(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.images()
        # Widgets
        self.labels_pictures()
        self.Entries()
        self.Buttons()


    def labels_pictures(self):
        # create the button and set the command
        # Title
        ttk.Label(self, text='Radiacion').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.radia1).grid(row=1, column=0, columnspan=2)
        ttk.Label(self, image=self.radia3).grid(row=1, column=2, columnspan=2)
        # Variables
        ttk.Label(self, text='q [W]').grid(row=3, column=0)
        ttk.Label(self, text='E').grid(row=4, column=0)
        ttk.Label(self, text='A [m2]').grid(row=5, column=0)
        ttk.Label(self, text='T1 [K]').grid(row=6, column=0)
        ttk.Label(self, text='T2 [K]').grid(row=7, column=0)
        # button to q
        ttk.Button(self, text="Quit", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.q = ttk.Entry(self)
        self.q.grid(row=3, column=1, columnspan=2)

        self.E = ttk.Entry(self)
        self.E.grid(row=4, column=1, columnspan=2)

        self.A = ttk.Entry(self)
        self.A.grid(row=5, column=1, columnspan=2)

        self.T1 = ttk.Entry(self)
        self.T1.grid(row=6, column=1, columnspan=2)

        self.T2 = ttk.Entry(self)
        self.T2.grid(row=7, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'q': self.q.get(), 'E': self.E.get(), 'A': self.A.get(), 'T1': self.T1.get(), 'T2': self.T2.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        tbl = ttk.Button(self, text='Tablas', command=self.managed_windows1)
        save.grid(row=10, column=1)
        show.grid(row=10, column=2)
        tbl.grid(row=10, column=3)


    def images(self):
        # image 1
        self.radia1 = Image.open("images\\radia2.JPG")
        self.radia1 = self.radia1.resize((250, 200))
        self.radia1 = ImageTk.PhotoImage(self.radia1)
        # Image 2
        self.radia3 = Image.open("images\\radia3.JPG")
        self.radia3 = self.radia3.resize((150, 200))
        self.radia3 = ImageTk.PhotoImage(self.radia3)

    def equation(self, q, E, A, T1, T2):
        self.Radia_1 = Radiacion(q=q, A=A, T1=T1, T2=T2, E=E)

    def show(self):
        ttk.Label(self, text=f'{self.Radia_1.solucion()}').grid(row=11, column=1)
    
    def managed_windows1(self):
        self.newWindow1 = tk.Toplevel(self.master)
        self.newWindow1.title('Table')
        self.newWindow1.geometry('500x500')
        self.app = tables(self.newWindow1)

class tables(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.images()
        # Labels
        self.labels_pictures_tables()
    def labels_pictures_tables(self):
        # create the button and set the command
        # Title
        ttk.Label(self, text='Tables').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.radia2).grid(row=1, column=0)
        # button to q
        ttk.Button(self, text="Quit", command=self.master.destroy).grid(row=11,column=0)
    def images(self):
    # Table 1
        self.radia2 = Image.open("images\\radia1.png")
        self.radia2 = self.radia2.resize((400, 400))
        self.radia2 = ImageTk.PhotoImage(self.radia2)
