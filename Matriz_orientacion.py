import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk


class Tablas_transfe(ttk.Frame):
    dicta = {'nuss_1': {'Flujo interno', 'Turbulento', 'Tubo liso', 'desarrollado', 'Propiedades fijas', 'None_6', 'Formula simple', 'Formula algebraica', 'Seccion tubo entrada','None_10'},
'nuss_2': {'Flujo interno', 'Turbulento', 'Tubo liso', 'desarrollado', 'Propiedades variables', 'None_6', 'Formula simple', 'Formula algebraica', 'Seccion tubo entrada','None_10'},
'nuss_3': {'Flujo interno', 'Turbulento', 'Tubo liso', 'desarrollado', 'Propiedades fijas', 'None_6', 'Formula simple', 'Formula algebraica', 'Seccion tubo entrada','None_10'},
'nuss_4': {'Flujo interno', 'Turbulento', 'rugoso', 'desarrollado', 'None_5', 'T calor constante', 'compleja',  'Formula algebraica', 'Seccion tubo entrada','None_10'},
'nuss_5': {'Flujo interno', 'Laminar', 'Tubo liso', 'desarrollado', 'None_5', 'T tubo constante', 'None_7',  'None_8', 'Seccion tubo entrada','None_10'},
'nuss_6': {'Flujo interno', 'Laminar', 'None_3', 'None_5', 'Propiedades variables', 'T tubo constante', 'None_7', 'None_8', 'None_9','None_10'}}

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # self.labels_pictures()
        self.images()
        ttk.Label(self, image=self.matriz_img).grid(row=0, column=0)
        self.entries()
        self.Buttons()

    def images(self):
        self.matriz_img = Image.open("images\\nuss_3.PNG")
        self.matriz_img = self.matriz_img.resize((400, 400))
        self.matriz_img = ImageTk.PhotoImage(self.matriz_img)
    
    def entries(self):
        self.example_1 = ttk.Combobox(self, values=('Flujo interno','Externo','None_1'))
        self.example_1.grid(row=3, column=0)
        self.example_2 = ttk.Combobox(self, values=('Laminar','Turbulento','None_2'))
        self.example_2.grid(row=4, column=0)
        self.example_3 = ttk.Combobox(self, values=('Tubo liso','rugoso','None_3'))
        self.example_3.grid(row=5, column=0)
        self.example_4 = ttk.Combobox(self, values=('No desarrollado','desarrollado','None_4'))
        self.example_4.grid(row=6, column=0)
        self.example_5 = ttk.Combobox(self, values=('Propiedades fijas','Propiedades variables','None_5'))
        self.example_5.grid(row=7, column=0)
        self.example_6 = ttk.Combobox(self, values=('T tubo constante','T calor constante','None_6'))
        self.example_6.grid(row=8, column=0)
        self.example_7 = ttk.Combobox(self, values=('Formula simple','compleja','None_7'))
        self.example_7.grid(row=9, column=0)
        self.example_8 = ttk.Combobox(self, values=('Formula algebraica','Grafica','None_8'))
        self.example_8.grid(row=10, column=0)
        self.example_9 = ttk.Combobox(self, values=('Seccion tubo entrada','a lo largo','None_9'))
        self.example_9.grid(row=11, column=0)
        self.example_10 = ttk.Combobox(self, values=('Propiedades pelicula','global','None_10'))
        self.example_10.grid(row=12, column=0)


    def get_entries(self):
        self.combo_values = {self.example_1.get(),self.example_2.get(),self.example_3.get(),self.example_4.get(),self.example_5.get(),self.example_6.get(),self.example_7.get(),self.example_8.get(),self.example_9.get(),self.example_10.get()}
        global_e = [0,0,0,0,0,0,0,0]
        current = {}
        self.equat = 0
        for key,values in Tablas_transfe.dicta.items():
            current = values.difference(self.combo_values)
            if len(list(current)) < len(list(global_e)):
                global_e = current
                self.equat = key
            elif 'rugoso' in self.combo_values:
                self.equat = 'nuss_4'
                break


    def Buttons(self):
        save = ttk.Button(self, text='Guardar', command=self.get_entries)
        show = ttk.Button(self, text='Calcular', command=self.show)
        save.grid(row=12, column=3)
        show.grid(row=12, column=4)

    def show(self):
        ttk.Label(self, text=f'{self.equat}').grid(row=8, column=3)


