class Vector:
    def __init__(self, *args):
        self.v = tuple(float(x) for x in args)

    def __add__(self, other):
        if len(self.v) != len(other.v):
            raise ValueError("벡터의 크기가 서로 달라 + 연산이 불가능")
        return Vector(*[self.v[i] + other.v[i] for i in range(len(self.v))])

    def __sub__(self, other):
        if len(self.v) != len(other.v):
            raise ValueError("벡터의 크기가 서로 달라 - 연산이 불가능")
        return Vector(*[self.v[i] - other.v[i] for i in range(len(self.v))])

    def __mul__(self, other):
        if len(self.v) != len(other.v):
            raise ValueError("벡터의 크기가 서로 달라 * 연산이 불가능")
        return sum(self.v[i] * other.v[i] for i in range(len(self.v)))

    def distance(self, other):
        if len(self.v) != len(other.v):
            raise ValueError("벡터의 크기가 서로 달라 거리 연산이 불가능")
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


# Define functions for operations
def add_u1_u2():
    return u1 + u2


def add_u1_u3():
    return u1 + u3


def sub_u3_u4():
    return u3 - u4


def mul_u1_u2():
    return u1 * u2


def mul_u1_u3():
    return u1 * u3


def dist_u1_u2():
    return u1.distance(u2)


def dist_u3_u4():
    return u3.distance(u4)


def norm_u1():
    return u1.norm()


def norm_u2():
    return u2.norm()


def norm_u3():
    return u3.norm()


def norm_u4():
    return u4.norm()


# List of operations to perform
operations = [
    ("u1 + u2", add_u1_u2),
    ("u1 + u3", add_u1_u3),
    ("u3 - u4", sub_u3_u4),
    ("u1 * u2", mul_u1_u2),
    ("u1 * u3", mul_u1_u3),
    ("u1 and u2 distance", dist_u1_u2),
    ("u3 and u4 distance", dist_u3_u4),
    ("u1 norm", norm_u1),
    ("u2 norm", norm_u2),
    ("u3 norm", norm_u3),
    ("u4 norm", norm_u4)
]

# Execute and print results with exception handling
for description, operation in operations:
    try:
        result = operation()
        print(f"{description}: {result}")
    except ValueError as e:
        print(f"{description}: {e}")


