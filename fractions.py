class Fraction:
    def __init__(self, top, bottom):
        self.numerator = top
        self.denominator = bottom
    
    def __str__(self):
        # return f"{self.numerator}/{self.denominator}"
        return f"{self.numerator // self.denominator}" if self.numerator == 0 else f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        newnum = self.numerator*other.denominator + self.denominator*other.numerator
        newden = self.denominator * other.denominator
        return Fraction(newnum, newden).reduce()

    def __sub__(self, other):
        newnum = self.numerator*other.denominator - self.denominator*other.numerator
        newden = self.denominator * other.denominator
        return Fraction(newnum, newden).reduce()
    
    def __mul__(self, other):
        newnum = self.numerator * other.numerator
        newden = self.denominator * other.denominator
        return Fraction(newnum, newden).reduce()
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        newnum = self.numerator * other.denominator
        newden = self.denominator * other.numerator
        return Fraction(newnum, newden).reduce()
    
    def __eq__(self, other):
        firstnum = self.numerator * other.denominator
        secondnum = self.denominator * other.numerator
        return firstnum == secondnum

    def __lt__(self, other):
        firstnum = self.numerator * other.denominator
        secondnum = self.denominator * other.numerator
        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.numerator * other.denominator
        secondnum = self.denominator * other.numerator
        return firstnum > secondnum
    
    def gcd(self, m, n):
        while m % n != 0:
            old_m = m
            old_n = n

            m = old_n
            n = old_m % old_n
        return n
    
    def reduce(self):
        common_divisor = self.gcd(self.numerator, self.denominator)
        newnum = self.numerator // common_divisor
        newden = self.denominator // common_divisor
        return Fraction(newnum, newden)



# a = Fraction(3, 6)
# print(a + 1)
# b = a
# print('b == a :', b == a)

# c = Fraction(1, 2)
# print('c == a :', c == a)

# print(a.reduce())

# print(a - c)

# d = Fraction(12, 6)
# e = 7 * a
# print(e)

# print(a / e)

# f = Fraction(1, 2)
# g = Fraction(1, 5)
# print('1/2 > 1/5 : ', f > g)
# print('1/5 > 1/2 : ', g > f)

# print('1/2 < 1/5 : ', f < g)
# print('1/5 < 1/2 : ', g < f)

h = Fraction(8, 16)
print(h)

i = h.reduce()
print(i)
print(h)