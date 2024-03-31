class rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        area = self.width * self.length
        return area

class prism(rectangle):
    def __init__(self, width, height, length):
        super().__init__(width, length)
        self.height = height

    def volume(self):
        return self.area() * self.height

prism1 = prism(1,2,3)

print(prism1.volume())