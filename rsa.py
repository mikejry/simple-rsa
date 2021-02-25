import math
import random
from primes import Prime
from keys import Keys


class Cipher:
    

    def __init__(self, p,q):
        
        self.key = Keys(p,q)
        self.tab =self.key.get_tab_keys()
        self.klucz_pub = self.tab[0]
        self.klucz_pryw = self.tab[1]
        self.n = self.tab[2]

    def encode(self, tekst):
        

        szyfr = [(ord(char) ** self.klucz_pub) % self.n for char in tekst]
        return szyfr

    def decode(self, zaszyfrowany):
        
        tekst = [chr((char ** self.klucz_pryw) % self.n) for char in zaszyfrowany]
        return ''.join(tekst)



