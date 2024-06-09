
class TestClass():
    pass


first_obj = TestClass()
second_obj = TestClass()


print("-"*25)

class Car():
    whells = 4



car = Car()
print(car.whells)

print("-"*25)

class Car():
    whells = 4

    def hello_car(self):
        print("Hello")

car = Car()
print(car.whells)
car.hello_car()


class Person():
    name = "Bob"
    age = 75

    def hello(self):
        print(f"Hello? my name is {self.name}, I`m {self.age} years old")

user1 = Person
#user1.hello()

user2 = Person()
user2.name = "Jack"
user2.name = 19
user2.hello()

print("-"*25)


class Car():

    car = Car()
    whells = 4
car.color = "red"
print(car.color)



car = Car()
new_attr = "engine"

print(dir(car))

if new_attr not in dir(car):
    car.engine = 1200
else:
    print(f"Attribute {new_attr} is already present in object car")

print("-"*25)


class Car():
    name = None
    wheels = None
    color = None

    def __init__(self, init_name, init_wheels, init_color):
        self.name = init_name
        self.wheels = init_wheels
        self.color = init_color

    def hello(self):
        print(f"My bame is {self.name}, I have {self.wheels} wheels and {color} color)

car = Car("sedan", 4, "green")
car.hello()

car2 = Car("sedan", 6, "green")
car2.hello()