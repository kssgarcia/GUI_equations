import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk

from Transferencia_calor import *



class Nusselt_1(ttk.Frame):
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
        ttk.Label(self, text='Nusselt').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.nuss_1).grid(row=1, column=0)
        ttk.Label(self, image=self.nuss_2).grid(row=1, column=2)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='nuss').grid(row=4, column=0)
        ttk.Label(self, text='Pr').grid(row=7, column=0)
        ttk.Label(self, text='n').grid(row=8, column=0)
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

        self.n = ttk.Entry(self)
        self.n.grid(row=8, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'nuss': self.nuss.get(), 'Pr': self.Pr.get(), 'n': self.n.get()}
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
        self.nuss_1 = Image.open("images\\nuss_1.PNG")
        self.nuss_1 = self.nuss_1.resize((200, 50))
        self.nuss_1 = ImageTk.PhotoImage(self.nuss_1)
        # image 2
        self.nuss_2 = Image.open("images\\nuss_2.PNG")
        self.nuss_2 = self.nuss_2.resize((200, 50))
        self.nuss_2 = ImageTk.PhotoImage(self.nuss_2)

    def equation(self, Re, nuss, Pr, n):
        self.Nusselt_1 = Nusselt1(Re=Re, nuss=nuss, Pr=Pr, n=n)

    def show(self):
        ttk.Label(self, text=f'{self.Nusselt_1.solucion_total()}').grid(row=9, column=4)

class Nusselt_2(ttk.Frame):
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
        ttk.Label(self, image=self.nuss_4img).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='nuss').grid(row=4, column=0)
        ttk.Label(self, text='Pr').grid(row=7, column=0)
        ttk.Label(self, text='U[m/s]').grid(row=8, column=0)
        ttk.Label(self, text='Um[kg/m*s]').grid(row=9, column=0)
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

        self.U = ttk.Entry(self)
        self.U.grid(row=8, column=1, columnspan=2)

        self.Um = ttk.Entry(self)
        self.Um.grid(row=9, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'nuss': self.nuss.get(), 'Pr': self.Pr.get(), 'U': self.U.get(), 'Um': self.Um.get()}
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
        self.nuss_4img = Image.open("images\\nuss_4.PNG")
        self.nuss_4img = self.nuss_4img.resize((400, 200))
        self.nuss_4img = ImageTk.PhotoImage(self.nuss_4img)

    def equation(self, Re, nuss, Pr, U, Um):
        self.nusselt_1 = Nusselt2(Re=Re, nuss=nuss, Pr=Pr, U=U, Um=Um)

    def show(self):
        ttk.Label(self, text=f'{self.nusselt_1}').grid(row=9, column=3)

class Nusselt_3(ttk.Frame):
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
        ttk.Label(self, image=self.nuss_5img).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='nuss').grid(row=4, column=0)
        ttk.Label(self, text='Pr').grid(row=5, column=0)
        ttk.Label(self, text='d[m]').grid(row=6, column=0)
        ttk.Label(self, text='L[m]').grid(row=7, column=0)
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

        self.d = ttk.Entry(self)
        self.d.grid(row=6, column=1, columnspan=2)

        self.L = ttk.Entry(self)
        self.L.grid(row=7, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'nuss': self.nuss.get(), 'Pr': self.Pr.get(), 'd': self.d.get(), 'L': self.L.get()}
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
        self.nuss_5img = Image.open("images\\nuss_5.PNG")
        self.nuss_5img = self.nuss_5img.resize((400, 200))
        self.nuss_5img = ImageTk.PhotoImage(self.nuss_5img)

    def equation(self, Re, nuss, Pr, d, L):
        self.nusselt_1 = Nusselt3(Re=Re, nuss=nuss, Pr=Pr, d=d, L=L)

    def show(self):
        ttk.Label(self, text=f'{self.nusselt_1}').grid(row=6, column=3)
    
