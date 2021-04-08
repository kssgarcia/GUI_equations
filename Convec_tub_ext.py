import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk

from Transferencia_calor import * 
from Ecuaciones_externo import * 


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



class Nusselt_1_ext(ttk.Frame):
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
        ttk.Label(self, text='Nusselt-1').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.nuss_1_ext).grid(row=1, column=1, columnspan=2)
        # Variables
        ttk.Label(self, text='h[w/m^2*s]').grid(row=2, column=0,)
        ttk.Label(self, text='d[m]').grid(row=3, column=0)
        ttk.Label(self, text='k[w/m*s]').grid(row=4, column=0)
        ttk.Label(self, text='C').grid(row=5, column=0)
        ttk.Label(self, text='U').grid(row=6, column=0)
        ttk.Label(self, text='Uf').grid(row=7, column=0)
        ttk.Label(self, text='n').grid(row=8, column=0)
        ttk.Label(self, text='Pr').grid(row=9, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.h = ttk.Entry(self)
        self.h.grid(row=2, column=1, columnspan=2)

        self.d = ttk.Entry(self)
        self.d.grid(row=3, column=1, columnspan=2)

        self.k = ttk.Entry(self)
        self.k.grid(row=4, column=1, columnspan=2)

        self.C = ttk.Entry(self)
        self.C.grid(row=5, column=1, columnspan=2)
        
        self.U = ttk.Entry(self)
        self.U.grid(row=6, column=1, columnspan=2)

        self.Uf = ttk.Entry(self)
        self.Uf.grid(row=7, column=1, columnspan=2)

        self.n = ttk.Entry(self)
        self.n.grid(row=8, column=1, columnspan=2)

        self.Pr = ttk.Entry(self)
        self.Pr.grid(row=9, column=1, columnspan=2)


    def get_entries(self):
        self.dict_entries = {'h': self.h.get(), 'd': self.d.get(), 'k': self.k.get(), 'C': self.C.get(),'U': self.U.get(), 'Uf': self.Uf.get(), 'n': self.n.get(), 'Pr': self.Pr.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=11, column=3)
        show.grid(row=11, column=4)


    def images(self):
        # image 1
        self.nuss_1_ext = Image.open("images\\ext_1_tub.PNG")
        self.nuss_1_ext = self.nuss_1_ext.resize((500, 150))
        self.nuss_1_ext = ImageTk.PhotoImage(self.nuss_1_ext)

    def equation(self, h, d, k, C, U, Uf, n, Pr):
        self.Nusselt_1 = Nusselt1_ext(h=h, d=d, k=k, C=C, U=U, Uf=Uf, n=n, Pr=Pr)

    def show(self):
        ttk.Label(self, text=f'{self.Nusselt_1.solucion_total()}').grid(row=9, column=3)

class Nusselt_2_ext(ttk.Frame):
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
        ttk.Label(self, text='Nusselt-2').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.nuss_4_ext).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='nuss').grid(row=4, column=0)
        ttk.Label(self, text='Pr').grid(row=7, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.Re = ttk.Entry(self)
        self.Re.grid(row=3, column=1, columnspan=2)

        self.nuss = ttk.Entry(self)
        self.nuss.grid(row=4, column=1, columnspan=2)

        self.Pr = ttk.Entry(self)
        self.Pr.grid(row=7, column=1, columnspan=2)




    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'nuss': self.nuss.get(), 'Pr': self.Pr.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=11, column=3)
        show.grid(row=11, column=4)


    def images(self):
        self.nuss_4_ext = Image.open("images\\tub_2_ext.PNG")
        self.nuss_4_ext = self.nuss_4_ext.resize((400, 80))
        self.nuss_4_ext = ImageTk.PhotoImage(self.nuss_4_ext)

    def equation(self, Re, nuss, Pr):
        self.nusselt_1 = Nusselt2_ext(Re=Re, nuss=nuss, Pr=Pr)

    def show(self):
        ttk.Label(self, text=f'{self.nusselt_1}').grid(row=9, column=3)

