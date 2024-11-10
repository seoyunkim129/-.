class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def __str__(self):
        return f"({self._x}, {self._y})"


class Rectangle:
    def __init__(self, base_point=Point(), width=0, height=0, color=""):
        self._base_point = base_point
        self._width = width
        self._height = height
        self._color = color

    @property
    def base_point(self):
        return self._base_point

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def color(self):
        return self._color

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    def draw(self):
        print("직사각형을 그려라")

    def move(self, new_base_point):
        self._base_point = new_base_point

    def __str__(self):
        return f"기준점(좌측 하단) : {self._base_point} 가로 : {self._width} 세로 : {self._height} 면적 : {self.area} 둘레 : {self.perimeter}"

# 테스트
if __name__ == "__main__":
    base_point = Point(-50, 100)
    rectangle = Rectangle(base_point, 50, 25, "red")
    print(rectangle)