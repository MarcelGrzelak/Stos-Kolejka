class Wezel:
    def __init__(self, wartosc, next=None):
        self.wartosc = wartosc
        self.next = next


class Stos:
    def __init__(self):
        self.front = None

    def push(self, e):
        self.front = Wezel(e, self.front)

    def pop(self):
        if self.front is None:
            raise IndexError("stos jest pusty")
        w = self.front
        self.front = w.next
        return w.wartosc

    def top(self):
        if self.front is None:
            raise IndexError("stos jest pusty")
        return self.front.wartosc

    def pusty(self):
        return self.front is None


class Kolejka:
    def __init__(self):
        self.front = None
        self.back = None

    def inject(self, e):
        w = Wezel(e)
        if self.back is None:
            self.front = w
        else:
            self.back.next = w
        self.back = w

    def out(self):
        if self.front is None:
            raise IndexError("kolejka jest pusta")
        w = self.front
        self.front = w.next
        if self.front is None:
            self.back = None
        return w.wartosc

    def top(self):
        if self.front is None:
            raise IndexError("kolejka jest pusta")
        return self.front.wartosc

    def pusta(self):
        return self.front is None


# test stosu
s = Stos()
for litera in "abc":
    s.push(litera)

print(s.pop())
print(s.top())
print(s.pop())
s.push("x")
print(s.pop())
print(s.pop())
print(s.pusty())

# test kolejki
k = Kolejka()
for n in [10, 20, 30]:
    k.inject(n)

print(k.out())
k.inject(40)
print(k.top())
print(k.out())
print(k.out())
print(k.out())
print(k.pusta())