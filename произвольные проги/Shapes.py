class Shape():
    def what_am_i(self):
        print("Я - фигура")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.w = w
        self.l = l

    def calculate_perimiter(self):
        return (self.w + self.l) * 2

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def calculate_perimiter(self):
        return self.s * 4

    def change_size(self, a):
        self.s += a

s1 = Rectangle(10,20)
print(s1.calculate_perimiter())

s2 = Square(4)
print(s2.calculate_perimiter())

s2.change_size(5)
print(s2.calculate_perimiter())

s1.what_am_i()
s2.what_am_i()

class Rider():
    def __init__(self, name):
        self.name = name

class Horse():
    def __init__(self, age, owner):
        self.age = age
        self.owner = owner

r = Rider("Мик Гордон")
h = Horse(12, r)
print("Возраст - {}\nХозяин - {}".format(h.age, h.owner.name))
