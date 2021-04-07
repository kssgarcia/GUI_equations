from sympy import symbols, Eq, solve


class Nusselt1_ext():
    incog = 0

    def __init__(self, nuss, Re, Pr, n):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        self.n = n
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt1_ext.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt1_ext.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt1_ext.incog = self.Pr
        elif self.n == None:
            self.n = symbols('n')
            Nusselt1_ext.incog = self.n

    def NPr(self):
        N_Pr = (0.023*(self.Re**0.8)*self.Pr**self.n)
        return N_Pr

    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt1_ext.incog)
        return f'El valor de {Nusselt1_ext.incog} es de {self.solv}'

class Nusselt2():
    incog = 0

    def __init__(self, nuss, Re, Pr, U, Um):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        self.U = U
        self.Um = Um
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt2.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt2.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt2.incog = self.Pr
        elif self.U == None:
            self.U = symbols('U')
            Nusselt2.incog = self.U
        elif self.Um == None:
            self.Um = symbols('Um')
            Nusselt2.incog = self.Um

    def NPr(self):
        N_Pr = (0.027*(self.Re**0.8)*self.Pr**0.33)*((self.U/self.Um)**0.14)
        return N_Pr

    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt2.incog)
        return f'El valor de {Nusselt2.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()

class Nusselt3():
    incog = 0

    def __init__(self, Re, nuss, Pr, d, L):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        self.d = d
        self.L = L
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt3.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt3.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt3.incog = self.Pr
        elif self.d == None:
            self.d = symbols('d')
            Nusselt3.incog = self.d
        elif self.L == None:
            self.L = symbols('L')
            Nusselt3.incog = self.L

    def NPr(self):
        N_Pr = (0.036*(self.Re**0.8)*self.Pr**0.333)*((self.d/self.L)**0.055)
        return N_Pr

    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt3.incog)
        return f'El valor de {Nusselt3.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()

class Nusselt4():
    incog = 0

    def __init__(self, nuss, Re, Pr, Ub, Uw, n, f):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        self.Ub = Ub
        self.Uw = Uw
        self.n = n
        self.f = f
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt4.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt4.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt4.incog = self.Pr
        elif self.Ub == None:
            self.Ub = symbols('Ub')
            Nusselt4.incog = self.Ub
        elif self.Uw == None:
            self.Uw = symbols('Uw')
            Nusselt4.incog = self.Uw
        elif self.n == None:
            self.n = symbols('n')
            Nusselt4.incog = self.n
        elif self.f == None:
            self.f = symbols('f')
            Nusselt4.incog = self.f

    def NPr(self):
        g = (self.f/8)
        N_Pr = ((g*self.Re*self.Pr)/(1.07+12.7*pow(g,0.5)*(pow(self.Pr,0.667)-1)))*(self.Ub/self.Uw)**self.n
        return N_Pr

    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt4.incog)
        return f'El valor de {Nusselt4.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()

class Nusselt5():
    incog = 0

    def __init__(self, nuss, Re, Pr, d, L):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        self.d = d
        self.L = L
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt5.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt5.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt5.incog = self.Pr
        elif self.d == None:
            self.d = symbols('d')
            Nusselt5.incog = self.d
        elif self.L == None:
            self.L = symbols('L')
            Nusselt5.incog = self.L

    def NPr(self):
        g = (self.d/self.L)
        N_Pr = 3.66 + ((0.0668*g*self.Re*self.Pr)/(1+0.04*(g*self.Re*self.Pr)**0.667))
        return N_Pr

    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt5.incog)
        return f'El valor de {Nusselt5.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()

class Nusselt6():
    incog = 0

    def __init__(self, nuss, Re, Pr, d, L, U, Um):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        self.U = U
        self.Um = Um
        self.d = d
        self.L =L
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt6.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt6.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt6.incog = self.Pr
        elif self.U == None:
            self.U = symbols('U')
            Nusselt6.incog = self.U
        elif self.Um == None:
            self.Um = symbols('Um')
            Nusselt6.incog = self.Um
        elif self.d == None:
            self.d = symbols('d')
            Nusselt6.incog = self.d
        elif self.L == None:
            self.L = symbols('L')
            Nusselt6.incog = self.L

    def NPr(self):
        N_Pr = (1.86*((self.Re*self.Pr)**0.333))*((self.d/self.L)**0.33)*((self.U/self.Um)**0.14)
        return N_Pr

    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt6.incog)
        return f'El valor de {Nusselt6.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()