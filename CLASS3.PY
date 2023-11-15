class Car():
    def __init__(self, name, speed, model, color, enginePower, nitroSpeed):
        # Initialize the Car object with the provided parameters
        self.name = name
        self.speed = speed
        self.model = model
        self.color = color
        self.enginePower = enginePower
        self.nitroSpeed = nitroSpeed
    
    def info(self):
        # Display information about the car
        print("The {} with a top speed of {} km/h, model {}, comes in a {} color. It features a high-performance engine with {} horsepower and a nitro speed boost for an acceleration of {}.".format(self.name, self.speed, self.model, self.color, self.enginePower, self.nitroSpeed))
    
    # The following methods are commented out because they are not implemented in the code
    # def turn():
    # def accelerate():
    # def brake():
    # def boost():
    # def start():
    # def stop():
    # def changeGear():

# Create instances of the Car class
car1 = Car("Bugatti W16", 420, 2023, "blue", 1500, 500)
car2 = Car("Dacia Duster", 1300, 2023, "white", 10000, 6000)

# Display information about each car
car1.info()
car2.info()
