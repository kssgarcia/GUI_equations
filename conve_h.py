import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk

from Transferencia_calor import * 


class h_conveccion(ttk.Frame):
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
        ttk.Label(self, text='h-conveccion').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.h_1).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='nuss').grid(row=3, column=0)
        ttk.Label(self, text='h[w/m^2*°C]').grid(row=4, column=0)
        ttk.Label(self, text='k[w/m*°C]').grid(row=7, column=0)
        ttk.Label(self, text='d[m]').grid(row=8, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.nuss = ttk.Entry(self)
        self.nuss.grid(row=3, column=1, columnspan=2)

        self.h = ttk.Entry(self)
        self.h.grid(row=4, column=1, columnspan=2)

        self.k = ttk.Entry(self)
        self.k.grid(row=7, column=1, columnspan=2)

        self.d = ttk.Entry(self)
        self.d.grid(row=8, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'h': self.h.get(), 'nuss': self.nuss.get(), 'k': self.k.get(), 'd': self.d.get()}
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
        self.h_1 = Image.open("images\\h_convecc.PNG")
        self.h_1 = self.h_1.resize((200, 200))
        self.h_1 = ImageTk.PhotoImage(self.h_1)


    def equation(self, nuss, d, h, k):
        self.Nusselt_1 = convecc_h(nuss=nuss, d=d, h=h, k=k)

    def show(self):
        ttk.Label(self, text=f'{self.Nusselt_1.solucion_total()}').grid(row=9, column=4)


