def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


def get_sign(n):
    if n >= 0:
        return 1
    elif n < 0:
        return -1


class Fraction:
    def __init__(self, top, bottom):
        if isinstance(top, int) and isinstance(bottom, int) == False:
            raise ValueError(f'{top} or {bottom} must be integers!')
        if bottom < 0:
            bottom = abs(bottom)
            # if top is already negative then keep it otherwise flip top's signage
            top = top * get_sign(top) * -1
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + \
            self.den*otherfraction.num
        newden = self.den * otherfraction.den
        #common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        newnum = self.getNum() * otherfraction.getDen() - \
            otherfraction.getNum() * self.getDen()
        newden = self.getDen() * otherfraction.getDen()
        return Fraction(newnum, newden)

    def __mul__(self, otherfraction):
        newnum = self.getNum() * otherfraction.getNum()
        newden = self.getDen() * otherfraction.getDen()
        return Fraction(newnum, newden)

    def __truediv__(self, otherfraction):
        # TODO: This doesn't work properly for negative fractions
        newnum = self.getNum() * otherfraction.getDen()
        newden = self.getDen() * otherfraction.getNum()
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __crossmul__(self, other):
        firstnum = self.getNum() * other.getDen()
        secondnum = other.getNum() * self.getDen()
        return firstnum, secondnum

    def __gt__(self, other):
        firstnum, secondnum = self.__crossmul__(other)
        return firstnum > secondnum

    def __ge__(self, other):
        firstnum, secondnum = self.__crossmul__(other)
        return firstnum >= secondnum

    def __lt__(self, other):
        firstnum, secondnum = self.__crossmul__(other)
        return firstnum < secondnum

    def __le__(self, other):
        firstnum, secondnum = self.__crossmul__(other)
        return firstnum <= secondnum

    def __ne__(self, other):
        return not(self.__eq__(other))


myfraction = Fraction(3, 5)
f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
f4 = f2 - f1
f5 = Fraction(8, 3)
f6 = Fraction(-1, -3)
f7 = f5 / f6
f8 = f5.__truediv__(f6)
#f9 = Fraction(1, "b")
f10 = Fraction(-1, -3)

print(myfraction)
print(f3)
print(f3 == f1)
print(f3 == Fraction(3, 4))
print(f'{f2} - {f1} = {f4}')
print(f'{f4} consists of {f4.getNum()} and {f4.getDen()}')
print(f'f5: {f5}, f6: {f6} and f6 consists of {f6.getNum()} and {f6.getDen()}')
print(f'f7: {f7}, f8: {f8}, same: {f7 == f8}')
print(f'f7: {f7}, f8: {f8}, check NotEqual: {f7.__ne__(f8)}')
print(f'f7: {f7}, f8: {f8}, check NotEqual: {f7 != f8}')
print(f'Is {f6} greater or equal to {f1}? {f6 >= f1}')
print(f'Is {f6} less or equal to {f1}? {f6 <= f1}')
print(f'{f10}')