class Nusselt_3_ext(ttk.Frame):
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
        ttk.Label(self, text='Nusselt-3').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.nuss_5_ext).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='nuss').grid(row=4, column=0)
        ttk.Label(self, text='Pr').grid(row=5, column=0)
        ttk.Label(self, text='Prf').grid(row=6, column=0)
        ttk.Label(self, text='Prw').grid(row=7, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.Re = ttk.Entry(self)
        self.Re.grid(row=3, column=1, columnspan=2)

        self.nuss = ttk.Entry(self)
        self.nuss.grid(row=4, column=1, columnspan=2)

        self.Pr = ttk.Entry(self)
        self.Pr.grid(row=5, column=1, columnspan=2)

        self.Prf = ttk.Entry(self)
        self.Prf.grid(row=6, column=1, columnspan=2)

        self.Prw = ttk.Entry(self)
        self.Prw.grid(row=7, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'nuss': self.nuss.get(), 'Pr': self.Pr.get(), 'Prf': self.Prf.get(), 'Prw': self.Prw.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=8, column=4)
        show.grid(row=8, column=5)


    def images(self):
        self.nuss_5_ext = Image.open("images\\tub_3_ext.PNG")
        self.nuss_5_ext = self.nuss_5_ext.resize((400, 60))
        self.nuss_5_ext = ImageTk.PhotoImage(self.nuss_5_ext)

    def equation(self, Re, nuss, Pr, Prw, Prf):
        self.nusselt_1 = Nusselt3_ext(Re=Re, nuss=nuss, Pr=Pr, Prw=Prw, Prf=Prf)

    def show(self):
        ttk.Label(self, text=f'{self.nusselt_1}').grid(row=6, column=3)
    
class Nusselt_4_ext(ttk.Frame):
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
        ttk.Label(self, text='Nusselt-3').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.nuss_6_ext).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='nuss').grid(row=4, column=0)
        ttk.Label(self, text='Pr').grid(row=5, column=0)
        ttk.Label(self, text='Prf').grid(row=6, column=0)
        ttk.Label(self, text='Prw').grid(row=7, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.Re = ttk.Entry(self)
        self.Re.grid(row=3, column=1, columnspan=2)

        self.nuss = ttk.Entry(self)
        self.nuss.grid(row=4, column=1, columnspan=2)

        self.Pr = ttk.Entry(self)
        self.Pr.grid(row=5, column=1, columnspan=2)

        self.Prf = ttk.Entry(self)
        self.Prf.grid(row=6, column=1, columnspan=2)

        self.Prw = ttk.Entry(self)
        self.Prw.grid(row=7, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'nuss': self.nuss.get(), 'Pr': self.Pr.get(), 'Prf': self.Prf.get(), 'Prw': self.Prw.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=8, column=4)
        show.grid(row=8, column=5)


    def images(self):
        self.nuss_6_ext = Image.open("images\\tub_4_ext.PNG")
        self.nuss_6_ext = self.nuss_6_ext.resize((400, 60))
        self.nuss_6_ext = ImageTk.PhotoImage(self.nuss_6_ext)

    def equation(self, Re, nuss, Pr, Prw, Prf):
        self.nusselt_1 = Nusselt4_ext(Re=Re, nuss=nuss, Pr=Pr, Prw=Prw, Prf=Prf)

    def show(self):
        ttk.Label(self, text=f'{self.nusselt_1}').grid(row=6, column=3)

class Nusselt_5_ext(ttk.Frame):
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
        ttk.Label(self, text='Nusselt-3').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.nuss_7_ext).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='nuss').grid(row=4, column=0)
        ttk.Label(self, text='Pr').grid(row=5, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.Re = ttk.Entry(self)
        self.Re.grid(row=3, column=1, columnspan=2)

        self.nuss = ttk.Entry(self)
        self.nuss.grid(row=4, column=1, columnspan=2)

        self.Pr = ttk.Entry(self)
        self.Pr.grid(row=5, column=1, columnspan=2)

    


    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'nuss': self.nuss.get(), 'Pr': self.Pr.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=8, column=4)
        show.grid(row=8, column=5)


    def images(self):
        self.nuss_7_ext = Image.open("images\\tub_5_ext.PNG")
        self.nuss_7_ext = self.nuss_7_ext.resize((430, 60))
        self.nuss_7_ext = ImageTk.PhotoImage(self.nuss_7_ext)

    def equation(self, Re, nuss, Pr):
        self.nusselt_1 = Nusselt5_ext(Re=Re, nuss=nuss, Pr=Pr)

    def show(self):
        ttk.Label(self, text=f'{self.nusselt_1}').grid(row=6, column=3)

class Nusselt_6_ext(ttk.Frame):
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
        ttk.Label(self, text='Nusselt-3').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.nuss_8_ext).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='nuss').grid(row=4, column=0)
        ttk.Label(self, text='Pr').grid(row=5, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.Re = ttk.Entry(self)
        self.Re.grid(row=3, column=1, columnspan=2)

        self.nuss = ttk.Entry(self)
        self.nuss.grid(row=4, column=1, columnspan=2)

        self.Pr = ttk.Entry(self)
        self.Pr.grid(row=5, column=1, columnspan=2)

    


    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'nuss': self.nuss.get(), 'Pr': self.Pr.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=8, column=4)
        show.grid(row=8, column=5)


    def images(self):
        self.nuss_8_ext = Image.open("images\\tub_6_ext.PNG")
        self.nuss_8_ext = self.nuss_8_ext.resize((430, 60))
        self.nuss_8_ext = ImageTk.PhotoImage(self.nuss_8_ext)

    def equation(self, Re, nuss, Pr):
        self.nusselt_1 = Nusselt6_ext(Re=Re, nuss=nuss, Pr=Pr)

    def show(self):
        ttk.Label(self, text=f'{self.nusselt_1}').grid(row=6, column=3)

