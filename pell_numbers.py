class Pell(object):
    def get(self, n):
        counter = 2
        if n <= 2: return n
        a, b = 0, 1
        while counter <= n:
            new = 2 * b + a
            a = b
            b = new
            counter += 1
        return b
pell = Pell()
print(pell.get(3))