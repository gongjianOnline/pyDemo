class Car:
    def run(self):
        print('run')

    def open(self):
        print('open')
        self.run()



car = Car()
car.open()
