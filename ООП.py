import time
import random
print("-" * 25)
print("-" * 25)


# class Car():
#
#     def __init__(self, init_fuel=0):
#         self.__fuel = init_fuel
#
#     @property
#     def fuel(self):
#         return self.__fuel
#
#     @fuel.setter
#     def fuel(self, value):
#         self.__fuel = value
#
# car = Car(30)
# car.fuel = 20
# print(car.fuel)

print("-" * 25)


# class Party():
#
#     def __init__(self, user):
#         self.user = user
#
#     def decor_party(func_to_decor):
#         def wrapper(*args, **kwargs):
#             print("we bought food and drinks, and hired a DJ-man")
#             res = func_to_decor(*args, **kwargs)
#             print("we need to take leftovers, throw all trash out, pay to the DJ-man")
#         return wrapper
#
#     @decor_party
#     def party(self):
#         print(f"host of party is {self.user}")
#
#     @decor_party
#     def no_party(self):
#         print(f"{self.user}'s parents came back, no party today")
#
#
# u_name = input("say the host's name: ")
# u_party = Party(u_name)
# u_inp = input(f"to be the party, or not to be?(Y/N): ")
#
# if u_inp[0] == "Y" or u_inp[0] == "y":
#     u_party.party()
# else:
#     u_party.no_party()

print("-" * 25)


# class Car():
#     __max_speed = 200
#     speed = property()
#
#     def __init__(self, init_speed=0):
#         self.__speed = init_speed
#
#     @speed.getter
#     def speed(self):
#         if self.__speed < 100:
#             print("YOU'RE TOO SLOW")
#         return self.__speed
#
#     @speed.setter
#     def speed(self, new_spd):
#         if new_spd > self.__max_speed:
#             print("IF YOU CONTINUE YOU WILL BECOME OUTLAW")
#         else:
#             print("fine")
#             self.__speed = new_spd
#
#     def time_it(func):
#         def wrapper(*args, **kwargs):
#             start_time = time.time()
#             result = func(*args, **kwargs)
#             time.sleep(random.randint(1, 10))
#             end_time = time.time()
#             print(f"ride time = {end_time - start_time} seconds")
#             return result
#         return wrapper
#
#     @time_it
#     def drive(self):
#         print("drive")
#
#
# car = Car(60)
# print(car.speed)
# car.speed= 120
# print()
# car.drive()


class Pers():

    def __init__(self, init_name):
        self.name = init_name

    def __repr__(self):
        return f"hi, I'm {self.name}"

    def __str__(self):
        return "I'm trying to be string"


p1 = Pers("penis")
print(p1)
