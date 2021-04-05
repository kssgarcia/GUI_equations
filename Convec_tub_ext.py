import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk

from Transferencia_calor import * 



class fuerza_arrastre(ttk.Frame):
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
        ttk.Label(self, text='Fuerza arrastre').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.arrastre_1).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='Fd').grid(row=2, column=0)
        ttk.Label(self, text='Cd').grid(row=3, column=0)
        ttk.Label(self, text='A').grid(row=4, column=0)
        ttk.Label(self, text='densi').grid(row=5, column=0)
        ttk.Label(self, text='U').grid(row=6, column=0)
        ttk.Label(self, text='g').grid(row=7, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=8,column=0)


    def Entries(self):
        # labels for entries
        self.Fd = ttk.Entry(self)
        self.Fd.grid(row=2, column=1, columnspan=2)

        self.Cd = ttk.Entry(self)
        self.Cd.grid(row=3, column=1, columnspan=2)

        self.A = ttk.Entry(self)
        self.A.grid(row=4, column=1, columnspan=2)

        self.densi = ttk.Entry(self)
        self.densi.grid(row=5, column=1, columnspan=2)

        self.U = ttk.Entry(self)
        self.U.grid(row=6, column=1, columnspan=2)

        self.g = ttk.Entry(self)
        self.g.grid(row=7, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'Fd': self.Fd.get(), 'Cd': self.Cd.get(), 'A': self.A.get(), 'densi': self.densi.get(), 'U': self.U.get(), 'g': self.g.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=9, column=4)
        show.grid(row=9, column=5)


    def images(self):
        # image 1
        self.arrastre_1 = Image.open("images\\arrastre_1.PNG")
        self.arrastre_1 = self.arrastre_1.resize((300, 300))
        self.arrastre_1 = ImageTk.PhotoImage(self.arrastre_1)

    def equation(self, Fd, Cd, A, densi, U, g):
        self.arrastre = fuerza_arrast(Fd=Fd, Cd=Cd, A=A, densi=densi, U=U, g=g)

    def show(self):
        ttk.Label(self, text=f'{self.arrastre}').grid(row=8, column=4)
