from sympy import symbols, Eq, solve
# ----------------------------------- masa y momento particulas-----------------------------------------
class masam_particulas:
    incog = 0

    def __init__(self, m, fr):
        self.m = m
        self.fr = fr
        if self.m == None:
            self.m = symbols('m')
            masam_particulas.incog = self.m
        elif self.fr == None:
            self.fr = symbols('fr')
            masam_particulas.incog = self.fr    

    def solucion(self, solv=None):
        cosntante_planck = 6.625e-34 #[J.s]
        ecuacion_mam = Eq(self.m, (cosntante_planck* self.fr)/(3e8**2))
        self.solv, *_ = solve(ecuacion_mam, masam_particulas.incog)
        if masam_particulas.incog == self.fr:
            momento_p = (cosntante_planck*self.solv)/3e8
        else:
            momento_p = (cosntante_planck*self.fr)/3e8
        return f'El valor de {masam_particulas.incog} es de {self.solv} y el momento es de {momento_p}'

# ---------------------------------------------Energia cuantos discretos---------------------------------
class Energia_cuantos_discretos:
    incog = 0

    def __init__(self, E, fr):
        self.E = E
        self.fr = fr
        if self.E == None:
            self.E = symbols('E')
            Energia_cuantos_discretos.incog = self.E
        elif self.fr == None:
            self.fr = symbols('fr')
            Energia_cuantos_discretos.incog = self.fr

    def solucion(self, solv=None):
        cosntante_planck = 6.625e-34 #[J.s]
        ecuacion_cuantos = Eq(self.E,cosntante_planck* self.fr)
        self.solv, *_ = solve(ecuacion_cuantos, Energia_cuantos_discretos.incog)
        return f'El valor de {Energia_cuantos_discretos.incog} es de {self.solv}'
    
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

# ----------------------------------------Radiacion formula 2_cuerpo negro---------------------------------------------

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
#-----------------------------------------Radiacion_formula_luz----------------------------------------
class Radiacion_formula_luz:
    incog = 0

    def __init__(self, lamb, v):
        self.lamb = lamb
        self.v = v

        if self.lamb == None:
            self.lamb = symbols('lamb')
            Radiacion_formula_luz.incog = self.lamb
        elif self.v == None:
            self.v = symbols('v')
            Radiacion_formula_luz.incog = self.v

    def solucion(self, solv=None):

        ecuacionluz = Eq(self.lamb * self.v, 3e10)
        self.solv, *_ = solve(ecuacionluz, Radiacion_formula_luz.incog)
        return f'El valor de {Radiacion_formula_luz.incog} es de {self.solv}'



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


class Nusselt1():
    incog = 0

    def __init__(self, nuss, Re, Pr, n):
        self.nuss = nuss
        self.Re = Re
        self.Pr = Pr
        self.n = n
        if self.nuss == None:
            self.nuss = symbols('nuss')
            Nusselt1.incog = self.nuss
        elif self.Re == None:
            self.Re = symbols('Re')
            Nusselt1.incog = self.Re
        elif self.Pr == None:
            self.Pr = symbols('Pr')
            Nusselt1.incog = self.Pr
        elif self.n == None:
            self.n = symbols('n')
            Nusselt1.incog = self.n

    def NPr(self):
        N_Pr = (0.023*(self.Re**0.8)*self.Pr**self.n)
        return N_Pr

    def solucion_total(self):
        ecuacion = Eq(self.NPr(), self.nuss)
        self.solv, *_ = solve(ecuacion, Nusselt1.incog)
        return f'El valor de {Nusselt1.incog} es de {self.solv}'

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

class fuerza_arrast():
    incog = 0

    def __init__(self, Fd, Cd, A, densi, U, g):
        self.Fd = Fd
        self.Cd  =Cd
        self.A = A
        self.densi = densi
        self.U = U
        self.g = g
        if self.Fd == None:
            self.Fd = symbols('Fd')
            fuerza_arrast.incog = self.Fd
        elif self.Cd == None:
            self.Cd = symbols('Cd')
            fuerza_arrast.incog = self.Cd
        elif self.A == None:
            self.A = symbols('A')
            fuerza_arrast.incog = self.A
        elif self.densi == None:
            self.densi = symbols('densi')
            fuerza_arrast.incog = self.densi
        elif self.U == None:
            self.U = symbols('U')
            fuerza_arrast.incog = self.U
        elif self.g == None:
            self.g = symbols('g')
            fuerza_arrast.incog = self.g

    def lado_izq(self):
        izq = self.Cd*self.A*((self.densi*pow(self.U,2))/(2*self.g))
        return izq

    def solucion_total(self):
        ecuacion = Eq(self.lado_izq(), self.Fd)
        self.solv, *r = solve(ecuacion, fuerza_arrast.incog)
        return f'El valor de {fuerza_arrast.incog} es de {self.solv}'

    def __str__(self):
        return self.solucion_total()


if __name__ == '__main__':
    nuss_1 = fuerza_arrast(Fd=87, Cd=87, A=97, densi=87, U=None, g=421)
    print(nuss_1)
