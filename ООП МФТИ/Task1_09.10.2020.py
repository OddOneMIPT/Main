class Complex:
    def __init__(self, re, im):
        try:
            self.__re = float(re)
            self.__im = float(im)
        except ValueError:
            print('Введите правильные значения, сначала реальную часть, потом мнимую')

    def __add__ (self, other):
        try:
            re = self.__re + other.__re
            im = self.__im + other.__im
            return Complex(re, im)
        except Exception:
            re = self.__re + other
            return Complex(re, self.__im)
    
    
    def __radd__(self, other):
        try:
            re = self.__re + other.__re
            im = self.__im + other.__im
            return Complex(re, im)
        except Exception:
            re = self.__re + other
            return Complex(re, self.__im)

    def __sub__(self, other):
        try:
            re = self.__re - other.__re
            im = self.__im - other.__im
            return Complex(re, im)
        except Exception:
            re = self.__re - other
            return Complex(re, self.__im)


    def __rsub__(self, other):
        try:
            re = self.__re - other.__re
            im = self.__im - other.__im
            return Complex(re, im)
        except Exception:
            re = self.__re - other
            return Complex(re, self.__im)


    def __mul__(self, other):
        try:
            re = (self.__re*other.__re - self.__im*other.__im)
            im = (self.__re*other.__im + self.__im*other.__re)
            return Complex(re, im)
        except Exception:
            re = self.__re * other
            im = self.__im * other
            return Complex(re, im)
    
    def __rmul__(self, other):
        try:
            re = (self.__re*other.__re - self.__im*other.__im)
            im = (self.__re*other.__im + self.__im*other.__re)
            return Complex(re, im)
        except Exception:
            re = self.__re * other
            im = self.__im * other
            return Complex(re, im)

    def __truediv__(self, other):
        try:
            chisl = self * Complex(other.__re, -other.__im)
            znam = other * Complex(other.__re, -other.__im)
            return Complex(chisl.__re/znam.__re, chisl.__im/znam.__re)
        except Exception:
            return Complex(self.__re/other, self.__im/other)


    def __rtruediv__(self, other):
        try:
            chisl = self * Complex(other.__re, -other.__im)
            znam = other * Complex(other.__re, -other.__im)
            return Complex(chisl.__re/znam.__re, chisl.__im/znam.__re)
        except Exception:
            return Complex(self.__re/other, self.__im/other)
            

    def __abs__(self):
        return (self.__re**2 + self.__im**2)**0.5
    
    def __str__(self):
        return '{} + i*({})'.format(self.__re,self.__im)


    def __repr__(self):
        return 'Complex({}, {})'.format(self.__re,self.__im)
 

x = Complex(3,4)
y = Complex(2,-1)
z = abs(x)
print(z)
