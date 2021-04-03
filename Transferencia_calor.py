from sympy import symbols, Eq, solve

# -----------------------------------------------------------Calor Radiacion-Formula----------------------------------

class Radiacion:
    incog = 0

    def __init__(self, q, A, T1, T2, E):
        self.q = q
        self.A = A
        self.T1 = T1
        self.T2 = T2
        self.E = E
        if self.q == None:
            self.q = symbols('q')
            Radiacion.incog = self.q
        elif self.A == None:
            self.A = symbols('A')
            Radiacion.incog = self.A
        elif self.T1 == None:
            self.T1 = symbols('T1')
            Radiacion.incog = self.T1
        elif self.T2 == None:
            self.T2 = symbols('T2')
            Radiacion.incog = self.T2
        elif self.E == None:
            self.E = symbols('E')
            Radiacion.incog = self.E

    def solucion(self, solv=None):

        ecuacion = Eq(self.E*(5.669E-8)*self.A*((self.T1**4)-(self.T2**4)), self.q)
        self.solv, *_ = solve(ecuacion, Radiacion.incog)
        return f'El valor de {Radiacion.incog} es de {self.solv}'

# ----------------------------------------Radiacion formula 2---------------------------------------------

class Radiacion_formula_2:
    incog = 0

    def __init__(self, p, o, t):
        self.p = p
        self.o = o
        self.t = t

        if self.p == None:
            self.p = symbols('p')
            Radiacion_formula_2.incog = self.p
        elif self.o == None:
            self.o = symbols('o')
            Radiacion_formula_2.incog = self.o
        elif self.t == None:
            self.t = symbols('t')
            Radiacion_formula_2.incog = self.t

    def solucion(self, solv=None):

        ecuacion2 = Eq(self.p + self.o + self.t, 1)
        self.solv, *_ = solve(ecuacion2, Radiacion_formula_2.incog)
        return f'El valor de {Radiacion_formula_2.incog} es de {self.solv}'



# if __name__ == '__main__':
#     Radia_1 = Radiacion(q=None, A=5, T1=564, T2=515, E=1)
#     print(Radia_1.solucion())

# -----------------------------------------------------------Reynolds----------------------------------

class Reynolds:
    incog = 0

    def __init__(self, Re, densi, Um, d, U):
        self.Re = Re
        self.densidad = densi
        self.Um = Um
        self.d = d
        self.U = U
        if self.Re == None:
            self.Re = symbols('Re')
            Reynolds.incog = self.Re
        elif self.densidad == None:
            self.densidad = symbols('densidad')
            Reynolds.incog = self.densidad
        elif self.Um == None:
            self.Um = symbols('Um')
            Reynolds.incog = self.Um
        elif self.d == None:
            self.d = symbols('d')
            Reynolds.incog = self.d
        elif self.U == None:
            self.U = symbols('U')
            Reynolds.incog = self.U

    def solucion(self, solv=None):

        ecuacion = Eq(((self.densidad*self.Um*self.d)/self.U), self.Re)
        self.solv, *_ = solve(ecuacion, Reynolds.incog)
        return f'El valor de {Reynolds.incog} es de {self.solv}'



if __name__ == '__main__':
    Rey_1 = Reynolds(Re=None, densi=548, Um=5155, d=5456, U=2.57E-5)
    print(Rey_1.solucion())
    


    
# -----------------------------------------------------------Nusselt----------------------------------


# class Nusselt(Reynolds):
#     incog = 0

#     def __init__(self, Re, Um, d, U, h, k, Pr, n):
#         super().__init__(Re, Um, d, U)
#         self.h = h
#         self.k = k
#         self.Pr = Pr
#         self.n = n
#         if self.h == None:
#             self.h = symbols('h')
#             Nusselt.incog = self.h
#         elif self.k == None:
#             self.k = symbols('k')
#             Nusselt.incog = self.k
#         elif self.Pr == None:
#             self.Pr = symbols('Pr')
#             Nusselt.incog = self.Pr
#         elif self.n == None:
#             self.n = symbols('n')
#             Nusselt.incog = self.n

#     def NPr(self):
#         N_Pr = (0.023*(self.solv**0.8)*self.Pr**self.n)
#         return N_Pr

#     def Nh(self):
#         N_h = (self.h*self.d)/self.k
#         return N_h

#     def solucion_total(self):
#         ecuacion = Eq(self.NPr()-self.Nh(), 0)
#         self.solv = solve(ecuacion, Nusselt.incog)[0]
#         return f'El valor de {Nusselt.incog} es de {self.solv}'

#     @classmethod
#     def __repr__(cls):
#         return 'Ejemplo de uso:\n\tRey_1 = Reynolds(Um=10, d=0.0254, U=2.57E-5)\n\tRey_1.Densidad(P=2*1.0132E5, R=287, T=473)\n\tprint(Rey_1.solucion())'


# # if __name__ == '__main__':
# #     nuss_1 = Nusselt(Re=None, Um=10, d=0.0254, U=2.57E-5,
# #                      h=None, k=0.0386, Pr=0.681, n=0.4)
# #     # nuss_1 = Nusselt(Re=14753.0811949218, Um=10, d=0.0254, U=2.57E-5,
# #     #                  h=None, k=0.0386, Pr=0.681, n=0.4)
# #     nuss_1.Densidad(P=2*1.0132E5, R=287, T=473)
# #     print(nuss_1.solucion())

# #     nuss_1.NPr()
# #     nuss_1.Nh()
# #     print(nuss_1.solucion_total())
