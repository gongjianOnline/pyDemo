
# 减肥
class WeighLoss:
    def __init__(self):
        self.weight = 100
    def eat(self):
        self.weight += 2
    def exercise(self):
        self.weight -= 0.5


if __name__ == '__main__':
    we = WeighLoss()
    we.eat()
    print(we.weight)
    we.exercise()
    print(we.weight)