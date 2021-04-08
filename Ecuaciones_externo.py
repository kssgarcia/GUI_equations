from sympy import symbols, Eq, solve, log


class Nusselt1_ext():
    incog = 0

    def __init__(self, h, d, k, C, U, Uf, n, Pr):
        self.h = h
        self.d = d
        self.k = k
        self.C = C
        self.U = U
        self.Uf = Uf
        self.n = n
        self.Pr =Pr
        if self.h == None:
            self.h = symbols('h')
            Nusselt1_ext.incog = self.h
        elif self.d == None:
            self.d = symbols('d')
            Nusselt1_ext.incog = self.d
        elif self.k == None:
            self.k = symbols('k')
            Nusselt1_ext.incog = self.k
        elif self.C == None:
            self.C = symbols('C')
            Nusselt1_ext.incog = self.C
        elif self.U == None:
            self.U = symbols('U')
            Nusselt1_ext.incog = self.U
        elif self.Uf == None:
            self.Uf = symbols('Uf')
            Nusselt1_ext.incog = self.Uf
        elif self.n == None:
            self.n = symbols('n')
            Nusselt1_ext.incog = self.n
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt1_ext.incog = self.Pr

    def lado_izq(self):
        N_Pr = (self.h*self.d)/self.k
        return N_Pr

    def lado_der(self):
        N_P = self.C*(((self.U*self.d)/self.Uf)**self.n)*self.Pr**0.3333
        return N_P

    def solucion_total(self):
        ecuacion = Eq(self.lado_izq(), self.lado_der())
        self.solv, *_ = solve(ecuacion, Nusselt1_ext.incog)
        return f'El valor de {Nusselt1_ext.incog} es de {self.solv}'

class Nusselt2_ext():
    incog = 0

    def __init__(self, nuss, Re, Pr):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt2_ext.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt2_ext.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt2_ext.incog = self.Pr

    def NPr(self):
        N_Pr = (0.35 + 0.56*self.Re**0.52)*self.Pr*0.3
        return N_Pr

    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt2_ext.incog)
        return f'El valor de {Nusselt2_ext.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()

class Nusselt3_ext():
    incog = 0

    def __init__(self, Re, nuss, Pr, Prf, Prw):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        self.Prf = Prf
        self.Prw = Prw
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt3_ext.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt3_ext.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt3_ext.incog = self.Pr
        elif self.Prf == None:
            self.Prf = symbols('Prf')
            Nusselt3_ext.incog = self.Prf
        elif self.Prw == None:
            self.Prw = symbols('Prw')
            Nusselt3_ext.incog = self.Prw

    def NPr(self):
        N_Pr = (0.43 + 0.50*self.Re**0.50)*(self.Pr*0.38)*(self.Prf/self.Prw)**0.25
        return N_Pr

    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt3_ext.incog)
        return f'El valor de {Nusselt3_ext.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()

class Nusselt4_ext():
    incog = 0

    def __init__(self, Re, nuss, Pr, Prf, Prw):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        self.Prf = Prf
        self.Prw = Prw
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt4_ext.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt4_ext.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt4_ext.incog = self.Pr
        elif self.Prf == None:
            self.Prf = symbols('Prf')
            Nusselt4_ext.incog = self.Prf
        elif self.Prw == None:
            self.Prw = symbols('Prw')
            Nusselt4_ext.incog = self.Prw

    def NPr(self):
        N_Pr = (0.25*self.Re**0.60)*(self.Pr*0.38)*(self.Prf/self.Prw)**0.25
        return N_Pr

    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt4_ext.incog)
        return f'El valor de {Nusselt4_ext.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()

class Nusselt5_ext():
    incog = 0

    def __init__(self, nuss, Re, Pr):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt5_ext.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt5_ext.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt5_ext.incog = self.Pr

    def NPr(self):
        N_Pr = 0.3 + (((0.62*pow(self.Re,0.5)*pow(self.Pr,0.333))/((1+(0.4/self.Pr)**0.6667))**0.75))
        a = N_Pr * (1 + (self.Re/282000)**0.625)**0.8
        return a

    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt5_ext.incog)
        return f'El valor de {Nusselt5_ext.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()

class Nusselt6_ext():
    incog = 0

    def __init__(self, nuss, Re, Pr):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt6_ext.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt6_ext.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt6_ext.incog = self.Pr

    def NPr(self):
        N_Pr = 0.3 + (((0.62*pow(self.Re,0.5)*pow(self.Pr,0.333))/((1+(0.4/self.Pr)**0.6667))**0.75))
        a = N_Pr * (1 + (self.Re/282000)**0.5)
        return a


    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt6_ext.incog)
        return f'El valor de {Nusselt6_ext.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()

class Nusselt7_ext():
    incog = 0

    def __init__(self, nuss, Ped):
        self.nuss = nuss
        self.Ped = Ped
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt7_ext.incog = self.nuss
        elif self.Ped == None:
            self.Ped = symbols('Ped')
            Nusselt7_ext.incog = self.Ped

    def NPr(self):
        N_Pr = (0.8237 - log(self.Ped**0.5))**-1
        return N_Pr


    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt7_ext.incog)
        return f'El valor de {Nusselt7_ext.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()

class bancos():
    incog = 0

    def __init__(self, Re, nuss, Pr, Prs, C, m, n):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        self.Prs = Prs
        self.C = C
        self.m = m
        self.n = n
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt3_ext.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt3_ext.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt3_ext.incog = self.Pr
        elif self.Prs == None:
            self.Prs = symbols('Prs')
            Nusselt3_ext.incog = self.Prs
        elif self.C == None:
            self.C = symbols('C')
            Nusselt3_ext.incog = self.C
        elif self.m == None:
            self.m = symbols('m')
            Nusselt3_ext.incog = self.m
        elif self.n == None:
            self.n = symbols('n')
            Nusselt3_ext.incog = self.n

    def NPr(self):
        N_Pr = (self.C*self.Re**self.m)*(self.Pr*self.n)*(self.Pr/self.Prs)**0.25
        return N_Pr

    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt3_ext.incog)
        return f'El valor de {Nusselt3_ext.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()