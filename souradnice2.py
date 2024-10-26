class Point:

    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_point(self):
        return [self.x, self.y]

    def set_point(self, coords):
        self.x = coords[0]
        self.y = coords[1]

class Line:

    def __init__(self, coordsA, coordsB):
        self.A = Point(coordsA)
        self.B = Point(coordsB)
        self.len = self.set_len()

    def set_len(self):
        x_len = abs(self.A.get_x() - self.B.get_x())
        y_len = abs(self.A.get_y() - self.B.get_y())
        return (x_len ** 2 + y_len ** 2) ** 0.5

    def get_len(self):
        return self.len        

class Circle:
    pi = 3.14159265358979

    def __init__(self, midPoint, circlePoint):
        self.SX = Line(midPoint, circlePoint)
        self.o = self.set_circumference()
        self.s = self.set_content()

    def set_circumference(self):
        return 2 * Circle.pi * self.SX.get_len()

    def set_content(self):
        return Circle.pi * (self.SX.get_len() ** 2)

    def get_circumference(self):
        return self.o

    def get_content(self):
        return self.s

k = Circle([0, 0], [3, 4])
print(k.get_circumference(), k.get_content())