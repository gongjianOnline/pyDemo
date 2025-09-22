class Car:
    def run(self):
        print('run')

    def open(self):
        print('open')
        self.run()


if __name__ == '__main__':

    car = Car()
    car.open()
