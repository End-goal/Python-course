import random

Масті = ['Пік', 'Хрест', 'Чирва', ' Бубна']
значення = ['Туз', '2','3','4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король']
score = 0
колода = []

value = 0
for z in значення:
    value +=1
    for m in Масті:
        card = [f"{z} {m}", value]
        колода.append(card)
        print(card)

random.shuffle(колода)
card1 = колода.pop(0)

while True:
    print("Твій рахунок - ", score)
    print("\n\nПоточна карта - ", card1[0])

    while True:
        print("Вгадай наступну картку. (Б)ільше або (М)еньше")
        choice = input().lower()

        if len(choice) == 0 or choice[0] not in "бм":
            continue

        choice = choice[0]
        break

    card2 = колода.pop(0)
    print("наступна карта - ", card2[0])

    if card1[1] == card2[1]:
        print("Однаково")
    elif (choice == "б" and card1[1] < card2[1]) or \
        (choice == "м" and card1[1] > card2[1]):
        print("Вірно!")
        score += 1
    else:
        print("Не вірно!")
        break

    card1 = card2
    print()
    print("-"*25)
    print()

print("\n\nGAME OVER!")
print("\nФінальний рахунок - ", score)
