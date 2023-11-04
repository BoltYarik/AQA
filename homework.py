class Figure:
    def get_perimeter(self):
        pass
    def get_square(self):
        pass


class Triangle(Figure):
    def __init__(self, side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        print(f'Perimeter of triangle = {perimeter}')

    def get_square(self):
        # get square of triangle using Geron formulа
        p = (self.side1 + self.side2 + self.side3) / 2
        s = p * (p - self.side1) * (p - self.side2) * (p - self.side3)
        square = s ** 0.5
        print(f'Square of triangle = {square}')


triangle = Triangle(3,3,3)
triangle.get_perimeter()
triangle.get_square()




class Round(Figure):

    def __init__(self, radius):
        self.radius = radius

    def get_square(self):
        square = 3.14 * (self.radius ** 2)
        print(f'Square of round = {square}')


    def get_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        print(f'Perimeter of round = {perimeter}')


round = Round(3)
round.get_square()
round.get_perimeter()