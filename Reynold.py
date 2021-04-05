import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk

from Transferencia_calor import * 

class Reynolds_class(ttk.Frame):
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
        ttk.Label(self, text='Reynolds').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.reynolds_1).grid(row=1, column=0, columnspan=2)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='densi[kg/m^3]').grid(row=4, column=0)
        ttk.Label(self, text='um[m/s]').grid(row=5, column=0)
        ttk.Label(self, text='d[m]').grid(row=6, column=0)
        ttk.Label(self, text='u[kg/m*s]').grid(row=7, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.Re = ttk.Entry(self)
        self.Re.grid(row=3, column=1, columnspan=2)

        self.densi = ttk.Entry(self)
        self.densi.grid(row=4, column=1, columnspan=2)

        self.um = ttk.Entry(self)
        self.um.grid(row=5, column=1, columnspan=2)

        self.d = ttk.Entry(self)
        self.d.grid(row=6, column=1, columnspan=2)

        self.u = ttk.Entry(self)
        self.u.grid(row=7, column=1, columnspan=2)
    

    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'densi': self.densi.get(), 'um': self.um.get(), 'd': self.d.get(), 'u': self.u.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=10, column=4)
        show.grid(row=10, column=5)


    def images(self):
        # image 1
        self.reynolds_1 = Image.open("images\\Reynolds_1.PNG")
        self.reynolds_1 = self.reynolds_1.resize((200, 200))
        self.reynolds_1 = ImageTk.PhotoImage(self.reynolds_1)

    def equation(self, Re, densi, um, d, u):
        self.Reyn_1 = Reynolds(Re=Re, densi=densi, Um=um, d=d, U=u)

    def show(self):
        ttk.Label(self, text=f'{self.Reyn_1.solucion()}').grid(row=9, column=4)
