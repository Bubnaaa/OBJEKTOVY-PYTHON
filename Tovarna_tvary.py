class Shape:
    def render(self):
        print("Initializing to render some shape...")

class Square(Shape):
    def render(self):
        super().render()
        print("Rendering square...")

class Triangle(Shape):
    def render(self):
        super().render()
        print("Rendering tringle...")

class Circle(Shape):
    def render(self):
        super().render()
        print("Rendering circle...")

class Pentagon(Shape):
    def render(self):
        super().render()
        print("Rendering pentagon...")

class House(Shape):
    def render(self):
        super().render()
        print("Rendering house...")

s1 = Square()
s1.render()

t1 = Triangle()
t1.render()

c1 = Circle()
c1.render()

p1 = Pentagon()
p1.render()

h1 = House()
h1.render()

class Factory:
    __article = ["Square", "Triangle", "Circle", "Pentagon", "House"]

    @staticmethod
    def create(representative):

        if representative in Factory.__article:
            return globals()[representative]()
        else:
            return Square()
        
my_square = Factory.create("Square")
my_square.render()

my_triangle = Factory.create("Triangle")
my_triangle.render()

my_circle = Factory.create("Circle")
my_circle.render()

my_pentagon = Factory.create("Pentagon")
my_pentagon.render()

my_house = Factory.create("House")
my_house.render()
