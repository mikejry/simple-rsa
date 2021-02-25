import math
import random
from primes import Prime



class Keys:
    
    def __init__(self,p,q):
        
        p = Prime(p)
        q = Prime(q)
        self.prime1=p
        self.prime2=q
        self.n = 0
        self.e = 0
        self.d = 0
        self.h = 0


    def modul(self):
        
        return self.prime1 * self.prime2

    def func_euler(self):
        
        return (self.prime1 - 1) * (self.prime2 - 1)

    def look_for_e(self):
        
        self.n = self.modul()
        self.h = self.func_euler()
        number = random.randint(1, (self.n // 2))
        for j in range(number, self.n):
            if (j % 2 != 0) and (j > 1):
                a = self.h
                c = 0
                bufor_j = j
                if self.h < j:
                    a = j
                    j = self.h
                while j != 0:
                    c = a % j
                    a = j
                    j = c
                if a == 1:
                    self.e = bufor_j
                    return bufor_j
                else:
                    return self.look_for_e()

    def inverse_modulo(self):

       

        for d in range(1, self.h):
            r = (d * self.e) % self.h
            if r == 1:
                break
        else:
            raise ValueError('%dNie ma odwrotnosci mod %d' % (self.e, self.h))
        self.d = d
        return d

    def get_tab_keys(self):
       
        tab=[]
        tab.append(self.look_for_e())
        tab.append(self.inverse_modulo())
        tab.append(self.modul())
        return tab
