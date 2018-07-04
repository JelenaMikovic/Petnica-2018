import math as m

class generator:
    def __init__(self):
        self.n = 2

    def getNum(self):
        return self.n

    def isPrime(self):
        i = 2
        ok = True

        while i <= m.sqrt(self.n) and ok:
            if self.n % i == 0:
                ok = False
            i += 1

        return ok

    def next(self):
        self.n += 1

        while not self.isPrime():
            self.n += 1
        return self

x = generator()

print(x.getNum())

print(x.next().getNum())
print(x.next().getNum())