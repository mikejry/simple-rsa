import math

class Prime:
    

    def __init__(self, number):
        
        try:
            if self.is_prime(number) is False:
                self.primeNumber = 2
            else:
                self.primeNumber = int(number)
        except ValueError:
            print("Invalid number")
            self.primeNumber = 2

    def __mul__(self, other):
        
        multiply = self.primeNumber*other.primeNumber
        return multiply

    def __sub__(self, other):
        substitute = self.primeNumber-other
        return substitute

    def enter_prime(self):
        
        pierwsza = input("Podaj liczbę pierwszą:")

        try:
            pierwsza = int(pierwsza)
        except ValueError:
            print("Invalid number")
        return pierwsza

    def is_prime(self,num):
        
        num = int(num)
        if (num < 2):
            return False

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def enter_authenticated(self, num):
        
        while self.is_prime(num) == False:
            num = self.enter_prime()
        return num
