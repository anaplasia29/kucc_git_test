class Car:
    color=""
    speed=0

    def __init__(self, color, speed):
        self.color = "white"
        self.speed = 40

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed += value

redCar = Car()
blueCar = Car()

redCar.upSpeed(50)

print(redCar.speed)

"""class Car:
    color=""
    speed = 0
"""

