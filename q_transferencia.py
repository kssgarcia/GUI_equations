import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk

from Transferencia_calor import * 



class q_coefic(ttk.Frame):
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
        ttk.Label(self, text='q con coeficiente').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.h_1).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='q[W]').grid(row=2, column=0)
        ttk.Label(self, text='h[w/m^2*°C]').grid(row=3, column=0)
        ttk.Label(self, text='d[m]').grid(row=4, column=0)
        ttk.Label(self, text='L[m]').grid(row=5, column=0)
        ttk.Label(self, text='Tw[°C]').grid(row=6, column=0)
        ttk.Label(self, text='Tb1[°C]').grid(row=7, column=0)
        ttk.Label(self, text='Tb2[°C]').grid(row=8, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=9,column=0)


    def Entries(self):
        # labels for entries
        self.q = ttk.Entry(self)
        self.q.grid(row=2, column=1, columnspan=2)

        self.h = ttk.Entry(self)
        self.h.grid(row=3, column=1, columnspan=2)

        self.d = ttk.Entry(self)
        self.d.grid(row=4, column=1, columnspan=2)

        self.L = ttk.Entry(self)
        self.L.grid(row=5, column=1, columnspan=2)

        self.Tw = ttk.Entry(self)
        self.Tw.grid(row=6, column=1, columnspan=2)

        self.Tb1 = ttk.Entry(self)
        self.Tb1.grid(row=7, column=1, columnspan=2)

        self.Tb2 = ttk.Entry(self)
        self.Tb2.grid(row=8, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'q': self.q.get(), 'h': self.h.get(), 'd': self.d.get(), 'L': self.L.get(), 'Tw': self.Tw.get(), 'Tb1': self.Tb1.get(), 'Tb2': self.Tb2.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=11, column=4)
        show.grid(row=11, column=5)


    def images(self):
        # image 1
        self.h_1 = Image.open("images\\Q_1.PNG")
        self.h_1 = self.h_1.resize((300, 70))
        self.h_1 = ImageTk.PhotoImage(self.h_1)


    def equation(self, q, d, h, Tw, Tb1, Tb2, L):
        self.coef = coeficien_q( q=q, d=d, h=h, Tw=Tw, Tb1=Tb1, Tb2=Tb2, L=L)

    def show(self):
        ttk.Label(self, text=f'{self.coef.solucion_total()}').grid(row=9, column=4)

class q_masic(ttk.Frame):
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
        ttk.Label(self, text='q con flujo masico').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.h_1).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='q[W]').grid(row=2, column=0)
        ttk.Label(self, text='m[kg/s]').grid(row=3, column=0)
        ttk.Label(self, text='Cp[kJ/kg*°C]').grid(row=4, column=0)
        ttk.Label(self, text='Tb1[°C]').grid(row=5, column=0)
        ttk.Label(self, text='Tb2[°C]').grid(row=6, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=9,column=0)


    def Entries(self):
        # labels for entries
        self.q = ttk.Entry(self)
        self.q.grid(row=2, column=1, columnspan=2)

        self.m = ttk.Entry(self)
        self.m.grid(row=3, column=1, columnspan=2)

        self.Cp = ttk.Entry(self)
        self.Cp.grid(row=4, column=1, columnspan=2)

        self.Tb1 = ttk.Entry(self)
        self.Tb1.grid(row=5, column=1, columnspan=2)

        self.Tb2 = ttk.Entry(self)
        self.Tb2.grid(row=6, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'q': self.q.get(), 'm': self.m.get(), 'Cp': self.Cp.get(), 'Tb1': self.Tb1.get(), 'Tb2': self.Tb2.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=11, column=4)
        show.grid(row=11, column=5)


    def images(self):
        # image 1
        self.h_1 = Image.open("images\\Q_2.PNG")
        self.h_1 = self.h_1.resize((250, 70))
        self.h_1 = ImageTk.PhotoImage(self.h_1)


    def equation(self, q, m, Cp, Tb1, Tb2):
        self.Nusselt_1 = q_masi(q=q, m=m, Cp=Cp, Tb1=Tb1, Tb2=Tb2)

    def show(self):
        ttk.Label(self, text=f'{self.Nusselt_1.solucion_total()}').grid(row=9, column=4)

