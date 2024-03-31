class Car:
    def __init__(self, weight, engine):
        self.weight = weight
        self.engine = engine
    def lifeExpectance(self):
        return self.weight / self.engine
class Airplane:
    def __init__(self, numOfWings):
        self.numOfWings = numOfWings
    def lifeExpectance(self):
        return self.numOfWings / 15
class Hybrid(Airplane,Car):

    def __init__(self, weight, engine, numOfWings):
        super().__init__(numOfWings)
        super(Airplane,self).__init__(weight,engine)
        # Car.__init__(weight, engine)
        # Airplane.__init__(numOfWings)
        # MRO - method resolution order
hybrid1 =Hybrid(10,21,22)
# print(hybrid1)
print(Airplane.lifeExpectance(hybrid1))