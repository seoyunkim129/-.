from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

    def __str__(self):
        return f"도형 종류: {self.__class__.__name__}"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self):
        return self._width * self._height

    def volume(self):
        return 0

    def __str__(self):
        return super().__str__() + f" (가로: {self.width:.1f}, 세로: {self.height:.1f})"


class Box(Rectangle):
    def __init__(self, width, height, depth):
        super().__init__(width, height)
        self._depth = depth

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value

    def area(self):
        return 2 * (self._width * self._height + self._width * self._depth + self._height * self._depth)

    def volume(self):
        return self._width * self._height * self._depth

    def __str__(self):
        return super().__str__() + f", 높이: {self.depth:.1f}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    def area(self):
        return math.pi * self._radius ** 2

    def volume(self):
        return 0

    def __str__(self):
        return super().__str__() + f" (반지름: {self.radius:.1f})"


class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self):
        return 2 * math.pi * self._radius * (self._radius + self._height)

    def volume(self):
        return math.pi * self._radius ** 2 * self._height

    def __str__(self):
        return super().__str__() + f", 높이: {self.height:.1f}"


class Sphere(Shape):
    def __init__(self, radius):
        super().__init__("Sphere")
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    def area(self):
        return 4 * math.pi * self._radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self._radius ** 3

    def __str__(self):
        return super().__str__() + f" (반지름: {self.radius:.1f})"


# 문제 2
rectangle = Rectangle(10, 5)
print(rectangle)
print(f"면적: {rectangle.area():.3f}, 체적: {rectangle.volume():.3f}")

# 문제 3
box = Box(10, 5, 30)
print(box)
print(f"겉넓이: {box.area():.3f}, 체적: {box.volume():.3f}")

# 문제 4
circle = Circle(20)
print(circle)
print(f"면적: {circle.area():.3f}, 체적: {circle.volume():.3f}")

# 문제 5
cylinder = Cylinder(20, 50)
print(cylinder)
print(f"겉면적: {cylinder.area():.3f}, 체적: {cylinder.volume():.3f}")

# 문제 6
sphere = Sphere(20)
print(sphere)
print(f"겉면적: {sphere.area():.3f}, 체적: {sphere.volume():.3f}")
