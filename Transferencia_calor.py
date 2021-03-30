from sympy import symbols, Eq, solve
# -----------------------------------------------------------Reynolds----------------------------------


class Muros:
    Q = 0
    T1 = 0
    T2 = 1
    conduccion = 0
    convec = 0
    incog = 0

    def __init__(self, L, k, A):
        self.L = L
        self.k = k
        self.A = A
        if Muros.Q == None:
            Muros.Q = symbols('Q')
            Muros.incog = Muros.Q
        if self.L == None:
            self.L = symbols('L')
            Muros.incog = self.L
        elif self.k == None:
            self.k = symbols('k')
            Muros.incog = self.k
        elif self.A == None:
            self.A = symbols('A')
            Muros.incog = self.A
        Muros.conduccion += (self.L) / (self.k*self.A)

    @classmethod
    def conveccion(cls, h, Ac):
        cls.h = h
        cls.Ac = Ac
        if cls.h == None:
            cls.h = symbols('h')
            Muros.incog = cls.h
        elif cls.Ac == None:
            cls.Ac = symbols('Ac')
            Muros.incog = cls.Ac
        cls.convec += 1 / (cls.h*cls.Ac)
        return cls.convec

    def Solucion(self):
        ecuacion = Eq((Muros.T1 - Muros.T2) /
                      (Muros.conduccion + Muros.convec)-Muros.Q, 0)
        return (Muros.incog, solve(ecuacion, Muros.incog)[0])

    @classmethod
    def __repr__(cls):
        return 'Ejemplo de uso:\n\tMuros.Q = 15500\n\tMuros.T1 = 25\n\tMuros.T2 = 50\n\tMuros.conveccion(h=1000, Ac=None)\n\tmuro_1 = Muros(L=50/1000, k=1, A=1)\n\tmuro_2 = Muros(L=50/1000, k=1, A=0.5)\n\tmuro_3 = Muros(L=50/1000, k=1, A=0.01)\n\tMuros.conveccion(h=500, Ac=1)\n\tprint(muro_3.Solucion())'


if __name__ == '__main__':
    Muros.Q = 15500
    Muros.T1 = 25
    Muros.T2 = 50
    Muros.conveccion(h=1000, Ac=None)
    muro_1 = Muros(L=50/1000, k=1, A=1)
    # muro_2 = Muros(L=50/1000, k=1, A=0.5)
    # muro_3 = Muros(L=50/1000, k=1, A=0.01)
    # Muros.conveccion(h=500, Ac=1)
    print(muro_1.Solucion())
# -----------------------------------------------------------Reynolds----------------------------------


class Reynolds:
    incog = 0

    def __init__(self, Re, Um, d, U):
        self.Re = Re
        self.Um = Um
        self.d = d
        self.U = U
        if self.Re == None:
            self.Re = symbols('Re')
            Reynolds.incog = self.Re
        elif self.Um == None:
            self.Um = symbols('Um')
            Reynolds.incog = self.Um
        elif self.d == None:
            self.d = symbols('d')
            Reynolds.incog = self.d
        elif self.U == None:
            self.U = symbols('U')
            Reynolds.incog = self.U

    def Densidad(self, P, R, T):
        if type(self.Re) == type(symbols('x')):
            self.P = P
            self.R = R
            self.T = T
            if self.P == None:
                self.P = symbols('P')
                Reynolds.incog = self.P
            elif self.R == None:
                self.R = symbols('R')
                Reynolds.incog = self.R
            self.densidad = P/(R*T)
            return self.densidad

    def solucion(self, solv=None):
        if type(self.Re) == type(symbols('x')):
            ecuacion = Eq(((self.densidad*self.Um*self.d)/self.U)-self.Re, 0)
            self.solv = solve(ecuacion, Reynolds.incog)[0]
            return f'El valor de {Reynolds.incog} es de {self.solv}'
        else:
            self.solv = self.Re
            return f'El valor de Re es de {self.solv}'

    @classmethod
    def __repr__(cls):
        return 'Ejemplo de uso:\n\tRey_1 = Reynolds(Um=10, d=0.0254, U=2.57E-5)\n\tRey_1.Densidad(P=2*1.0132E5, R=287, T=473)\n\tprint(Rey_1.solucion())'


# if __name__ == '__main__':
#     Rey_1 = Reynolds(Re=None, Um=10, d=0.0254, U=2.57E-5)
#     Rey_1.Densidad(P=2*1.0132E5, R=287, T=473)
#     Rey_1.solucion()
#     print(Rey_1.solucion())
# -----------------------------------------------------------Nusselt----------------------------------


class Nusselt(Reynolds):
    incog = 0

    def __init__(self, Re, Um, d, U, h, k, Pr, n):
        super().__init__(Re, Um, d, U)
        self.h = h
        self.k = k
        self.Pr = Pr
        self.n = n
        if self.h == None:
            self.h = symbols('h')
            Nusselt.incog = self.h
        elif self.k == None:
            self.k = symbols('k')
            Nusselt.incog = self.k
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt.incog = self.Pr
        elif self.n == None:
            self.n = symbols('n')
            Nusselt.incog = self.n

    def NPr(self):
        N_Pr = (0.023*(self.solv**0.8)*self.Pr**self.n)
        return N_Pr

    def Nh(self):
        N_h = (self.h*self.d)/self.k
        return N_h

    def solucion_total(self):
        ecuacion = Eq(self.NPr()-self.Nh(), 0)
        self.solv = solve(ecuacion, Nusselt.incog)[0]
        return f'El valor de {Nusselt.incog} es de {self.solv}'

    @classmethod
    def __repr__(cls):
        return 'Ejemplo de uso:\n\tRey_1 = Reynolds(Um=10, d=0.0254, U=2.57E-5)\n\tRey_1.Densidad(P=2*1.0132E5, R=287, T=473)\n\tprint(Rey_1.solucion())'


# if __name__ == '__main__':
#     nuss_1 = Nusselt(Re=None, Um=10, d=0.0254, U=2.57E-5,
#                      h=None, k=0.0386, Pr=0.681, n=0.4)
#     # nuss_1 = Nusselt(Re=14753.0811949218, Um=10, d=0.0254, U=2.57E-5,
#     #                  h=None, k=0.0386, Pr=0.681, n=0.4)
#     nuss_1.Densidad(P=2*1.0132E5, R=287, T=473)
#     print(nuss_1.solucion())

#     nuss_1.NPr()
#     nuss_1.Nh()
#     print(nuss_1.solucion_total())
