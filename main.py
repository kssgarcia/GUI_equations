import tkinter as tk
from PIL import Image, ImageTk
from Transferencia_calor import *


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # create the button and set the command
        self.radiacion = tk.Button(self, text="Radiacion", command=self.managed_windows)
        self.reynolds = tk.Button(self, text="Reynolds")
        self.nusselt = tk.Button(self, text="Nusselt")
        self.quit = tk.Button(self, text="Quit", command=self.master.destroy)
        # Grid the buttons
        self.Grid_set()

    def Grid_set(self):
        self.radiacion.grid(row=0, column=0)
        self.reynolds.grid(row=1, column=0)
        self.nusselt.grid(row=2, column=0)
        self.quit.grid(row=3, column=0)

    def managed_windows(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('500x500')
        self.app = window_radiacion(self.newWindow)

#---------------------------------------------Radiacion------------------------------------------
class window_radiacion(tk.Frame):
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
        tk.Label(self, text='Radiacion').grid(row=0, column=1, columnspan=2)
        # Images
        tk.Label(self, image=self.radia1).grid(row=1, column=0, columnspan=2)
        # Variables
        tk.Label(self, text='q').grid(row=3, column=0)
        tk.Label(self, text='E').grid(row=4, column=0)
        tk.Label(self, text='A').grid(row=5, column=0)
        tk.Label(self, text='T1').grid(row=6, column=0)
        tk.Label(self, text='T2').grid(row=7, column=0)
        # button to q
        tk.Button(self, text="Quit", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.q = tk.Entry(self)
        self.q.grid(row=3, column=1, columnspan=2)

        self.E = tk.Entry(self)
        self.E.grid(row=4, column=1, columnspan=2)

        self.A = tk.Entry(self)
        self.A.grid(row=5, column=1, columnspan=2)

        self.T1 = tk.Entry(self)
        self.T1.grid(row=6, column=1, columnspan=2)

        self.T2 = tk.Entry(self)
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
        save = tk.Button(self, text='Save', command=self.get_entries)
        show = tk.Button(self, text='Show', command=self.show)
        save.grid(row=10, column=4)
        show.grid(row=10, column=5)


    def images(self):
        # image 1
        self.radia1 = Image.open("images\\radia1.PNG")
        self.radia1 = self.radia1.resize((200, 200))
        self.radia1 = ImageTk.PhotoImage(self.radia1)

    def equation(self, q, E, A, T1, T2):
        self.Radia_1 = Radiacion(q=q, A=A, T1=T1, T2=T2, E=E)

    def show(self):
        tk.Label(self, text=f'{self.Radia_1.solucion()}').grid(row=9, column=4)

master = tk.Tk()
master.geometry('200x150')
app = GUI(master=master)
app.mainloop()

