# Class - blueprint for creating objects - custom data type

# Came case - eg. helloThere

class Car: #Pascal case - eg. HelloThere
# Constructor - optional special method that sets up attributes of a new instance
# will be called automatically when a new instance is created
    def __init__(self, make, model): #self is passed implicitly by the interpreter
        # create an attribute 'make' and copy the value of the 'make' param into it
        self.__make = make #dot notation - <object>.<attr/method>
        self.model = model
        #implicity returns self
    
    def start(self):
        print(f'{self.__make} {self.model} started!')

    def display(self):
        return f'This is a {self.__make} {self.model}'
    
    #getter
    def get_make(self):
        return self.__make
    
    def set_make(self, new_make):
        pass

class PetrolCar(Car):
    def __init__(self, make, model, tank_capacity_l):
        self.__make = make
        self.model = model
        self.tank_capacity_l = tank_capacity_l

# Composition
class Engine:
    def __init__(self, type, max_power_kw):
        self.type = type
        self.max_power_kw = max_power_kw
    
    def __str__(self):
        return f'This is a {self.type} engine with a {self.max_power_kw}kw'

#Main
engine1 = Engine('petrol', max_power_kw=235)
my_car = PetrolCar('Honda', 'Civic', 47) # create a new istance of Car
your_car = Car('Toyota', 'Landcruiser')
# my-car is now an object of class 'Car'
#print(my_car.__dict__)
#print(your_car)
my_car.start()
your_car.start()
print(your_car.display)
print(my_car.make)

