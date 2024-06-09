#a = 5
# b = 6
# if a>b:
#     print("Yes")
# else:
#     print("No")
# print("-"*100)
# color= input("Enter color - ")
#
# if color == "Black":
#     print("Box number 1")
# elif color == "White":
#     print("Box number 2")
# elif color == "Silver":
#     print("Box number 3")
# elif color == "Green":
#     print("Box number 4")
# elif color == "Red":
#     print("Box number 5")
# else:
#     print("There is no such color")
#
# print("-"*100)
#
# color= input("Enter color - ")
#
# if color == "Black" or color == "Blue":
#     print("Box number 1")
# elif color == "White" or color == "Silver":
#     print("Box number 2")
# elif color == "Yellow" or color == "Gold":
#     print("Box number 3")
# elif color == "Green" or color == "Orchid":
#     print("Box number 4")
# else:
#     print("There is no such color")
#
# print("-" * 100)
#
# color = input("Enter vechicle type car/truck - ")
# color = input("Enter color - ")
#
# if color == "car" and color == "Black":
#     print("Box number 1")
# elif color == "truck" and color == "Black":
#     print("Box number 2")
# elif color == "car" and color == "Blue":
#     print("Box number 3")
# elif color == "truck" and color == "Blue":
#     print("Box number 4")

# print("-" * 100)
#
# type = input("Enter vechicle type car/truck - ")
# color = input("Enter color - ")
#
# if color == "car" and (color == "Black" or color == "Blue"):
#     print("Box number 1")
# elif color == "truck" and (color == "Black" or color == "Blue"):
#     print("Box number 2")
# elif color == "car" and (color == "White" or color == "Silver"):
#     print("Box number 3")
# elif color == "truck" and (color == "White" or color == "Silver"):
#     print("Box number 4")
# cond=True
# x=0
# while cond:
#     print("Oops, I did it again...")
#     x = x + 1
#     if x > 10:
#         cond=False
#
x=0
while x<10:
    x=x+1
    if str(x) in "02468":
        print("Ya lubliu svoyu stranu...")
    if str(x) in "13579":
        print("Bachyty schos' dali doloni")
print("-"*25)
x=0
while x<10:
    x=x+1
    if str(x) in "02468":
        print("Ya lubliu svoyu stranu...")
        continue
    print("Bachyty schos' dali doloni")