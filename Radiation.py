import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk

from Transferencia_calor import * 

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
        ttk.Label(self, image=self.luz).grid(row=1, column=0, columnspan=2)
        #Variables
        ttk.Label(self, text='Longitud de onda [lambda]').grid(row=3, column=0)
        ttk.Label(self, text='Frecuencia [v]').grid(row=4, column=0)

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
        save.grid(row=10, column=1)
        show.grid(row=10, column=2)

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
