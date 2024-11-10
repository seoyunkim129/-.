class Vector:
    def __init__(self, *args):
        self.v = tuple(float(x) for x in args)

    def __add__(self, other):
        if len(self.v) != len(other.v):
            return "벡터의 크기가 서로 달라 + 연산이 불가능"
        return Vector(*[self.v[i] + other.v[i] for i in range(len(self.v))])

    def __sub__(self, other):
        if len(self.v) != len(other.v):
            return "벡터의 크기가 서로 달라 - 연산이 불가능"
        return Vector(*[self.v[i] - other.v[i] for i in range(len(self.v))])

    def __mul__(self, other):
        if len(self.v) != len(other.v):
            return "벡터의 크기가 서로 달라 * 연산이 불가능"
        return sum(self.v[i] * other.v[i] for i in range(len(self.v)))

    def distance(self, other):
        if len(self.v) != len(other.v):
            return "벡터의 크기가 서로 달라 거리 연산이 불가능"
        return sum((self.v[i] - other.v[i]) ** 2 for i in range(len(self.v))) ** 0.5

    def norm(self):
        return sum(a ** 2 for a in self.v) ** 0.5

    def __str__(self):
        return str(self.v)


# Test the Vector class with the given examples
u1 = Vector(1, 2, 3, 4)
u2 = Vector(-1, 0, 1, 0)
u3 = Vector(1, 0, 1)
u4 = Vector(-1, 0, 1)

# Perform the required operations and print results
print("u1 + u2:", u1 + u2)
print("u1 + u3:", u1 + u3)
print("u3 - u4:", u3 - u4)
print("u1 * u2:", u1 * u2)
print("u1 * u3:", u1 * u3)
print("u1 and u2 distance:", u1.distance(u2))
print("u3 and u4 distance:", u3.distance(u4))
print("u1 norm:", u1.norm())
print("u2 norm:", u2.norm())
print("u3 norm:", u3.norm())
print("u4 norm:", u4.norm())

