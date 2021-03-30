import tkinter as tk
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
        self.newWindow.geometry('400x400')
        self.app = window_muros(self.newWindow)


class window_muros(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.images()
        # create the button and set the command
        self.title = tk.Label(self, text='MUROS',)
        self.pic_muros1 = tk.Label(self, image=self.muro1)
        self.pic_muros2 = tk.Label(self, image=self.muro2)
        self.v1 = tk.Button(self, text='Quit', width=25)
        self.v2 = tk.Button(self, text='Quit', width=25)
        self.v3 = tk.Button(self, text='Quit', width=25)
        self.quit = tk.Button(self, text="Quit", command=self.master.destroy)
        # Grid the buttons
        self.Grid_set()

    def Grid_set(self):
        self.title.grid(row=0, column=1, pady=2)
        self.pic_muros1.grid(row=0, column=1, pady=2)
        self.pic_muros2.grid(row=3, column=1, pady=2)
        self.v1.grid(row=2, column=0)
        self.v2.grid(row=3, column=0)
        self.v3.grid(row=4, column=0)
        self.quit.grid(row=5,column=0)

    def images(self):
        self.muro1 = tk.PhotoImage(file="images\\muros1.PNG")
        self.muro2 = tk.PhotoImage(file="images\\muros2.PNG")

master = tk.Tk()
master.geometry('200x400')
app = GUI(master=master)
app.mainloop()