class Nusselt_4(ttk.Frame):
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
        ttk.Label(self, text='Nusselt-4').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.nuss_6img).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='nuss').grid(row=4, column=0)
        ttk.Label(self, text='Pr').grid(row=5, column=0)
        ttk.Label(self, text='Ub[m]').grid(row=6, column=0)
        ttk.Label(self, text='Uw[m]').grid(row=7, column=0)
        ttk.Label(self, text='n').grid(row=8, column=0)
        ttk.Label(self, text='f').grid(row=9, column=0)
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

        self.Ub = ttk.Entry(self)
        self.Ub.grid(row=6, column=1, columnspan=2)

        self.Uw = ttk.Entry(self)
        self.Uw.grid(row=7, column=1, columnspan=2)

        self.n = ttk.Entry(self)
        self.n.grid(row=8, column=1, columnspan=2)

        self.f = ttk.Entry(self)
        self.f.grid(row=9, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'nuss': self.nuss.get(), 'Pr': self.Pr.get(), 'Ub': self.Ub.get(), 'Uw': self.Uw.get(), 'n': self.n.get(), 'f': self.f.get()}
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
        self.nuss_6img = Image.open("images\\nuss_6.PNG")
        self.nuss_6img = self.nuss_6img.resize((400, 200))
        self.nuss_6img = ImageTk.PhotoImage(self.nuss_6img)

    def equation(self, nuss, Re, Pr, Ub, Uw, n, f):
        self.nusselt_1 = Nusselt4(nuss=nuss, Re=Re, Pr=Pr, Ub=Ub, Uw=Uw, n=n, f=f)

    def show(self):
        ttk.Label(self, text=f'{self.nusselt_1}').grid(row=9, column=3)


class Nusselt_5(ttk.Frame):
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
        ttk.Label(self, text='Nusselt-5').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.nuss_7img).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='nuss').grid(row=4, column=0)
        ttk.Label(self, text='Pr').grid(row=5, column=0)
        ttk.Label(self, text='d[m]').grid(row=6, column=0)
        ttk.Label(self, text='L[m]').grid(row=7, column=0)
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

        self.d = ttk.Entry(self)
        self.d.grid(row=6, column=1, columnspan=2)

        self.L = ttk.Entry(self)
        self.L.grid(row=7, column=1, columnspan=2)
    

    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'nuss': self.nuss.get(), 'Pr': self.Pr.get(), 'd': self.d.get(), 'L': self.L.get()}
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
        self.nuss_7img = Image.open("images\\nuss_7.PNG")
        self.nuss_7img = self.nuss_7img.resize((400, 200))
        self.nuss_7img = ImageTk.PhotoImage(self.nuss_7img)

    def equation(self, Re, nuss, Pr, d, L):
        self.nusselt_1 = Nusselt5(Re=Re, nuss=nuss, Pr=Pr, d=d, L=L)

    def show(self):
        ttk.Label(self, text=f'{self.nusselt_1}').grid(row=6, column=3)

class Nusselt_6(ttk.Frame):
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
        ttk.Label(self, text='Nusselt-6').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.nuss_4img).grid(row=1, column=1)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='nuss').grid(row=4, column=0)
        ttk.Label(self, text='Pr').grid(row=5, column=0)
        ttk.Label(self, text='U[m/s]').grid(row=6, column=0)
        ttk.Label(self, text='Um[kg/m*s]').grid(row=7, column=0)
        ttk.Label(self, text='d[m]').grid(row=8, column=0)
        ttk.Label(self, text='L[m]').grid(row=9, column=0)
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

        self.U = ttk.Entry(self)
        self.U.grid(row=6, column=1, columnspan=2)

        self.Um = ttk.Entry(self)
        self.Um.grid(row=7, column=1, columnspan=2)

        self.d = ttk.Entry(self)
        self.d.grid(row=8, column=1, columnspan=2)

        self.L = ttk.Entry(self)
        self.L.grid(row=9, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'nuss': self.nuss.get(), 'Pr': self.Pr.get(), 'U': self.U.get(), 'Um': self.Um.get(), 'd': self.d.get(), 'L': self.L.get()}
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
        self.nuss_4img = Image.open("images\\nuss_8.PNG")
        self.nuss_4img = self.nuss_4img.resize((400, 200))
        self.nuss_4img = ImageTk.PhotoImage(self.nuss_4img)

    def equation(self, nuss, Re, Pr, d, L, U, Um):
        self.nusselt_1 = Nusselt6(Re=Re, nuss=nuss, Pr=Pr, U=U, Um=Um, d=d, L=L)

    def show(self):
        ttk.Label(self, text=f'{self.nusselt_1}').grid(row=9, column=3)


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
