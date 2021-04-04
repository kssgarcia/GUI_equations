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
        self.nusselt = ttk.Button(self, text="Nusselt", command=self.window_nusselt)
        self.quit = ttk.Button(self, text="Salir", command=self.master.destroy)
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
        self.app = window_Radia(self.newWindow)

    def window_reynolds(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Reynolds')
        self.newWindow.geometry('500x500')
        self.app = Reynolds_class(self.newWindow)
    def window_nusselt(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt')
        self.newWindow.geometry('400x550')
        self.app = window_Nusselt(self.newWindow)


class window_Radia(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # create the buttons and set the command
        self.forradiacion = ttk.Button(self, text="Formula-Radicion", command=self.managed_windows)
        self.radbblack = ttk.Button(self, text="Radiacion de cuerpo negro", command=self.body_black_radiation)
        self.velocidad_luz = ttk.Button(self,text="Velocidad de la luz",command=self.velocidad_luz_radiation)
        self.quit = ttk.Button(self, text="Quit", command=self.master.destroy)
        # Grid the buttons
        self.forradiacion.grid(row=0, column=0)
        self.radbblack.grid(row=1, column=0)
        self.quit.grid(row=2, column=0)
    
    def managed_windows(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Radiacion')
        self.newWindow.geometry('600x500')
        self.app = window_radiacion(self.newWindow)
    def body_black_radiation(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Cuerpo-negro')
        self.newWindow.geometry('600x500')
        self.app = cuerpo_negro(self.newWindow)
    def velocidad_luz_radiation(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Velocidad de la luz')
        self.newWindow.geometry('600x500')
        self.app = light_speed(self.newWindow)

class window_Nusselt(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.images()
        ttk.Label(self, image=self.nuss_3img).grid(row=0, column=1)
        # create the buttons and set the command
        self.var_1 = ttk.Button(self, text="Nusselt-1", command=self.nuss_1)
        self.var_2 = ttk.Button(self, text="Nusselt-2", command=self.nuss_2)
        self.var_3 = ttk.Button(self, text="Nusselt-3", command=self.nuss_3)
        self.var_4 = ttk.Button(self, text="Nusselt-4", command=self.nuss_4)
        self.var_5 = ttk.Button(self, text="Nusselt-5", command=self.nuss_5)
        self.var_6 = ttk.Button(self, text="Nusselt-6", command=self.nuss_6)
        self.quit = ttk.Button(self, text="Salir", command=self.master.destroy)
        # Grid the buttons
        self.var_1.grid(row=1, column=1)
        self.var_2.grid(row=2, column=1)
        self.var_3.grid(row=3, column=1)
        self.var_4.grid(row=4, column=1)
        self.var_5.grid(row=5, column=1)
        self.var_6.grid(row=6, column=1)
        self.quit.grid(row=7, column=1)
    def images(self):
        self.nuss_3img = Image.open("images\\nuss_3.PNG")
        self.nuss_3img = self.nuss_3img.resize((300, 300))
        self.nuss_3img = ImageTk.PhotoImage(self.nuss_3img)


    def nuss_1(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-1')
        self.newWindow.geometry('600x300')
        self.app = Nusselt_1(self.newWindow)
    def nuss_2(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-2')
        self.newWindow.geometry('700x450')
        self.app = Nusselt_2(self.newWindow)
    def nuss_3(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-3')
        self.newWindow.geometry('700x450')
        self.app = Nusselt_3(self.newWindow)
    def nuss_4(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-4')
        self.newWindow.geometry('700x550')
        self.app = Nusselt_4(self.newWindow)
    def nuss_5(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-5')
        self.newWindow.geometry('700x450')
        self.app = Nusselt_5(self.newWindow)
    def nuss_6(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Nusselt-6')
        self.newWindow.geometry('800x500')
        self.app = Nusselt_6(self.newWindow)
#---------------------------------------------Radiacion------------------------------------------
class light_speed(ttk.Frame):
   def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.imagenes_luz()
        # Widgets
        self.labels_luz()
        self.Entradas_luz()
        self.Botones_luz()
    def labels_luz(self):
        # Title
        ttk.Label(self, text='Velocidad de la luz').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.luz).grid(row=1, column=0, columnspan=2)
        #Variables
        ttk.Label(self, text='Longitud de onda [lambda]').grid(row=3, column=0)
        ttk.Label(self, text='Frecuencia [v]').grid(row=4, column=0)

    def Entradas(self):
        # labels for entries
        self.lamb = ttk.Entry(self)
        self.lamb.grid(row=3, column=1, columnspan=2)

        self.v = ttk.Entry(self)
        self.v.grid(row=4, column=1, columnspan=2)

    def Botones(self):
        save = ttk.Button(self, text='Guardar',command=self.obtener_entradas_luz)
        show = ttk.Button(self, text='Calcular', command=self.mostrar_luz)
        quit1 = ttk.Button(self, text="Salir", command=self.master.destroy)
        save.grid(row=10, column=1)
        show.grid(row=10, column=2)
        quit1.grid(row=10, column=3)

    def imagenes(self):
        # image 1
        self.luz = Image.open("images\\luz.JPG")
        self.luz = self.luz.resize((250, 200))
        self.luz = ImageTk.PhotoImage(self.luz)

    def obtener_entradas(self):
        self.dict2_entries = {'lamb': self.p.get(), 'v': self.o.get()}
        for item, value in self.dict2_entries.items():
            if value == 'None':
                self.dict2_entries[item] = None
            elif type(value) is str:
                self.dict2_entries[item] = float(value)
        self.vel_light(**self.dict2_entries)

    def vel_light(self, lamb, v):
        self.Radia_light = Radiacion_formula_luz(lamb=lamb, v=v)

    def mostrar(self):
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
        self.newWindow.title('Table')
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

#---------------------------------------------Nusselt------------------------------------------
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

master = ThemedTk(themebg=True)
#ubuntu
master.set_theme('breeze')
master.geometry('200x150')
app = GUI(master=master)
app.mainloop()