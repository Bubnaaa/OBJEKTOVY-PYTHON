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

AB = Line([0, 0], [3, 4])
print(AB.get_len())
del AB

C = Point([0, 0])
D = Point([3, 4])
CD = Line(C.get_point(), D.get_point())
print(CD.get_len())
del CD

print(C, D)