class Nusselt_7_ext(ttk.Frame):
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
        ttk.Label(self, text='Nusselt-3').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.nuss_9_ext).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='nuss').grid(row=3, column=0)
        ttk.Label(self, text='Ped').grid(row=4, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.nuss = ttk.Entry(self)
        self.nuss.grid(row=3, column=1, columnspan=2)

        self.Ped = ttk.Entry(self)
        self.Ped.grid(row=4, column=1, columnspan=2)


    


    def get_entries(self):
        self.dict_entries = {'nuss': self.nuss.get(), 'Ped': self.Ped.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=8, column=4)
        show.grid(row=8, column=5)


    def images(self):
        self.nuss_9_ext = Image.open("images\\tub_7_ext.PNG")
        self.nuss_9_ext = self.nuss_9_ext.resize((430, 60))
        self.nuss_9_ext = ImageTk.PhotoImage(self.nuss_9_ext)

    def equation(self, nuss, Ped):
        self.nusselt_1 = Nusselt7_ext(nuss=nuss, Ped=Ped)

    def show(self):
        ttk.Label(self, text=f'{self.nusselt_1}').grid(row=6, column=3)

class bancos_ext(ttk.Frame):
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
        ttk.Label(self, text='Bancos').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.img_bancos).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='nuss').grid(row=4, column=0)
        ttk.Label(self, text='Pr').grid(row=5, column=0)
        ttk.Label(self, text='Prs').grid(row=6, column=0)
        ttk.Label(self, text='C').grid(row=7, column=0)
        ttk.Label(self, text='m').grid(row=8, column=0)
        ttk.Label(self, text='n').grid(row=9, column=0)
        # button to q
        ttk.Button(self, text="Salir", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.Re = ttk.Entry(self)
        self.Re.grid(row=3, column=1, columnspan=2)

        self.nuss = ttk.Entry(self)
        self.nuss.grid(row=4, column=1, columnspan=2)

        self.Pr = ttk.Entry(self)
        self.Pr.grid(row=5, column=1, columnspan=2)

        self.Prs = ttk.Entry(self)
        self.Prs.grid(row=6, column=1, columnspan=2)

        self.C = ttk.Entry(self)
        self.C.grid(row=7, column=1, columnspan=2)

        self.m = ttk.Entry(self)
        self.m.grid(row=8, column=1, columnspan=2)

        self.n = ttk.Entry(self)
        self.n.grid(row=9, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'nuss': self.nuss.get(), 'Pr': self.Pr.get(), 'Prs': self.Prs.get(), 'm': self.m.get(), 'n': self.n.get(), 'C': self.C.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=8, column=4)
        show.grid(row=8, column=5)


    def images(self):
        self.img_bancos = Image.open("images\\ecuacion_bancos.PNG")
        self.img_bancos = self.img_bancos.resize((500, 500))
        self.img_bancos = ImageTk.PhotoImage(self.img_bancos)

    def equation(self, Re, nuss, Pr, Prs, C, m, n):
        self.nusselt_1 = bancos(Re=Re, nuss=nuss, Pr=Pr, Prs=Prs, C=C, m=m, n=n)

    def show(self):
        ttk.Label(self, text=f'{self.nusselt_1}').grid(row=7, column=3)
    
class Tablas(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.images()
        # Widgets
        self.labels_pictures()

    def labels_pictures(self):
        # create the button and set the command
        # Title
        ttk.Label(self, text='Tablas').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.tabla_1).grid(row=1, column=1)
        ttk.Label(self, image=self.tabla_2).grid(row=1, column=2)
        ttk.Label(self, image=self.tabla_3).grid(row=2, column=1)
        ttk.Label(self, image=self.tabla_4).grid(row=2, column=2)
        # Variables

    def images(self):
        # image 1
        self.tabla_1 = Image.open("images\\Tabla_1_emp.PNG")
        self.tabla_1 = self.tabla_1.resize((400, 400))
        self.tabla_1 = ImageTk.PhotoImage(self.tabla_1)
        # image 2
        self.tabla_2 = Image.open("images\\Tabla_2_emp.PNG")
        self.tabla_2 = self.tabla_2.resize((400, 400))
        self.tabla_2 = ImageTk.PhotoImage(self.tabla_2)
        # image 3
        self.tabla_3 = Image.open("images\\Tabla_3_emp.PNG")
        self.tabla_3 = self.tabla_3.resize((400, 400))
        self.tabla_3 = ImageTk.PhotoImage(self.tabla_3)
        # image 4
        self.tabla_4 = Image.open("images\\Tabla_4_emp.PNG")
        self.tabla_4 = self.tabla_4.resize((400, 400))
        self.tabla_4 = ImageTk.PhotoImage(self.tabla_4)