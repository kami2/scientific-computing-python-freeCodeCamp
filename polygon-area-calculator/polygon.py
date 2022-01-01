class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        display = f'Rectangle(width={self.width}, height={self.height})'
        return display

    def set_width(self, width_to_set):
        self.width = width_to_set
        return self.width

    def set_height(self, height_to_set):
        self.height = height_to_set
        return self.height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) **.5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        dimension = ((self.width * "*") + '\n') * self.height
        return dimension

    def get_amount_inside(self, shape):
        self.shape = shape
        amount_inside = self.get_area() / shape.get_area()
        return int(amount_inside)

class Square(Rectangle):

    def __init__(self, side_lenght):
        self.side_lenght = side_lenght
        self.width = self.side_lenght
        self.height = self.side_lenght

    def __str__(self):
        display = f"Square(side={self.width})"
        return display

    def set_side(self, side_to_set):
        self.set_width(side_to_set)
        self.set_height(side_to_set)



rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

check = Rectangle(10, 6)
print(check.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(check))


