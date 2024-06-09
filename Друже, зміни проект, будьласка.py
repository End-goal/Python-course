import random


# x = input()
#
# try:
#     y = 1/int(x)
# except ZeroDivisionError:
#     print("bad, not a zero")
# except ValueError:
#     print("int")
# else:
#     print(y)
# finally:
#     print("Heavy: \"sex, now\"")

# МАСТІ = ['Хрест', 'Пік', 'Чирв', 'Бубн']
# ЗНАЧЕННЯ = ['Туз', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король']
# колода = []
# score = 0
#
# value = 0
# while True:
#     for z in ЗНАЧЕННЯ:
#         value += 1
#         for m in МАСТІ:
#             card = [z + ' ' + m, value]
#             колода.append(card)
#     random.shuffle(колода)
#     card1 = колода.pop(0)
#
#     while True:
#         print("\nВаші бали = ", score)
#         print("поточна карта -", card1[0])
#         user_input = input("Вгадай наступну карту. (Б)більше або (М)менше: ").lower()
#         if len(user_input) == 0 or user_input[0] not in "бм":
#             print("ram")
#             continue
#         guess = user_input[0]
#         break
#
#         card2 = колода.pop(0)
#         print("наступна карта -", card2[0])
#
#         if card1[1] == card2[1]:
#             print("Однаково!")
#         elif (card1[1] > card2[1] and guess == "м") or \
#              (card1[1] < card2[1] and guess == "б"):
#             print("Вірно!")
#             score += 1
#         else:
#             print("нєа")
#             break
#         card1 = card2
# print()
# print("-"*25)
# print("\nGAME OVER")
# print("Фінальний рахунок:", score)

input1 = input("number1 ")
input2 = input("number2 ")
input3 = input("number3 ")
lists = [input1, input2, input3]
dob = 1
for x in lists:
    try:
        dob = dob * int(x)
    except ValueError:
        print("fuck you")
print(dob)
