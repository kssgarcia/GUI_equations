import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk
from Transferencia_calor import * 

class rap_masa_flujo(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.imagenes_rmf()
        # Widgets
        self.labels_rmf()
        self.Entradas_rmf()
        self.Botones_rmf()

    def Entradas_rmf(self):
     # labels for entries
        self.m = ttk.Entry(self)
        self.m.grid(row=3, column=1, columnspan=2)
        self.p = ttk.Entry(self)
        self.p.grid(row=4, column=1, columnspan=2) 
        self.Vm = ttk.Entry(self)
        self.Vm.grid(row=5,column=1,columnspan=2) 
        self.A = ttk.Entry(self)
        self.A.grid(row=6,column=1,columnspan=2)
    def labels_rmf(self):
         # Title
        ttk.Label(self, text='Rapidez de masa de flujo').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.rmf).grid(row=1, column=0, columnspan=3)
        #Variables
        ttk.Label(self, text='Rapidez de la masa de flujo [Kg/s]').grid(row=3, column=0)
        ttk.Label(self, text='Densidad [kg/m3]').grid(row=4, column=0) 
        ttk.Label(self, text='Velocidad media[m/s]').grid(row=5, column=0) 
        ttk.Label(self,text='Area [m2]').grid(row=6, column=0) 
    def Botones_rmf(self):
        save = ttk.Button(self, text='Guardar',command=self.obtener_entradas_rmf)
        show = ttk.Button(self, text='Calcular', command=self.mostrar_rmf)
        quit1 = ttk.Button(self, text="Salir", command=self.master.destroy)
        save.grid(row=10, column=1)
        show.grid(row=10, column=2)
        quit1.grid(row=10, column=3) 
    def imagenes_rmf(self):
        # image 1
        self.rmf = Image.open("images\\rmf.JPG")
        self.rmf = self.rmf.resize((250, 150))
        self.rmf = ImageTk.PhotoImage(self.rmf) 
    def obtener_entradas_rmf(self):
        self.dictt_entries = {'m': self.m.get(),'p': self.p.get(),'Vm':self.Vm.get(),'A':self.A.get()}
        for item, value in self.dictt_entries.items():
            if value == 'None':
                self.dictt_entries[item] = None
            elif type(value) is str:
                self.dictt_entries[item] = float(value)
        self.rmf_ecu(**self.dictt_entries)

    def rmf_ecu(self,m, p, Vm,A):
        self.Energy_rmf1 = rapidez_flujo(m=m,p=p, Vm=Vm,A=A)

    def mostrar_rmf(self):
        ttk.Label(self, text=f'{self.Energy_rmf1.solucion()}').grid(row=11, column=1)