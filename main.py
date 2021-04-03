import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk

from Transferencia_calor import *

class GUI(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # create the button and set the command
        self.radiacion = ttk.Button(self, text="Radiacion", command=self.window_radia)
        self.reynolds = ttk.Button(self, text="Reynolds", command=self.window_reynolds)
        self.nusselt = ttk.Button(self, text="Nusselt")
        self.quit = ttk.Button(self, text="Quit", command=self.master.destroy)
        # Grid the buttons
        self.Grid_set()

    def Grid_set(self):
        self.radiacion.grid(row=0, column=0)
        self.reynolds.grid(row=1, column=0)
        self.nusselt.grid(row=2, column=0)
        self.quit.grid(row=3, column=0)

    
    def window_radia(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('200x150')
        self.app = window1(self.newWindow)

    def window_reynolds(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('500x500')
        self.app = Reynolds_class(self.newWindow)

class window1(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # create the buttons and set the command
        self.forradiacion = ttk.Button(self, text="Formula-Radicion", command=self.managed_windows)
        self.radbblack = ttk.Button(self, text="Radiacion de cuerpo negro", command=self.body_black_radiation)
        self.quit = ttk.Button(self, text="Quit", command=self.master.destroy)
        # Grid the buttons
        self.forradiacion.grid(row=0, column=0)
        self.radbblack.grid(row=1, column=0)
        self.quit.grid(row=2, column=0)
    
    def managed_windows(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('600x500')
        self.app = window_radiacion(self.newWindow)
    def body_black_radiation(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('600x500')
        self.app = cuerpo_negro(self.newWindow)
#---------------------------------------------Radiacion------------------------------------------
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
        save = ttk.Button(self, text='Save', command=self.get_entries)
        show = ttk.Button(self, text='Show', command=self.show)
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



#---------------------------------------------Reynolds------------------------------------------
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
        ttk.Button(self, text="Quit", command=self.master.destroy).grid(row=11,column=0)


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
        save = ttk.Button(self, text='Save', command=self.get_entries)
        show = ttk.Button(self, text='Show', command=self.show)
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

#---------------------------------------------Nusselt------------------------------------------
# class window_Nusselt(ttk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         # Images 
#         self.images()
#         # Widgets
#         self.labels_pictures()
#         self.Entries()
#         self.Buttons()


#     def labels_pictures(self):
#         # create the button and set the command
#         # Title
#         ttk.Label(self, text='Nusselt').grid(row=0, column=1, columnspan=2)
#         # Images
#         ttk.Label(self, image=self.nuss_1).grid(row=1, column=0, columnspan=2)
#         # Variables
#         ttk.Label(self, text='Re').grid(row=3, column=0)
#         ttk.Label(self, text='h').grid(row=4, column=0)
#         ttk.Label(self, text='d').grid(row=5, column=0)
#         ttk.Label(self, text='k').grid(row=6, column=0)
#         ttk.Label(self, text='Pr').grid(row=7, column=0)
#         ttk.Label(self, text='n').grid(row=8, column=0)
#         # button to q
#         ttk.Button(self, text="Quit", command=self.master.destroy).grid(row=11,column=0)


#     def Entries(self):
#         # labels for entries
#         self.Re = ttk.Entry(self)
#         self.Re.grid(row=3, column=1, columnspan=2)

#         self.h = ttk.Entry(self)
#         self.h.grid(row=4, column=1, columnspan=2)

#         self.d = ttk.Entry(self)
#         self.d.grid(row=5, column=1, columnspan=2)

#         self.k = ttk.Entry(self)
#         self.k.grid(row=6, column=1, columnspan=2)

#         self.Pr = ttk.Entry(self)
#         self.Pr.grid(row=7, column=1, columnspan=2)

#         self.n = ttk.Entry(self)
#         self.n.grid(row=8, column=1, columnspan=2)
    


#     def get_entries(self):
#         self.dict_entries = {'Re': self.Re.get(), 'h': self.h.get(), 'd': self.d.get(), 'k': self.k.get(), 'Pr': self.Pr.get(), 'n': self.n.get()}
#         for item, value in self.dict_entries.items():
#             if value == 'None':
#                 self.dict_entries[item] = None
#             elif type(value) is str:
#                 self.dict_entries[item] = float(value)
#         self.equation(**self.dict_entries)


#     def Buttons(self):
#         save = ttk.Button(self, text='Save', command=self.get_entries)
#         show = ttk.Button(self, text='Show', command=self.show)
#         save.grid(row=11, column=4)
#         show.grid(row=11, column=5)


#     def images(self):
#         # image 1
#         self.nuss_1 = Image.open("images\\nuss_1.PNG")
#         self.nuss_1 = self.nuss_1.resize((200, 200))
#         self.nuss_1 = ImageTk.PhotoImage(self.nuss_1)

#     def equation(self, Re, h, d, k, Pr, n):
#         self.Nusselt_1 = Nusselt(Re=Re,h=h, d=d, k=k, Pr=Pr, n=n)

#     def show(self):
#         ttk.Label(self, text=f'{self.Nusselt_1.solucion_total()}').grid(row=9, column=4)

    
master = ThemedTk(themebg=True)
#ubuntu
master.set_theme('breeze')
master.geometry('200x150')
app = GUI(master=master)
app.mainloop()