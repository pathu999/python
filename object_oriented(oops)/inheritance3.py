class Car:
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand

    def display(self):
        print(self.color)
        print(self.brand)

class BMW(Car):
    def __init__(self, color, brand,price,size):
        self.price = price
        self.size = size
        super().__init__(color, brand)

       

    def display(self):
        super().display()
        print(self.price)
        print(self.size)


e=BMW("red","x5",45000000000,4*4)

e.display()
