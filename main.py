import tkinter as tk
from PIL import Image, ImageTk
from Transferencia_calor import *


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # create the button and set the command
        self.muros = tk.Button(self, text="Muros", command=self.managed_windows)
        self.reynolds = tk.Button(self, text="Reynolds")
        self.nusselt = tk.Button(self, text="Nusselt")
        self.quit = tk.Button(self, text="Quit", command=self.master.destroy)
        # Grid the buttons
        self.Grid_set()

    def Grid_set(self):
        self.muros.grid(row=0, column=0)
        self.reynolds.grid(row=1, column=0)
        self.nusselt.grid(row=2, column=0)
        self.quit.grid(row=3, column=0)

    def managed_windows(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('500x500')
        self.app = window_muros(self.newWindow)


class window_muros(tk.Frame):
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
        tk.Label(self, text='MUROS',).grid(row=0, column=1, columnspan=2)
        # Images
        tk.Label(self, image=self.muro1).grid(row=1, column=0, columnspan=2)
        tk.Label(self, image=self.muro2).grid(row=1, column=3, columnspan=2)
        # labels for entries
        tk.Label(self, text='Q').grid(row=3, column=0)
        tk.Label(self, text='T1').grid(row=4, column=0)
        tk.Label(self, text='T2').grid(row=5, column=0)
        # conveccion
        tk.Label(self, text='h').grid(row=6, column=0)
        tk.Label(self, text='Ac').grid(row=7, column=0)
        # para muros
        tk.Label(self, text='L').grid(row=8, column=0)
        tk.Label(self, text='k').grid(row=9, column=0)
        tk.Label(self, text='A').grid(row=10, column=0)
        # button to q
        tk.Button(self, text="Quit", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.Q = tk.Entry(self, text='Q')
        self.Q.grid(row=3, column=1, columnspan=2)
        self.T1 = tk.Entry(self, text='T1')
        self.T1.grid(row=4, column=1, columnspan=2)
        self.T2 = tk.Entry(self, text='T2')
        self.T2.grid(row=5, column=1, columnspan=2)
        # conveccion
        self.h = tk.Entry(self, text='h')
        self.h.grid(row=6, column=1, columnspan=2)
        self.Ac = tk.Entry(self, text='Ac')
        self.Ac.grid(row=7, column=1, columnspan=2)
        # para muros
        self.L = tk.Entry(self, text='L')
        self.L.grid(row=8, column=1, columnspan=2)
        self.k = tk.Entry(self, text='k')
        self.k.grid(row=9, column=1, columnspan=2)
        self.A = tk.Entry(self, text='A')
        self.A.grid(row=10, column=1, columnspan=2)


    def get_entries(self):
        self.dict_entries = {'Q': self.Q.get(), 'T1': self.T1.get(), 'T2': self.T2.get(), 'h': self.h.get(), 'Ac': self.Ac.get(), 'L': self.L.get()\
            , 'k': self.A.get(), 'A': self.A.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = tk.Button(self, text='Save', command=self.get_entries)
        save.grid(row=10, column=4)


    def images(self):
        # image 1
        self.muro1 = Image.open("images\\muros1.PNG")
        self.muro1 = self.muro1.resize((200, 200))
        self.muro1 = ImageTk.PhotoImage(self.muro1)
        # image 2
        self.muro2 = Image.open("images\\muros2.PNG")
        self.muro2 = self.muro2.resize((200, 200))
        self.muro2 = ImageTk.PhotoImage(self.muro2)


    def equation(self, Q, T1, T2, h, Ac, L, k, A):
        Muros.Q = Q
        Muros.T1 = T1
        Muros.T2 = T2
        Muros.conveccion(h=h, Ac=Ac)
        muro_1 = Muros(L=L/1000, k=k, A=A)
        # muro_2 = Muros(L=L/1000, k=k, A=A)
        # muro_3 = Muros(L=L/1000, k=k, A=A)
        # Muros.conveccion(h=h, Ac=Ac)
        print(muro_1.Solucion())


master = tk.Tk()
master.geometry('200x150')
app = GUI(master=master)
app.mainloop()

